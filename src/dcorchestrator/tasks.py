import luigi
import time
from tqdm import tqdm
import os

from .utils import (
    run_list_of_commands,
    create_full_dir_name,
    get_list_of_jobs_from_file,
    get_job_status,
    check_job_status,
    BaseNotifierClass,
)

root_dir = os.environ["ROOTDIR"]

kappa_naming_conv = {
    "YukawaConstrained": "Yukawa_NOTscalingbbH_couplingdependentBRs",
    "YukawaFloat": "Yukawa_NOTscalingbbH_floatingBRs",
    "TopCgKtConstrained": "Top_scalingttH_couplingdependentBRs",
    "TopCgKtFloat": "Top_scalingttH_floatingBRs",
    "TopKbKtConstrained": "Top_scalingbbHttH_couplingdependentBRs",
    "TopKbKtFloat": "Top_scalingbbHttH_floatingBRs",
}

def replace_mass_in_card(card):
    with open(card, "r") as f:
        lines = f.readlines()

    with open(card, "w") as f:
        for line in lines:
            if "$MASS" in line:
                line = line.replace("$MASS", "125")
            f.write(line)


def change_ooa_number_in_card(card):
    with open(card) as f:
        lines = f.readlines()
        process_lines = []
        for line in lines:
            if line.startswith("process"):
                process_lines.append(line.split()[1:])
        process_names, process_numbers = process_lines

    # make a dictionary of process names and numbers
    process_dict = {}
    for name, number in zip(process_names, process_numbers):
        if name not in process_dict:
            process_dict[name] = int(number)
    #print(process_dict)
    #print(len(process_dict))

    # order the dictionary by number
    process_dict = dict(sorted(process_dict.items(), key=lambda item: item[1]))
    #print(process_dict)

    # for all processes which contain OutsideAcceptance in the name, assign a negative number
    to_change = [k for k, v in process_dict.items() if "OutsideAcceptance" in k and v > 0]
    if to_change:
        for key in to_change:
            min_value = min(process_dict.values())
            current_ooa_value = process_dict[key]
            process_dict[key] = min_value - 1
            for key, value in process_dict.items():
                if value > current_ooa_value:
                    process_dict[key] = value - 1

        process_dict = dict(sorted(process_dict.items(), key=lambda item: item[1]))
        #print(process_dict)

        # make new process number line
        new_process_numbers = []
        for name in process_names:
            new_process_numbers.append(str(process_dict[name]))

        # add to lines and write to file
        # get index of process line
        index = 0
        for i, line in enumerate(lines):
            if line.startswith("process"):
                index = i
                break
        index += 1

        # replace process numbers
        lines[index] = "process " + " ".join(new_process_numbers) + "\n"

        with open(card, "w") as f:
            f.writelines(lines)


