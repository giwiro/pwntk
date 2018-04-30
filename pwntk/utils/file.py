from os import path

__all__ = ["file_exists"]

def file_exists(path: str) -> bool:
    return os.path.exists(path)

