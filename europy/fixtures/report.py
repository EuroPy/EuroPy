import pytest

from europy.lifecycle.reporting import get_report
from europy.lifecycle.result import TestResult


@pytest.fixture()
def report():
    return get_report()


@pytest.fixture()
def test_result():
    return TestResult(None, None, None, None)
