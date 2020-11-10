import pytest
from pandas import DataFrame

from build.lib.europy.lifecycle.result import TestResult, TestLabel
from europy.decorators import bias
from europy.lifecycle.report import Report


# This is an example on how I can alter the report
@pytest.mark.bias
def test_alter_report(report: Report):
    report.title = "My Example Test Title"

@bias("Example with manipulating test result")
def test_manipulate_test_result(test_result: TestResult) -> TestResult:
    test_result.key = "A great test key"
    # This is how you can add onto the test labels if you want to
    # So this test will be marked as BIAS and FAIRNESS
    test_result.labels = [TestLabel.FAIRNESS]
    test_result.description = "An example on how I can manipulate a test programmatically"
    test_result.result = 0.956
    return test_result


@pytest.mark.bias
def test_alter_report():
    df = DataFrame([[1, 2], [3, 4]], columns=['odds', 'evens'])

    assert True
    return df


# This is an example on using raw decorators
@bias("Testing it out")
def test_sample_with_raw_decorator():
    df = DataFrame([[1, 2], [3, 4]], columns=['odds', 'evens'])

    assert True
    return df


@bias("Testing it out 2")
def test_sample_with_raw_decorator_2():
    df = DataFrame([[1, 2], [1, 2]], columns=['ones', 'twos'])

    assert True
    return df