class CombineCards(BaseNotifierClass):
    channels = luigi.ListParameter()
    output_card_name = luigi.Parameter()
    extra_options = luigi.OptionalParameter(default="")
    replace_mass = luigi.BoolParameter(default=False)

    def output(self):
        return luigi.LocalTarget(self.output_card_name)

    def run(self):
        # create directory if it does not exist
        output_dir = "/".join(self.output_card_name.split("/")[:-1])
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        commands = [
            "combineCards.py {}".format(" ".join(self.channels))
            + self.extra_options
            + " > {}".format(self.output_card_name)
        ]
        to_further_append = """
#param_alphaS
nuisance edit add .*h(tt|ww|zz|zg|gg|mm)                  *                param_alphaS lnN 1.006
nuisance edit add .*hbb                                   *                param_alphaS lnN 0.992
nuisance edit add .*hcc                                   *                param_alphaS lnN 0.987
nuisance edit add .*hgluglu                               *                param_alphaS lnN 1.036

#param_mB
nuisance edit add .*h(ww|zz|gg|tt|zg|mm|cc|gluglu)        *                param_mB lnN 0.990
nuisance edit add .*hbb                                   *                param_mB lnN 1.007

#param_mC
nuisance edit add .*hcc                                   *                param_mC lnN 1.051

#param_mt -- 0,1 constraint global on this parameter
param_mt param 0 1

#HiggsDecayWidthTHU_hqq
nuisance edit add .*h(ww|zz|gg|tt|zg|mm|gluglu)           *                HiggsDecayWidthTHU_hqq lnN 0.997
nuisance edit add .*h(bb|cc)                              *                HiggsDecayWidthTHU_hqq lnN 1.002

#HiggsDecayWidthTHU_hvv
nuisance edit add .*h(ww|zz)                              *                HiggsDecayWidthTHU_hvv lnN 1.004

#HiggsDecayWidthTHU_hll
nuisance edit add .*h(tt|mm)                              *                HiggsDecayWidthTHU_hll lnN 1.005

#HiggsDecayWidthTHU_hgg
nuisance edit add .*hgg                                   *                HiggsDecayWidthTHU_hgg lnN 1.010

#HiggsDecayWidthTHU_hzg
nuisance edit add .*hzg                                   *                HiggsDecayWidthTHU_hzg lnN 1.050

#HiggsDecayWidthTHU_hgluglu
nuisance edit add .*hgluglu                               *                HiggsDecayWidthTHU_hgluglu lnN 1.029
"""

# note: CMS_res_j_18 is removed when runnung combineCards.py because of its small effect
# (check parseCard function)
# ifexists option does not seem to work, so remove the line completely
        to_further_append_systematics_httboost = """
nuisance edit rename * httboost.* THU_ggH_Mig01_ THU_ggH_Mig01 ifexists
nuisance edit rename * httboost.* THU_ggH_Mig12_ THU_ggH_Mig12 ifexists
nuisance edit rename * httboost.* THU_ggH_Mu_ THU_ggH_Mu ifexists
nuisance edit rename * httboost.* THU_ggH_PT120_ THU_ggH_PT120 ifexists
nuisance edit rename * httboost.* THU_ggH_PT60_ THU_ggH_PT60 ifexists
nuisance edit rename * httboost.* THU_ggH_Res_ THU_ggH_Res ifexists
nuisance edit rename * httboost.* THU_ggH_VBF2j_ THU_ggH_VBF2j ifexists
nuisance edit rename * httboost.* THU_ggH_VBF3j_ THU_ggH_VBF3j ifexists
nuisance edit rename * httboost.* THU_ggH_qmtop_ THU_ggH_qmtop ifexists
nuisance edit rename * httboost.* CMS_res_j2016 CMS_res_j_2016 ifexists
nuisance edit rename * httboost.* CMS_res_j2017 CMS_res_j_2017 ifexists
nuisance edit rename * httboost.* CMS_res_j2018 CMS_res_j_2018 ifexists
nuisance edit rename * httboost.* CMS_scale_j2016 CMS_scale_j_2016 ifexists
nuisance edit rename * httboost.* CMS_scale_j2017 CMS_scale_j_2017 ifexists
nuisance edit rename * httboost.* CMS_scale_j2018 CMS_scale_j_2018 ifexists
nuisance edit rename * httboost.* CMS_scale_met_unclustered2016 CMS_scale_met_unclustered_2016 ifexists
nuisance edit rename * httboost.* CMS_scale_met_unclustered2017 CMS_scale_met_unclustered_2017 ifexists
nuisance edit rename * httboost.* CMS_scale_met_unclustered2018 CMS_scale_met_unclustered_2018 ifexists
"""

        to_further_append_systematics_hgg = """
nuisance edit rename * hgg.* CMS_res_j_16 CMS_res_j_2016 ifexists
nuisance edit rename * hgg.* CMS_res_j_17 CMS_res_j_2017 ifexists
"""
        commands.append("echo '{}' >> {}".format(to_further_append, self.output_card_name))
        if "HttBoost" in self.output_card_name:
            commands.append("echo '{}' >> {}".format(to_further_append_systematics_httboost, self.output_card_name))
        if "Hgg" in self.output_card_name:
            commands.append("echo '{}' >> {}".format(to_further_append_systematics_hgg, self.output_card_name))
        
        run_list_of_commands(commands)

        if self.replace_mass:
            replace_mass_in_card(self.output_card_name)

        change_ooa_number_in_card(self.output_card_name)
        
        self.send_notification_complete()


