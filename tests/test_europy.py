from pandas import DataFrame

from europy.decorators import bias, fairness, unit, minimum_functionality, integration, data_bias, test, \
    decorator_factory
from europy.lifecycle.result import TestLabel

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
