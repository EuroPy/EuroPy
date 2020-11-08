import pytest
from pandas import DataFrame

from europy.decorators import bias
from europy.fixtures.report import basic_report


# def test_bias_marker(testdir):
#     testdir.makepyfile(
#         """
#         import pytest
#         import europy
#         from europy import *
#
#         @bias_test
#         def test_nothing():
#             assert True
#         """
#     )
#
#     result = testdir.runpytest('--strict-markers')
#     result.assert_outcomes(passed=1)


@pytest.mark.bias
def test_sample(basic_report: basic_report):
    basic_report.status = True

    assert True


@bias("Testing it out")
def test_sample_with_raw_decorator(basic_report: basic_report):
    basic_report.status = True
    df = DataFrame([[1, 2], [3, 4]], columns=['odds', 'evens'])

    assert True
    return df


@bias("Testing it out 2")
def test_sample_with_raw_decorator_2(basic_report: basic_report):
    basic_report.status = True
    df = DataFrame([[1, 2], [1, 2]], columns=['ones', 'twos'])

    assert True
    return df
