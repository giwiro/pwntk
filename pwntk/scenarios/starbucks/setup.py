import os
import shutil
from sys import platform

import wget

from pwntk.utils.io import find_file_path
from pwntk.utils.logger import print_check
from pwntk.vars import vars

__all__ = ["ensure_scripts_folder", "download_scripts", "ensure_copy_etter_conf"]

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
    print_check("Finished downloading")


def ensure_copy_etter_conf():
    search_path = "/etc"
    filename = "etter.conf"
    if platform == "darwin":
        search_path = "/usr/local"
    path = find_file_path(search_path, filename)
    print(f"found: {path}")
#    shutil.os.system('sudo cp "{}" "{}"'.format(file1, destination))
