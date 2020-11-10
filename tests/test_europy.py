import pytest
from pandas import DataFrame

from europy.decorators import bias
from europy.lifecycle.report import Report


@pytest.mark.bias
def test_alter_report(report: Report):
    report.title = "My Example Test Title"


@bias("Testing it out")
def test_sample_with_raw_decorator(report):
    report.status = True
    df = DataFrame([[1, 2], [3, 4]], columns=['odds', 'evens'])

    assert True
    return df


@bias("Testing it out 2")
def test_sample_with_raw_decorator_2(report):
    report.status = True
    df = DataFrame([[1, 2], [1, 2]], columns=['ones', 'twos'])

    assert True
    return df
