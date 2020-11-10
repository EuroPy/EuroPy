from enum import Enum
from typing import Union, List

from _pytest.mark import Mark
from pandas import DataFrame


class TestLabel(Enum):
    BIAS = "bias"
    FAIRNESS = "fairness"

    @staticmethod
    def of(mark: Mark):
        return TestLabel(mark.name)


class TestResult:
    def __init__(self, key: str, labels: List[TestLabel], result: Union[str, bool, DataFrame], description: str):
        self.key = key
        self.description = description
        self.labels = labels
        self.result = result
