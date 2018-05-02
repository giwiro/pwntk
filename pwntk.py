#!/usr/bin/env python3
import argparse
import signal
import sys
from pwntk import scenario_names
from pwntk.base_scenario import BaseScenario
from pwntk.scenarios import StarbucksScenario
from pwntk.utils.io import ensure_folder_exist
from pwntk.vars import vars

from pwntk.utils.logger import print_error

scenario: BaseScenario = None


def print_banner():
    print(f"""\
                     _              _ _    _ _   
 _ ____      ___ __ | |_ ___   ___ | | | _(_| |_ 
| '_ \ \ /\ / | '_ \| __/ _ \ / _ \| | |/ | | __|
| |_) \ V  V /| | | | || (_) | (_) | |   <| | |_ 
| .__/ \_/\_/ |_| |_|\__\___/ \___/|_|_|\_|_|\__| v0.0.1
|_|  
    - Greetings, Professor Falken
    - Hello
    """)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="pwntk", description="Pawn toolkit")
    parser.add_argument("-l", "--list", action="store_true", help="List available scenarios")
    parser.add_argument("-s", "--scenario", action="store", help="Scenario to deploy")

    args, _ = parser.parse_known_args()

    if args.list is True:
        print("\nScenarios\n----------")
        for name in scenario_names:
            print(name)
        print("\n")
        sys.exit(1)

    if args.scenario is None or args.scenario not in scenario_names:
        print_error("Please select a valid scenario.\nTo see the list use the paramter --list (-l)\n")
        sys.exit(1)

    # Evaluate and execute the scenario class
    if args.scenario == StarbucksScenario.name:
        scenario = StarbucksScenario()

    ensure_folder_exist(vars.get('pwntk_home'))

    scenario.validate_options(parser)
    scenario.setup()
    scenario.validate_programs()
    scenario.validate_files()
    print_banner()
    scenario.print_name()
    scenario.run()

    signal.pause()
