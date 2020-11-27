import sys
from types import TracebackType
from typing import List, Union, Tuple, Type

from pandas import DataFrame

from europy.lifecycle.report import TestResult, TestLabel
from europy.lifecycle.report_figure import ReportFigure


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
        for label in other.labels:
            if label not in self.labels:
                self.labels.append(label)
        if self.key is None and other.key is not None:
            self.key = other.key
        if self.description is None and other.description is not None:
            self.description = other.description

    def execute(self, *args, **kwargs) -> TestResult:
        print(f"Execute - {self.key} ({self.labels})")
        try:

            plots = {}
            if "plots" in kwargs.keys():
                kwargs["plots"] = plots

            result: Union[float, str, bool, DataFrame] = self.func(*args, **kwargs)
            print(f"\tPASS")

            return TestResult(self.key,
                              self.labels,
                              result=result,
                              figures=[ReportFigure.of(name, plot) for name, plot in plots.items()],
                              description=self.description,
                              success=True)
        except:
            error_info: Union[Tuple[Type[BaseException], BaseException, TracebackType], Tuple[None, None, None]] = \
                sys.exc_info()[0]
            print(f"\tFAIL")
            return TestResult(self.key,
                              self.labels,
                              result=str(error_info),
                              figures=[],
                              description=self.description,
                              success=False)
