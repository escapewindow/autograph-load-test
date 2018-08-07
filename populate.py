#!/usr/bin/env python
from __future__ import print_function

from copy import deepcopy
import json
import os
import shutil

SOURCE_DIR = "/builds/scriptworker/aki"
TARGET_DIR = "/builds/scriptworker/load"


def work_dir(parent):
    return os.path.join(parent, "work")


def cot_dir(parent):
    return os.path.join(work_dir(parent), "cot", "eiQZF2TcT2q8_ILvb2d_tQ", "public", "build")


def artifact_dir(parent):
    return os.path.join(parent, "artifacts")


def task_json_path(parent):
    return os.path.join(work_dir(parent), "task.json")


def mar_path(parent):
    return os.path.join(cot_dir(parent), "target.complete.mar")


def config_path(parent):
    return os.path.join(parent, "script_config.json")


def script_path(parent):
    return os.path.join(parent, "run.sh")


def mkdir_p(path):
    if not os.path.exists(path):
        print("mkdir: {}".format(path))
        os.makedirs(path)


def copyfile(from_, to):
    print("Copy {} to {}".format(from_, to))
    shutil.copyfile(from_, to)


def create_config(target_config, source_config):
    config = deepcopy(source_config)
    config['work_dir'] = work_dir(target_config['target_dir'])
    config['artifact_dir'] = work_dir(target_config['artifact_dir'])
    with open(config_path(target_config['target_dir']), "w") as fh:
        json.dump(config, fh, indent=2, sort_keys=True)


if __name__ == '__main__':

    source_task_json = task_json_path(SOURCE_DIR)
    source_mar = mar_path(SOURCE_DIR)
    source_script = script_path(SOURCE_DIR)

    with open(config_path(SOURCE_DIR), "r") as fh:
        source_config = json.load(fh)

    for i in range(1, 21):
        localconfig = {}
        localconfig['target_dir'] = os.path.join(TARGET_DIR, str(i))
        localconfig['cot_dir'] = cot_dir(localconfig['target_dir'])
        localconfig['artifact_dir'] = artifact_dir(localconfig['target_dir'])
        target_task_json = task_json_path(localconfig['target_dir'])
        target_mar = mar_path(localconfig['target_dir'])
        target_script = script_path(localconfig['target_dir'])
        mkdir_p(localconfig['artifact_dir'])
        mkdir_p(localconfig['cot_dir'])
        copyfile(source_task_json, target_task_json)
        copyfile(source_mar, target_mar)
        copyfile(source_script, target_script)
        create_config(localconfig, source_config)
