from functools import wraps
from typing import Union, List

from pandas import DataFrame

from europy.lifecycle import reporting
from europy.lifecycle.test_result import TestLabel


def bias(name: str,
         description: str = ""):
    labels: List[TestLabel] = [TestLabel.BIAS]

    def inner_bias_wrapper(func):
        @wraps(func)
        def bias_wrapper(*args, **kwargs):
            result: Union[str, DataFrame, bool] = func(*args, **kwargs)
            test_result = reporting.capture(name, labels, result, description)
            return test_result

        return bias_wrapper

    return inner_bias_wrapper
