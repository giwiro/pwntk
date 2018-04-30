#!/usr/bin/python3
from pwntk import scenario_names, BaseScenario
from pwntk.scenarios import StarbucksScenario
import argparse
import sys
from pprint import pprint

scenario: BaseScenario = None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="pwntk", description="Pawn toolkit")
    parser.add_argument("-l", "--list", action="store_true", help="List available scenarios")
    parser.add_argument("-s", "--scenario", action="store",
            help="Scenario to deploy")
    
    args, _ = parser.parse_known_args()

    # pprint(args)

    if args.list is True:
        print("\nScenarios\n----------")
        for name in scenario_names:
            print(name)
        print("\n")
        sys.exit(0)
    
    if args.scenario is None or args.scenario not in scenario_names:
        print("Please select a valid scenario.\nTo see the list use the paramter --list (-l)\n")
        sys.exit(0)

    # Evaluate and execute the scenario class
    if args.scenario == StarbucksScenario.name:
        scenario = StarbucksScenario()
    
    scenario.validate_options()
    scenario.validate_programs()

