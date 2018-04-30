from typing import List
from abc import abstractmethod, ABCMeta

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
            print("validating programs")

