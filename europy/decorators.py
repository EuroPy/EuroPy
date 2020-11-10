from functools import wraps
from typing import Union, List

from pandas import DataFrame

from europy.lifecycle import reporting
from europy.lifecycle.result import TestLabel, TestResult


def bias(name: str,
         description: str = ""):
    labels: List[TestLabel] = [TestLabel.BIAS]

    def inner_bias_wrapper(func):
        @wraps(func)
        def bias_wrapper(*args, **kwargs):
            result: Union[float, str, bool, DataFrame, TestResult] = func(*args, **kwargs)

            if isinstance(result, TestResult):
                labels.extend(result.labels)
                return reporting.capture(result.key, labels, result.result, result.description)
            else:
                return reporting.capture(name, labels, result, description)

        return bias_wrapper

    return inner_bias_wrapper
