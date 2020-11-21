from pandas import DataFrame

import europy
from europy.lifecycle.result import TestResult, TestLabel
from europy.lifecycle.report import Report

# TODO: Explicitly import each decorator in release
from europy.decorators import *

EXAMPLE_LABEL_NAME = "my-custom-label"


# This is how you make your own decorator for tests with a custom label or with a provided label
def custom_decorator(name: str = ""):
    labels = ["my-custom-decorator-label", TestLabel.MINIMUM_FUNCTIONALITY]
    return decorator_factory(labels, name)


df = DataFrame([[1, 2], [3, 4]], columns=['odds', 'evens'])


# This is how you can create your own labels on the fly
@test(EXAMPLE_LABEL_NAME, "My custom label test")
def test_custom_label():
    assert True
    return df


@custom_decorator("Test with custom decorator")
def test_custom_decorator():
    assert True
    return df


# This is an example on using raw decorators
@bias("Testing it out")
def test_sample_with_raw_decorator():
    assert True
    return df


@data_bias("example data bias test")
def test_data_bias():
    assert True
    return df


# This is an example on using raw decorators
@fairness("Example Fairness Test")
def test_fairness_example():
    assert True
    return "Its Fair!"


@transparency("Example Transparency Test")
def test_transparency_example():
    assert True
    return "It's easy to understand!"


@accountability("Example Accountability Test")
def test_accountability_example():
    assert True
    return "expectations are defined!"


# This is an example on using raw decorators
@unit("Example Unit Test")
def test_unit_example():
    assert True


# This is an example on using raw decorators
@integration("Example Integration Test")
def test_integration_example():
    assert True


# This is an example on using raw decorators
@minimum_functionality("Example Minimum Functionality Test")
def test_minimum_functionality_example():
    assert True


# This is an example on using raw decorators
@unit("Example with multiple labels")
@fairness()
@minimum_functionality()
@integration()
@bias()
@test(EXAMPLE_LABEL_NAME)
def test_multiple_labels():
    return "Woah, what a fair unit test"


@model_details('tests/model_details_example.json') # this will override the current details in the report
def test_model_details_json(details: ModelDetails=None):
    import json
    details.description += '... this is a computed description'

    with open('tests/model_details_example.json', 'r') as f:
        loaded_details = ModelDetails(**json.load(f))

        assert loaded_details.title == details.title
        assert loaded_details.description != details.description

@model_details('tests/model_details_example.yml')
def test_model_details_ymal(details: ModelDetails=None):
    import yaml
    details.description += '... this is computed yaml description'

    with open('tests/model_details_example.yml', 'r') as f:
        loaded_details = ModelDetails(**yaml.load(f, Loader=yaml.FullLoader))

        assert loaded_details.title == details.title
        assert loaded_details.description != details.description


# this must run in order to pass
@model_details() # this will load the latest in the report
def test_loaded_model_details(details: ModelDetails=None):
    assert '... this is computed yaml description' in details.description


@using_params('tests/param_example.yml')
def test_params(op1: int=None, op2: int=None, text_example: str=None, list_example: List[float]=[], a_global_param=None):
    assert op1 != None, "op1 should be populated from params"
    assert op2 != None, "op1 should be populated from params"
    assert text_example != None, "text_example should be populated from params"
    assert list_example != [], "list_example should be populated from params"
    assert a_global_param != None, "a_global_param should be populated from params"


@report_plt("example_figure")
def test_save_image():
    import matplotlib.pyplot as plt
    import numpy as np

    plt.style.use('fivethirtyeight')

    x = np.linspace(0, 10)

    # Fixing random state for reproducibility
    np.random.seed(19680801)

    fig, ax = plt.subplots()

    ax.plot(x, np.sin(x) + x + np.random.randn(50))
    ax.plot(x, np.sin(x) + 0.5 * x + np.random.randn(50))
    ax.plot(x, np.sin(x) + 2 * x + np.random.randn(50))
    ax.plot(x, np.sin(x) - 0.5 * x + np.random.randn(50))
    ax.plot(x, np.sin(x) - 2 * x + np.random.randn(50))
    ax.plot(x, np.sin(x) + np.random.randn(50))
    ax.set_title("'fivethirtyeight' style sheet")

    return plt