class CreateSMWorkspace(BaseNotifierClass):
    datacard_path = luigi.Parameter()
    observable = luigi.Parameter()
    category = luigi.Parameter()
    combine_cards = luigi.OptionalParameter(default=None)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.output_dir = "{}/CombinedWorkspaces".format(root_dir)

    def requires(self):
        if self.combine_cards is not None:
            return self.combine_cards
        else:
            return []

    def output(self):
        return luigi.LocalTarget(
            f"{self.output_dir}/SM/{self.observable}/{self.category}.root"
        )

    def run(self):
        commands = [
            "produce_workspace.py --datacard {} --observable {} --category {} --output-dir {} --model SM".format(
                self.datacard_path, self.observable, self.category, self.output_dir
            )
        ]
        run_list_of_commands(commands)
        self.send_notification_complete()

class AlwaysCompleteTask(luigi.Task):
    def run(self):
        # Task logic goes here
        pass

    def complete(self):
        return True

class SubmitSMScans(BaseNotifierClass):
    category = luigi.Parameter()
    create_sm_workspace = luigi.TaskParameter()
    has_jobs = luigi.BoolParameter(default=True)
    global_fit_file = luigi.OptionalParameter(default=None)
    full_stat_task = luigi.TaskParameter(default=AlwaysCompleteTask())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.observable = self.create_sm_workspace.observable
        self.input_dir="{}/CombinedWorkspaces".format(root_dir)
        self.output_dir="{}/outputs/SM_scans".format(root_dir)
        self.full_output_dir = create_full_dir_name(
            self.output_dir, self.observable, self.category
        )
        if self.global_fit_file is not None:
            self.global_fit_file = "{}/{}".format(
                self.full_stat_task.full_output_dir, self.global_fit_file
            )

    def requires(self):
        requirements = [self.create_sm_workspace]
        if self.global_fit_file is not None:
            requirements.append(self.full_stat_task)
        return requirements

    def output(self):
        return luigi.LocalTarget(self.full_output_dir)

    def complete(self):
        """If there are log files in the output directory, jobs have been submitted.
        If there are not, then combine was run only locally
        """
        if not self.output().exists():
            return False
        if self.has_jobs:
            list_of_jobs = get_list_of_jobs_from_file(
                self.full_output_dir + "/jobs.txt"
            )
            # check status of jobs
            for job_id in list_of_jobs:
                status = get_job_status(job_id)
                if "RUNNING" in status or "PENDING" in status:
                    return False
            return True
        else:
            return self.output().exists()

    def run(self):
        # create output directory if it doesn't exist
        if not os.path.exists(self.full_output_dir):
            os.makedirs(self.full_output_dir)
        commands = [
            "submit_scans.py --model SM --observable {} --category {} --input-dir {}/SM/{} --output-dir {} --force-output-name".format(
                self.observable,
                self.category,
                self.input_dir,
                self.observable,
                self.full_output_dir,
            ) + " --global-fit-file {}".format(self.global_fit_file) * bool(self.global_fit_file),
        ]
        print("Running commands: {}".format(commands))
        run_list_of_commands(commands)
        if self.has_jobs:
            # wait 60 seconds for the jobs to be submitted
            time.sleep(60)
            list_of_jobs = get_list_of_jobs_from_file(
                self.full_output_dir + "/jobs.txt"
            )
            progress_bar = tqdm(total=len(list_of_jobs))
            check_job_status(list_of_jobs, get_job_status, progress_bar)
        self.send_notification_complete()


