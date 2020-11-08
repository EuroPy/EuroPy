import pytest

# def test_bias_marker(testdir):
#     testdir.makepyfile(
#         """
#         import pytest
#         import europy
#         from europy import *

#         @bias_test
#         def test_nothing():
#             assert True
#         """
#     )

#     result = testdir.runpytest('--strict-markers')
#     result.assert_outcomes(passed=1)

@pytest.mark.bias
def test_sample(basic_report):
    
    basic_report.status = True
    
    assert True