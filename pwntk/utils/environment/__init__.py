import os

PWNTK_DEV = "PWNTK_DEV"

__all__ = ["is_dev"]

def is_dev():
    return os.environ.get(PWNTK_DEV, None) is not None

