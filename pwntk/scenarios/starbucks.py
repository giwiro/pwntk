import sys
from pwntk.base_scenario import BaseScenario

class StarbucksScenario(BaseScenario):
    name = "starbucks"
    programs = ["/usr/bin/mitmdump", "/usr/bin/ettercap"]

    @staticmethod
    def validate_options():
        print("Holis")
