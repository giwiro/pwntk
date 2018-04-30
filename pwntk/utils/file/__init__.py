import os.path
import time

__all__ = ["file_exists", "timestamp_file"]

def file_exists(path: str) -> bool:
    return os.path.exists(path)

def timestamp_file(filestr: str) -> str:
    timestr = timestr = time.strftime("%Y%m%d-%H%M%S")
    tok = filestr.split(".")
    tok[0] += f".{timestr}"
    return ".".join(tok)
