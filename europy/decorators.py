from functools import wraps
from typing import Union, List

from pandas import DataFrame

from europy.lifecycle import reporting
from europy.lifecycle.result import TestLabel, TestResult


def test(label: str = "",
         name: str = "",
         description: str = ""):
    labels: List[Union[str, TestLabel]] = [label]

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


def bias(name: str = "",
         description: str = ""):
    labels: List[Union[str, TestLabel]] = [TestLabel.BIAS]

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


def data_bias(name: str = "",
              description: str = ""):
    labels: List[Union[str, TestLabel]] = [TestLabel.DATA_BIAS]

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


def fairness(name: str = "",
             description: str = ""):
    labels: List[Union[str, TestLabel]] = [TestLabel.FAIRNESS]

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


def accuracy(name: str = "",
             description: str = ""):
    labels: List[Union[str, TestLabel]] = [TestLabel.ACCURACY]

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


def unit(name: str = "",
         description: str = ""):
    labels: List[Union[str, TestLabel]] = [TestLabel.UNIT]

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


def integration(name: str = "",
                description: str = ""):
    labels: List[Union[str, TestLabel]] = [TestLabel.INTEGRATION]

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


def minimum_functionality(name: str = "",
                          description: str = ""):
    labels: List[Union[str, TestLabel]] = [TestLabel.MINIMUM_FUNCTIONALITY]

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
