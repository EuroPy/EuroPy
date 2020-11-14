from functools import wraps
from typing import Union, List

from pandas import DataFrame

from europy.lifecycle import reporting
from europy.lifecycle.result import TestLabel, TestResult


def __inner_wrapper_factory(labels: List[Union[str, TestLabel]],
                            name: str,
                            description: str):
    def inner_wrapper(func):
        @wraps(func)
        def func_wrapper(*args, **kwargs):
            result: Union[float, str, bool, DataFrame, TestResult] = func(*args, **kwargs)

            if isinstance(result, TestResult):
                labels.extend(result.labels)
                return reporting.capture(result.key, labels, result.result, result.description)
            else:
                return reporting.capture(name, labels, result, description)

        return func_wrapper

    return inner_wrapper


def test(label: str = "",
         name: str = "",
         description: str = ""):
    labels: List[Union[str, TestLabel]] = [label]

    return __inner_wrapper_factory(labels, name, description)


def bias(name: str = "",
         description: str = ""):
    labels: List[Union[str, TestLabel]] = [TestLabel.BIAS]

    return __inner_wrapper_factory(labels, name, description)


def data_bias(name: str = "",
              description: str = ""):
    labels: List[Union[str, TestLabel]] = [TestLabel.DATA_BIAS]

    return __inner_wrapper_factory(labels, name, description)


def fairness(name: str = "",
             description: str = ""):
    labels: List[Union[str, TestLabel]] = [TestLabel.FAIRNESS]

    return __inner_wrapper_factory(labels, name, description)


def accuracy(name: str = "",
             description: str = ""):
    labels: List[Union[str, TestLabel]] = [TestLabel.ACCURACY]

    return __inner_wrapper_factory(labels, name, description)


def unit(name: str = "",
         description: str = ""):
    labels: List[Union[str, TestLabel]] = [TestLabel.UNIT]

    return __inner_wrapper_factory(labels, name, description)


def integration(name: str = "",
                description: str = ""):
    labels: List[Union[str, TestLabel]] = [TestLabel.INTEGRATION]

    return __inner_wrapper_factory(labels, name, description)


def minimum_functionality(name: str = "",
                          description: str = ""):
    labels: List[Union[str, TestLabel]] = [TestLabel.MINIMUM_FUNCTIONALITY]

    return __inner_wrapper_factory(labels, name, description)
