#!/usr/bin/env python3
import argparse
import os
import sys
from pwntk import scenario_names
from pwntk.base_scenario import BaseScenario
from pwntk.scenarios import StarbucksScenario
from pwntk.utils.file import ensure_folder_exist
from pwntk.vars import vars

from pwntk.utils.logger import print_error

scenario: BaseScenario = None


def ensure_pwntk_home():
    ensure_folder_exist(vars.get('pwntk_home'))


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
        sys.exit(0)

    if args.scenario is None or args.scenario not in scenario_names:
        print_error("Please select a valid scenario.\nTo see the list use the paramter --list (-l)\n")
        sys.exit(0)

    # Evaluate and execute the scenario class
    if args.scenario == StarbucksScenario.name:
        scenario = StarbucksScenario()

    ensure_pwntk_home()

    scenario.validate_options(parser)
    scenario.setup()
    scenario.validate_programs()
    scenario.validate_files()
    scenario.run()

    while True:
        pass
