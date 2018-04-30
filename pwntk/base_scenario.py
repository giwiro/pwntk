import sys
from typing import List
from abc import abstractmethod, ABCMeta
from pwntk.utils.file import program_exists, file_exists
from pwntk.utils.logger import print_check, print_error


class BaseScenario(metaclass=ABCMeta):
    name: str = None
    programs: List[str] = []
    files: List[str] = []

    @abstractmethod
    def validate_options(self, parser):
        pass

    @classmethod
    def validate_files(cls):
        if len(cls.files) > 0:
            for f in cls.files:
                if file_exists(f) is not True:
                    print_error(f"Could not find file in location: {f}\n")
                    sys.exit(0)
            print_check("All file dependencies checked")
        #else:
        #    print("No file dependencies to check")

    @classmethod
    def validate_programs(cls):
        if len(cls.programs) > 0:
            for p in cls.programs:
                if program_exists(p) is not True:
                    print_error(f"Could not find program: {p}\n")
                    sys.exit(0)
            print_check("All program dependencies checked")
        #else:
        #    print("No program dependencies to check")

    #@abstractmethod
    #def setup(self):
    #    pass

    @abstractmethod
    def run(self):
        pass