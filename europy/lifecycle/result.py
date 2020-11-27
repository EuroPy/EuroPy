from enum import Enum
from types import TracebackType
from typing import Union, List, Tuple, Type

from _pytest.mark import Mark
from pandas import DataFrame

from europy.lifecycle.report_figure import ReportFigure


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
                 figures: [ReportFigure],
                 description: str,
                 success: bool):
        self.key = key
        self.description = description
        self.labels = labels
        self.result = result
        self.figures: [ReportFigure] = figures
        self.success = success
