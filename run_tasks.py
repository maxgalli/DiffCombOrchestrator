#!/usr/bin/env python3
# PYTHON_ARGCOMPLETE_OK
import luigi
import os
import argparse
import argcomplete

from dcorchestrator.instances import instances

def print_task_info(task):
    # recursive function to print the task info and the info of its dependencies
    print("\n\n")
    print(task.get_task_info())
    print("Command: {}".format(task.get_command_line()))
    deps = task.requires()
    # if not a list of tasks, make it a list
    if not isinstance(deps, list):
        deps = [deps]
    for dep in deps:
        print_task_info(dep)

def get_tasks(parsed_args, **kwargs):
    tasks = []
    for task in instances:
        tasks.append(task)
    return tasks

parser = argparse.ArgumentParser()
parser.add_argument("tasks", nargs='+', type=str, help="Tasks to run").completer = get_tasks
argcomplete.autocomplete(parser)
parser.add_argument("--test", action="store_true", help="Plot comands without running them", default=False)
args = parser.parse_args()
if args.test:
    for task in args.tasks:
        print_task_info(instances[task])
else:
    luigi.build([instances[task] for task in args.tasks], local_scheduler=True)