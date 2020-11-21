from functools import wraps
from typing import Union, List

from pandas import DataFrame

from europy.lifecycle import reporting
from europy.lifecycle.model_details import ModelDetails
from europy.lifecycle.reporting import put_test
from europy.lifecycle.result import TestLabel, TestResult, TestPromise


def isnotebook():
    try:
        shell = get_ipython()
        return True
    except NameError:
        return False


def decorator_factory(labels: List[Union[str, TestLabel]],
                      name: str = "",
                      description: str = ""):
    def inner_wrapper(func):
        if isnotebook():
            put_test(TestPromise(name, labels, func, description))

        @wraps(func)
        def func_wrapper(*args, **kwargs):
            result: Union[float, str, bool, DataFrame, TestResult] = func(*args, **kwargs)

            if not isinstance(result, TestResult):
                # labels.extend(result.labels)
                # return reporting.capture(result.key, labels, result.result, result.description)
                # else:
                return reporting.capture(name, labels, result, description)

        return func if isnotebook() else func_wrapper

    return inner_wrapper


def test(label: str = "",
         name: str = None,
         description: str = None):
    labels: List[Union[str, TestLabel]] = [label]

    return decorator_factory(labels, name, description)


def bias(name: str = None,
         description: str = None,
         x=None):
    labels: List[Union[str, TestLabel]] = [TestLabel.BIAS]
    return decorator_factory(labels, name, description)


def data_bias(name: str = None,
              description: str = None):
    labels: List[Union[str, TestLabel]] = [TestLabel.DATA_BIAS]

    return decorator_factory(labels, name, description)


def fairness(name: str = None,
             description: str = None):
    labels: List[Union[str, TestLabel]] = [TestLabel.FAIRNESS]

    return decorator_factory(labels, name, description)


def transparency(name: str = None,
                 description: str = None):
    labels: List[Union[str, TestLabel]] = [TestLabel.TRANSPARENCY]

    return decorator_factory(labels, name, description)


def accountability(name: str = None,
                   description: str = None):
    labels: List[Union[str, TestLabel]] = [TestLabel.ACCOUNTABILITY]

    return decorator_factory(labels, name, description)


def accuracy(name: str = None,
             description: str = None):
    labels: List[Union[str, TestLabel]] = [TestLabel.ACCURACY]

    return decorator_factory(labels, name, description)


def unit(name: str = None,
         description: str = None):
    labels: List[Union[str, TestLabel]] = [TestLabel.UNIT]

    return decorator_factory(labels, name, description)


def integration(name: str = None,
                description: str = None):
    labels: List[Union[str, TestLabel]] = [TestLabel.INTEGRATION]

    return decorator_factory(labels, name, description)


def minimum_functionality(name: str = None,
                          description: str = None):
    labels: List[Union[str, TestLabel]] = [TestLabel.MINIMUM_FUNCTIONALITY]

    return decorator_factory(labels, name, description)


def model_details(file_path: str = None):
    """Adds a model details to the Report.

    Args:
        file_path (str, optional): Path to model details JSON file. Defaults to None.
    """

    def inner_wrapper(func):
        @wraps(func)
        def inner_func_wrapper(*args, **kwargs):
            import json

            # pull current report (generated @ __init__)
            details = reporting.get_report().model_card['details']

            if file_path:
                # load the model detail path
                with open(file_path, 'r') as f:
                    details_data = json.load(f)
                    details = ModelDetails(**details_data)

            # load details into the func arguments (optional)
            kwargs['details'] = details

            result = func(*args, **kwargs)

            # capture model details **after** func is executed
            reporting.capture_model_details(details)

        return inner_func_wrapper

    return inner_wrapper
