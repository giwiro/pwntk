import os
import wget
from pwntk.utils.logger import print_check
from pwntk.vars import vars

__all__ = ["ensure_scripts_folder", "download_scripts"]

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
