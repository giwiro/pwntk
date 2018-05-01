import os
import shlex
import time
from shutil import which
from subprocess import Popen, check_output
from typing import List

from pwntk.utils.logger import print_executing, print_check, print_kill_pid

__all__ = ["program_exists", "file_exists", "timestamp_file",
           "ensure_folder_exist", "execute_cmd"]


def program_exists(name: str) -> bool:
    return which(name) is not None


def file_exists(path: str) -> bool:
    return os.path.exists(path)


def timestamp_file(filestr: str) -> str:
    timestr = time.strftime("%Y%m%d-%H%M%S")
    tok = filestr.split(".")
    tok[0] += f".{timestr}"
    return ".".join(tok)


def ensure_folder_exist(path: str):
    if not os.path.exists(path):
        os.makedirs(path)


def kill_proccesses(processes: List[Popen]):
    print("Cleaning up:")
    if len(processes) == 0:
        print("\tNo processes to clean")
    else:
        for p in processes:
            print_kill_pid(p.pid)
            p.kill()
        print_check("Finished cleaning processes")


def execute_cmd(cmd: str) -> Popen:
    print_executing(cmd)
    proccess = Popen(shlex.split(cmd))
    print_check(f"Started PID: {proccess.pid}")
    return proccess


def get_output_from_cmd(cmd: str) -> str:
    return check_output(shlex.split(cmd))