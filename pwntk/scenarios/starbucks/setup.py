import os
import sys
import shutil
import filecmp
from sys import platform

import wget

from pwntk.utils.io import find_file_path
from pwntk.utils.logger import print_check, print_error
from pwntk.vars import vars

__all__ = ["ensure_scripts_folder", "download_scripts", "ensure_etter_conf"]

scripts_path = f"{vars.get('pwntk_home')}/mitmproxy/scripts"
sslstrip_url = "https://raw.githubusercontent.com/mitmproxy/mitmproxy/master/examples/complex/sslstrip.py"


# mitmdump

def ensure_scripts_folder():
    if not os.path.exists(scripts_path):
        os.makedirs(scripts_path)


def download_scripts():
    path = f"{scripts_path}/sslstrip.py"
    if os.path.exists(path):
        print_check(f"Found {path}, skipping download")
        return
    print("Downloading sslstrip.py ...")
    file = wget.download(sslstrip_url, path)
    print_check("\tFinished downloading")


def ensure_etter_conf():
    print("Checking ettercap config file diff from local optimal")
    search_path = "/etc"
    filename = "etter.conf"
    if platform == "darwin":
        search_path = "/usr/local"
    path_config = find_file_path(search_path, filename)
    local_config = f"{vars.get('src')}/scenarios/starbucks/scripts/{filename}"
    eq = filecmp.cmp(path_config, local_config)
    if eq:
        print_check(f"\t{filename} checked")
    else:
        print_error(f"""Ettercap config file differs from optimal for this attack.

Try to run this command:

    sudo cp {local_config} {path_config}
    
        """)
        sys.exit(1)
#    shutil.os.system('sudo cp "{}" "{}"'.format(file1, destination))
