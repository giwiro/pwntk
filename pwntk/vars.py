import os
from pathlib import Path

__all__ = ["vars"]

home = str(Path.home())
root = os.path.dirname(os.path.abspath(__file__))

vars = {
    "home": home,
    "pwntk_home": f"{home}/.pwntk",
}

