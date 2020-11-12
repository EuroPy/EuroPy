from enum import Enum
from typing import Union, List

from _pytest.mark import Mark
from pandas import DataFrame


class TestLabel(str, Enum):
    BIAS = "bias"
    FAIRNESS = "fairness"
    TRANSPARENCY = "transparency"
    ACCOUNTABILITY = "accountability"

    @staticmethod
    def of(mark: Mark):
        return TestLabel(mark.name)

    def __json__(self):
        return str(self.value)

    def description(self):
        if (self == BIAS):
            return ""
        if (self == FAIRNESS):
            return ""
        if (self == TRANSPARENCY):
            return ""
        if (self == ACCOUNTABILITY):
            return ""


class TestResult:
    def __init__(self, key: str,
                 labels: List[TestLabel],
                 result: Union[float, str, bool, DataFrame],
                 description: str):
        self.key = key
        self.description = description
        self.labels = labels
        self.result = result
