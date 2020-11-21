import sys
from enum import Enum
from types import TracebackType
from typing import Union, List, Tuple, Type

from _pytest.mark import Mark
from pandas import DataFrame


class TestLabel(str, Enum):
    BIAS = "bias"
    DATA_BIAS = "data-bias"
    FAIRNESS = "fairness"
    TRANSPARENCY = "transparency"
    ACCOUNTABILITY = "accountability"
    UNIT = "unit"
    INTEGRATION = "integration"
    ACCURACY = "accuracy"
    MINIMUM_FUNCTIONALITY = "minimum-functionality"

    @staticmethod
    def of(mark: Mark):
        return TestLabel(mark.name)

    def __json__(self):
        return str(self.value)

    def __str__(self):
        return str(self.value)


class TestResult:
    def __init__(self,
                 key: str,
                 labels: List[str],
                 result: Union[
                     float, str, bool, DataFrame, Tuple[Type[BaseException], BaseException, TracebackType], Tuple[
                         None, None, None]],
                 description: str,
                 success: bool):
        self.key = key
        self.description = description
        self.labels = labels
        self.result = result
        self.success = success


class TestPromise:
    def __init__(self,
                 key: str = None,
                 labels: List[Union[str, TestLabel]] = None,
                 func=None,
                 description: str = None):
        self.key = key
        self.description = description
        self.labels = [str(label) for label in labels]
        self.func = func

    def merge(self, other):
        if len(other.labels) > 0:
            self.labels = self.labels + other.labels
        if self.key is None and other.key is not None:
            self.key = other.key
        if self.description is None and other.description is not None:
            self.description = other.description

    def execute(self, *args, **kwargs) -> TestResult:
        print(f"Execute - {self.key} ({self.labels})")
        try:
            result: Union[float, str, bool, DataFrame] = self.func(*args, **kwargs)
            print(f"\tPASS")
            return TestResult(self.key,
                              self.labels,
                              result,
                              self.description,
                              success=True)
        except:
            error_info: Union[Tuple[Type[BaseException], BaseException, TracebackType], Tuple[None, None, None]] = \
                sys.exc_info()[0]
            print(f"\tFAIL")
            return TestResult(self.key,
                              self.labels,
                              result=str(error_info),
                              description=self.description,
                              success=False)
