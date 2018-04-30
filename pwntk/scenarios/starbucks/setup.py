#!/usr/bin/env python3
import os
import wget
from pathlib import Path

home = str(Path.home())

scripts_path = f"{home}/.pwntk/mitmproxy/scripts"
sslstrip_url = "https://raw.githubusercontent.com/mitmproxy/mitmproxy/master/examples/complex/sslstrip.py"

def ensure_scripts_folder():
    if not os.path.exists(scripts_path):
        os.makedirs(scripts_path)

def download_scripts():
    path = f"{scripts_path}/sslstrip.py"
    if os.path.exists(path):
        print("Found sslstrip.py, skipping download")
        return
    print("Downloading sslstrip.py")
    file = wget.download(sslstrip_url, path)
    print("\n")

ensure_scripts_folder()
download_scripts()