from functools import wraps
from typing import Union, List
import os
import inspect

from pandas import DataFrame

from europy.lifecycle import reporting
from europy.lifecycle.result import TestLabel, TestResult
from europy.lifecycle.model_details import ModelDetails


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

def transparency(name: str="",
                 description: str = ""):
    labels: List[Union[str, TestLabel]] = [TestLabel.TRANSPARENCY]
    
    return decorator_factory(labels, name, description)

def accountability(name: str="",
                 description: str = ""):
    labels: List[Union[str, TestLabel]] = [TestLabel.ACCOUNTABILITY]
    
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



def model_details(file_path: str = None):
    """Adds a model details to the Report.

    Args:
        file_path (str, optional): Path to model details JSON file. Defaults to None.
    """
    def inner_wrapper(func):
        @wraps(func)
        def inner_func_wrapper(*args, **kwargs):
            import json, yaml
        
            # pull current report (generated @ __init__)
            details = reporting.get_report().model_card['details']
            
            if file_path:
                # load the model detail path
                with open(file_path, 'r') as f:
                    # load in yml or json format (to dict)
                    if os.path.split(file_path)[-1].split('.')[-1] in ["yml", "yaml"]:
                        details_data = yaml.load(f, Loader=yaml.FullLoader)
                    else: 
                        details_data = json.load(f)
                    
                    details = ModelDetails(**details_data)
                
            # load details into the func arguments (optional)
            kwargs['details'] = details
            
            result = func(*args, **kwargs)

            # capture model details **after** func is executed
            reporting.capture_model_details(details)

        return inner_func_wrapper

    return inner_wrapper


def using_params(file_path: str, report=True):
    """allows params for a function to be injected from a yaml or json file

    NOTE: parameters should be prefixed with function name,
    ```yaml
    a_func.param1 = 1.2
    a_different_func.param1 = 1.4
    global_param1 = 1e-6
    ```
    only parameters with a matching prefix will be used. this matches the implementation of gin.config.

    Args:
        file_path (str): relative path to the paramters file (.json, .yaml, or .yml)
        report (bool, optional): should include in model card report. Defaults to True.
    """
    def inner_wrapper(func):
        @wraps(func)
        def inner_func_wrapper(*args, **kwargs):
            import json, yaml
            
            func_name = func.__name__
            
            file_name = os.path.split(file_path)[0]
            func_spec = inspect.getfullargspec(func)
            if report:
                params = reporting.get_report().model_card['parameters'].get(func_name, {})
            else:
                param = False

            with open(file_path, 'r') as f:
                if os.path.split(file_path)[-1].split('.')[-1] in ['yml', 'yaml']:
                    params = yaml.load(f, Loader=yaml.FullLoader)
                else: 
                    params = json.load(f)
                
            for (key, value) in params.items():
                key_split = key.split('.')

                # global params
                if key in func_spec.args:
                    kwargs[key] = value
                
                # func specific params
                if key_split[0] == func_name and key_split[-1] in func_spec.args:
                    kwargs[key_split[-1]] = value
            
            result = func(*args, **kwargs)

            """ may want to name it something other than the function name
                maybe try to pull a key from the doc string first, or
                give a special key in yaml
            """
            if report:
                reporting.capture_parameters(func_name, kwargs)
                
        return inner_func_wrapper
    return inner_wrapper


