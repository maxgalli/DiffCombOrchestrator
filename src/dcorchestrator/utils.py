import subprocess
import os
import time
import luigi
import requests


def run_list_of_commands(list_of_commands):
    print("Running list of commands:")
    print(list_of_commands)
    for command in list_of_commands:
        process = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
        )
        out, err = process.communicate()
        if (process.returncode != 0 or err) and "Warning" not in err:
            raise RuntimeError(
                f"Command {command} failed with error code {process.returncode} and error message {err}"
            )
        print(f"Command: {command}\nOutput: {out}")


def get_list_of_jobs_from_logs(logs_dir):
    """
    Very shacky. Within each directory there are jobs whose name look like
    slurm__SCAN_r_smH_PTH_45_80_HWW_422095_10.log
    and in this case the job id is 422095_10
    """
    list_of_jobs = []
    for log_file in os.listdir(logs_dir):
        if log_file.endswith(".log"):
            log_file_no_ext = log_file.split(".")[0]
            job_id = "_".join(log_file_no_ext.split("_")[-2:])
            list_of_jobs.append(job_id)
    return list_of_jobs


def get_list_of_jobs_from_file(file_path):
    """_summary_
    In the patched version of stupid harvester, I dump a txt file with the list of jobs
    Each line a job id.
    This is done because get_list_of_jobs_from_logs would not consider the pending jobs
    """
    list_of_jobs = []
    with open(file_path, "r") as f:
        for line in f.readlines():
            list_of_jobs.append(line.strip())
    return list_of_jobs


def get_job_status(job_id):
    while True:
        try:
            output = subprocess.check_output(
                ["sacct", "-j", job_id, "--format", "State", "--noheader"]
            )
            status = output.decode("utf-8").strip()
            return status
        except subprocess.CalledProcessError:
            print('Failed to get job status. Retrying...')
            time.sleep(1)


def check_job_status(job_ids, get_job_status, progress_bar):
    total_jobs = len(job_ids)
    finished_jobs = []
    n_finished_jobs = 0

    while True:
        jobs_to_check = list(set(job_ids) - set(finished_jobs))
        for job_id in jobs_to_check:
            status = get_job_status(job_id)

            if "COMPLETED" in status or "FAILED" in status:
                finished_jobs.append(job_id)
            n_finished_jobs = len(finished_jobs)

        progress_bar.update(n_finished_jobs - progress_bar.n)

        if n_finished_jobs == total_jobs:
            progress_bar.close()
            return

        time.sleep(10)  # Delay for 5 seconds


def create_full_dir_name(output_dir, observable, category):
    output_path = "{}/{}/{}-luigi".format(output_dir, observable, category)
    return output_path

class BaseNotifierClass(luigi.Task):

    def get_task_info(self):
        param_str = ',\n'.join(f"{k}={v}" for k, v in self.param_kwargs.items())
        return f"{self.__class__.__name__}(\n{param_str}\n)"

    def send_notification_complete(self):
        webhook_url = "https://mattermost.web.cern.ch/hooks/rwkmpscjwpfytgdfu4qz5nnyur"
        message = "Task\n {} \ncompleted successfully!".format(self.get_task_info())
        payload = {"text": message}
        response = requests.post(webhook_url, json=payload)

        if response.status_code == 200:
            print("Notification sent successfully")
        else:
            print("Failed to send notification") 