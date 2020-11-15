from functools import wraps
from typing import Union, List
import os

from pandas import DataFrame

from europy.lifecycle import reporting
from europy.lifecycle.result import TestLabel, TestResult
from europy.lifecycle.modeldetails import ModelDetails


def decorator_factory(labels: List[Union[str, TestLabel]],
                      name: str = "",
                      description: str = ""):
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

    return decorator_factory(labels, name, description)


def bias(name: str = "",
         description: str = ""):
    labels: List[Union[str, TestLabel]] = [TestLabel.BIAS]

    return decorator_factory(labels, name, description)


def data_bias(name: str = "",
              description: str = ""):
    labels: List[Union[str, TestLabel]] = [TestLabel.DATA_BIAS]

    return decorator_factory(labels, name, description)


def fairness(name: str = "",
             description: str = ""):
    labels: List[Union[str, TestLabel]] = [TestLabel.FAIRNESS]

    return decorator_factory(labels, name, description)


def accuracy(name: str = "",
             description: str = ""):
    labels: List[Union[str, TestLabel]] = [TestLabel.ACCURACY]

    return decorator_factory(labels, name, description)


def unit(name: str = "",
         description: str = ""):
    labels: List[Union[str, TestLabel]] = [TestLabel.UNIT]

    return decorator_factory(labels, name, description)


def integration(name: str = "",
                description: str = ""):
    labels: List[Union[str, TestLabel]] = [TestLabel.INTEGRATION]

    return decorator_factory(labels, name, description)


def minimum_functionality(name: str = "",
                          description: str = ""):
    labels: List[Union[str, TestLabel]] = [TestLabel.MINIMUM_FUNCTIONALITY]

    return decorator_factory(labels, name, description)


def modeldetails(file_path: str = None):
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
            reporting.capture_modeldetails(details)

        return inner_func_wrapper

    return inner_wrapper