class CreateKappaWorkspace(luigi.Task):
    model = luigi.Parameter()
    category = luigi.Parameter()
    combine_cards = luigi.OptionalParameter(default=None)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model_arg = kappa_naming_conv[self.model]
        self.input_dir="{}/CombinedCards/TK".format(root_dir)
        self.output_dir="{}/CombinedWorkspaces/TK".format(root_dir)

    def requires(self):
        if self.combine_cards is not None:
            return self.combine_cards
        else:
            return []

    def output(self):
        return luigi.LocalTarget(
            "{}/{}_{}.root".format(self.output_dir, self.model_arg, self.category)
        )

    def run(self):
        commands = [
            "produce_TK_workspace.py --model {} --category {} --input-dir {} --output-dir {}".format(
                self.model_arg, self.category, self.input_dir, self.output_dir
            )
        ]
        run_list_of_commands(commands)


class SubmitKappaScans(BaseNotifierClass):
    category = luigi.Parameter()
    create_kappa_workspace = luigi.TaskParameter()
    has_jobs = luigi.BoolParameter(default=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = self.create_kappa_workspace.model
        self.input_dir = "{}/CombinedWorkspaces/TK".format(root_dir)
        self.output_dir = "{}/outputs/TK_scans".format(root_dir)
        self.full_output_dir = create_full_dir_name(
            self.output_dir, self.create_kappa_workspace.model_arg, self.category
        )

    def requires(self):
        return self.create_kappa_workspace

    def output(self):
        return luigi.LocalTarget(self.full_output_dir)

    def complete(self):
        """If there are log files in the output directory, jobs have been submitted.
        If there are not, then combine was run only locally
        """
        if not self.output().exists():
            return False
        if self.has_jobs:
            list_of_jobs = get_list_of_jobs_from_file(
                self.full_output_dir + "/jobs.txt"
            )
            # check status of jobs
            for job_id in list_of_jobs:
                status = get_job_status(job_id)
                if "RUNNING" in status or "PENDING" in status:
                    return False
            return True
        else:
            return self.output().exists()

    def run(self):
        commands = [
            "submit_TK_scans.py --model {} --category {} --input-dir {} --output-dir {} --force-output-name".format(
                self.create_kappa_workspace.model_arg,
                self.category,
                self.input_dir,
                self.full_output_dir,
            ),
        ]
        run_list_of_commands(commands)
        if self.has_jobs:
            # wait 60 seconds for the jobs to be submitted
            time.sleep(60)
            list_of_jobs = get_list_of_jobs_from_file(
                self.full_output_dir + "/jobs.txt"
            )
            progress_bar = tqdm(total=len(list_of_jobs))
            check_job_status(list_of_jobs, get_job_status, progress_bar)
        self.send_notification_complete()


class CreateSMEFTWorkspace(BaseNotifierClass):
    datacard = luigi.Parameter()
    model = luigi.Parameter()
    equations = luigi.Parameter()
    chan_obs = luigi.Parameter()
    linearised = luigi.BoolParameter(default=False)
    combine_cards = luigi.OptionalParameter(default=None)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config_file = (
            "{}/DifferentialCombinationRun2/metadata/SMEFT/{}.yml".format(
                root_dir, self.model
            )
        )
        self.equations_dir = "{}/EFTScalingEquations/equations/{}".format(
            root_dir, self.equations
        )
        self.chan_obs_file = (
            "{}/DifferentialCombinationRun2/metadata/SMEFT/config/{}.json".format(
                root_dir, self.chan_obs
            )
        )
        self.output_dir_to_pass = "{}/CombinedWorkspaces/SMEFT/{}".format(
            root_dir, self.equations
        )

    def requires(self):
        if self.combine_cards is not None:
            return self.combine_cards
        else:
            return []

    def output(self):
        self.output_root_file = "{}/{}/{}.root".format(
            self.output_dir_to_pass, self.model, self.chan_obs
        )
        return luigi.LocalTarget(self.output_root_file)

    def run(self):
        # create output directory if it doesn't exist
        if not os.path.exists(self.output_dir_to_pass):
            os.makedirs(self.output_dir_to_pass)

        commands = [
            "produce_SMEFT_workspace.py --datacard {} --config-file {} --equations-dir {} --chan-obs {} --output-dir {}".format(
                self.datacard,
                self.config_file,
                self.equations_dir,
                self.chan_obs_file,
                self.output_dir_to_pass,
            )
            + " --linearised" * self.linearised
        ]
        run_list_of_commands(commands)
        self.send_notification_complete()


class SubmitSMEFTScans(BaseNotifierClass):
    category = luigi.Parameter()
    submodel = luigi.Parameter(default=None)
    skip_twod = luigi.BoolParameter(default=False)
    create_smeft_workspace = luigi.TaskParameter()
    full_stat_task = luigi.TaskParameter(default=AlwaysCompleteTask())
    has_jobs = luigi.BoolParameter(default=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.chan_obs = self.create_smeft_workspace.chan_obs
        self.chan_obs_file = self.create_smeft_workspace.chan_obs_file
        self.model = self.create_smeft_workspace.model
        self.input_dir = "{}/{}".format(
            self.create_smeft_workspace.output_dir_to_pass, self.model
        )
        self.model_config_file = self.create_smeft_workspace.config_file
        if self.submodel is None:
            self.submodel_config_file = self.model_config_file
            self.submodel = self.model
        else:
            self.submodel_config_file = (
                "{}/DifferentialCombinationRun2/metadata/SMEFT/{}_{}.yml".format(
                    root_dir, self.model, self.submodel
                )
            )

        base_output_dir = "{}/outputs/SMEFT_scans".format(root_dir)
        # FreezeOthers case not considered yet
        cat_dct = {
            "observed": "",
            "asimov": "_asimov",
            "statonly": "_statonly",
            "statonly_asimov": "_statonly_asimov",
        }
        full_category = "{}{}".format(self.chan_obs, cat_dct[self.category])
        self.output_dir = "{}/{}/{}/{}-luigi".format(
            base_output_dir,
            self.model,
            self.submodel,
            full_category,
        )
        try:
            self.global_fit_dir = self.full_stat_task.output_dir
        except AttributeError:
            self.global_fit_dir = None

        self.commands = [
            "submit_SMEFT_scans.py --chan-obs {} --category {} --input-dir {} --output-dir {} --base-model {} --submodel {} --force-output-name".format(
                self.chan_obs_file,
                self.category,
                self.input_dir,
                self.output_dir,
                self.model_config_file,
                self.submodel_config_file,
            )
            + " --skip-2d" * self.skip_twod
            + " --global-fit-dir {}".format(self.global_fit_dir) * bool(self.global_fit_dir),
        ]

    def get_command_line(self):
        return self.commands[0]

    def requires(self):
        return self.create_smeft_workspace

    def output(self):
        return luigi.LocalTarget(self.output_dir)

    def complete(self):
        """If there are log files in the output directory, jobs have been submitted.
        If there are not, then combine was run only locally
        """
        print("Checking if complete: {}".format(self.get_command_line()))
        if not self.output().exists():
            return False
        if self.has_jobs:
            list_of_jobs = get_list_of_jobs_from_file(self.output_dir + "/jobs.txt")
            # check status of jobs
            for job_id in list_of_jobs:
                status = get_job_status(job_id)
                if "RUNNING" in status or "PENDING" in status:
                    return False
            return True
        else:
            return self.output().exists()

    def run(self):
        # create output directory if it doesn't exist
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        run_list_of_commands(self.commands)
        if self.has_jobs:
            # wait 60 seconds for the jobs to be submitted
            time.sleep(60)
            list_of_jobs = get_list_of_jobs_from_file(self.output_dir + "/jobs.txt")
            progress_bar = tqdm(total=len(list_of_jobs))
            check_job_status(list_of_jobs, get_job_status, progress_bar)
        self.send_notification_complete()