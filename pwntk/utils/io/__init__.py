import os
import shlex
import time
import subprocess
from shutil import which
from typing import List
from subprocess import Popen, check_output

from pwntk.utils.logger import print_executing, print_check, print_kill_pid

__all__ = ["program_exists", "file_exists", "timestamp_file", "ensure_folder_exist",
           "kill_processes", "execute_cmd", "get_output_from_cmd"]


def program_exists(name: str) -> bool:
    return which(name) is not None


def file_exists(path: str) -> bool:
    return os.path.exists(path)


def find_file_path(path: str, filename: str) -> str:
    for root, dirs, files in os.walk(path):
        if filename in files:
            return f"{root}/{filename}"


def timestamp_file(filestr: str) -> str:
    timestr = time.strftime("%Y%m%d-%H%M%S")
    tok = filestr.split(".")
    tok[0] += f".{timestr}"
    return ".".join(tok)


def ensure_folder_exist(path: str):
    if not os.path.exists(path):
        os.makedirs(path)


def kill_processes(processes: List[Popen]):
    print("Cleaning up:")
    if len(processes) == 0:
        print("\tNo processes to clean")
    else:
        for p in processes:
            print_kill_pid(p.pid)
            p.kill()
        print_check("Finished cleaning processes")


def execute_cmd(cmd: str, sudo: bool = False) -> Popen:
    print_executing(cmd)
    if not sudo:
        proccess = Popen(shlex.split(cmd))
    else:
        proccess = Popen(shlex.split(cmd), stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    print_check(f"Started PID: {proccess.pid}")
    return proccess


def get_output_from_cmd(cmd: str) -> str:
    return check_output(shlex.split(cmd))
