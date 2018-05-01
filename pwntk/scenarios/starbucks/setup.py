import os
import shlex
import subprocess
from subprocess import Popen

import wget
from sys import platform

from pwntk.utils.io import execute_cmd, kill_proccesses, get_output_from_cmd
from pwntk.utils.logger import print_check
from pwntk.vars import vars

__all__ = ["ensure_scripts_folder", "download_scripts", "ensure_port_fwd"]

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


# ettercap (spoof arp table)
def ensure_port_fwd():
    proccesses = []
    fwd_var = "net.ipv4.ip_forward"
    print(f"Checking port forwarding for arquitecture: {platform}")
    if platform == "darwin":
        fwd_var = "net.inet.ip.forwarding"
    cmd_red = f"sysctl -n {fwd_var}"
    sysctl_read_out = get_output_from_cmd(cmd_red)
    print(sysctl_read_out)

    p = Popen(shlex.split(cmd_red), stdout=subprocess.PIPE)
    result = p.communicate()[0]
    print(result)
    # kill_proccesses(proccesses)
