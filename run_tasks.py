#!/usr/bin/env python3
# PYTHON_ARGCOMPLETE_OK
import luigi
import os
import argparse
import argcomplete

from dcorchestrator.instances import instances

def get_tasks(parsed_args, **kwargs):
    tasks = []
    for task in instances:
        tasks.append(task)
    return tasks

parser = argparse.ArgumentParser()
parser.add_argument("tasks", nargs='+', type=str, help="Tasks to run").completer = get_tasks
argcomplete.autocomplete(parser)
args = parser.parse_args()
luigi.build([instances[task] for task in args.tasks], local_scheduler=True)