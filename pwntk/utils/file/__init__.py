import os
import time
from shutil import which

__all__ = ["program_exists", "file_exists",
           "timestamp_file", "ensure_folder_exist"]


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
