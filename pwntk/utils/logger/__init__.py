import emoji
from typing import NamedTuple

__all__ = ["Bcolors", "print_error", "print_check", "print_executing", "print_kill_pid"]


class Bcolors(NamedTuple):
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_error(msg: str):
    print(f"{Bcolors.FAIL}Error: {msg}{Bcolors.ENDC}")


def print_check(msg: str):
    print(emoji.emojize(f"{msg} {Bcolors.OKGREEN}:heavy_check_mark:{Bcolors.ENDC}", use_aliases=True))


def print_kill_pid(pid: int):
    print(emoji.emojize(f":hocho: Killing PID: {pid}", use_aliases=True))


def print_executing(cmd: str):
    print(emoji.emojize(f":computer: {Bcolors.OKGREEN}Executing:{Bcolors.ENDC} {Bcolors.OKBLUE}{cmd}{Bcolors.ENDC}", use_aliases=True))
