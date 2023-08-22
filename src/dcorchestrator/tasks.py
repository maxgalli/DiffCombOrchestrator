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


class CombineCards(BaseNotifierClass):
    channels = luigi.ListParameter()
    output_card_name = luigi.Parameter()
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
            + " > {}".format(self.output_card_name)
        ]
        run_list_of_commands(commands)

        if self.replace_mass:
            replace_mass_in_card(self.output_card_name)
        
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
        commands = [
            "submit_scans.py --model SM --observable {} --category {} --input-dir {}/SM/{} --output-dir {} --force-output-name".format(
                self.observable,
                self.category,
                self.input_dir,
                self.observable,
                self.full_output_dir,
            ) + " --global-fit-file {}".format(self.global_fit_file) * bool(self.global_fit_file),
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


class CreateKappaWorkspace(luigi.Task):
    model = luigi.Parameter()
    category = luigi.Parameter()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model_arg = kappa_naming_conv[self.model]
        self.input_dir="{}/CombinedCards/TK".format(root_dir)
        self.output_dir="{}/CombinedWorkspaces/TK".format(root_dir)

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

    def requires(self):
        return self.create_smeft_workspace

    def output(self):
        return luigi.LocalTarget(self.output_dir)

    def complete(self):
        """If there are log files in the output directory, jobs have been submitted.
        If there are not, then combine was run only locally
        """
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

        commands = [
            "submit_SMEFT_scans.py --chan-obs {} --category {} --input-dir {} --output-dir {} --base-model {} --submodel {} --force-output-name".format(
                self.chan_obs_file,
                self.category,
                self.input_dir,
                self.output_dir,
                self.model_config_file,
                self.submodel_config_file,
            )
            + " --skip-2d" * self.skip_twod
        ]
        run_list_of_commands(commands)
        if self.has_jobs:
            # wait 60 seconds for the jobs to be submitted
            time.sleep(60)
            list_of_jobs = get_list_of_jobs_from_file(self.output_dir + "/jobs.txt")
            progress_bar = tqdm(total=len(list_of_jobs))
            check_job_status(list_of_jobs, get_job_status, progress_bar)
        self.send_notification_complete()