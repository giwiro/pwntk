import sys
from typing import List
from abc import abstractmethod, ABCMeta
from pwntk.utils.file import file_exists

class BaseScenario(metaclass=ABCMeta):
    name: str = None
    programs: List[str] = []

    @staticmethod
    @abstractmethod
    def validate_options():
        pass

    @classmethod
    def validate_programs(cls):
        if len(cls.programs) > 0:
            for p in cls.programs:
                if file_exists(p) is not True:
                    print(f"Could not find program in location: {p}\n")
                    sys.exit(0)
               

