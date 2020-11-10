from typing import List, Union

import pytest
from _pytest.mark import Mark
from _pytest.python import Function
from pandas import DataFrame

from europy.lifecycle import reporting
from europy.lifecycle.test_result import TestLabel, TestResult
from europy.fixtures.report import report, test_result

@pytest.hookimpl()
def pytest_addoption(parser):
    # TODO: build report object
    pass


def pytest_configure(config):
    # build marks
    config.addinivalue_line(
        "markers",
        "report_bias: this is a marker for bias tests"
    )

    config.addinivalue_line(
        "markers",
        "report_accurarcy: this is a marker for bias tests"
    )

    config.addinivalue_line(
        "markers",
        "report_performance: this is a marker for bias tests"
    )

    print()


@pytest.hookimpl()
def pytest_terminal_summary(terminalreporter, exitstatus, config):
    reporting.flush()


@pytest.hookimpl(hookwrapper=True)
def pytest_pyfunc_call(pyfuncitem: Function):
    outcome = yield

    # Will raise an error if the outcome throws
    result: Union[str, bool, DataFrame, TestResult] = outcome.get_result()

    if isinstance(result, TestResult):
        reporting.capture(result.key, result.labels, result.result, result.description)
    else:
        node_id = pyfuncitem.nodeid
        marks: List[Mark] = pyfuncitem.own_markers
        labels: List[TestLabel] = [TestLabel.of(mark) for mark in marks]
        reporting.capture(node_id, labels, result, "")
