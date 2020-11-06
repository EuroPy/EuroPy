import pytest


def test_bias_marker(testdir):
    testdir.makepyfile(
        """
        import pytest

        @pytest.mark.bias_test
        def test_nothing():
            assert True
        """
    )

    result = testdir.runpytest('--strict-markers')
    result.assert_outcomes(passed=1)
