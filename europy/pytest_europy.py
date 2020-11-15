from typing import List, Union

import pytest
from _pytest.mark import Mark
from _pytest.python import Function
from pandas import DataFrame

from europy.lifecycle import reporting
from europy.lifecycle.result import TestLabel, TestResult
from europy.fixtures.report import report, test_result
from europy.decorators import test

@pytest.hookimpl()
def pytest_addoption(parser):
    # TODO: build report object
    pass


def pytest_configure(config):
    # build marks
    config.addinivalue_line(
        "markers",
        "bias: this is a marker for bias tests"
    )

    config.addinivalue_line(
        "markers",
        "accurarcy: this is a marker for bias tests"
    )

    config.addinivalue_line(
        "markers",
        "performance: this is a marker for bias tests"
    )

    print()


@pytest.hookimpl()
def pytest_terminal_summary(terminalreporter, exitstatus, config):
    reporting.flush()


# @pytest.hookimpl(hookwrapper=True)
# def pytest_pyfunc_call(pyfuncitem: Function):
#     outcome = yield

#     # Will raise an error if the outcome throws
#     result: Union[float, str, bool, DataFrame, TestResult] = outcome.get_result()
#     marks: List[Mark] = pyfuncitem.own_markers
#     labels: List[TestLabel] = [TestLabel.of(mark) for mark in marks]

#     if isinstance(result, TestResult):
#         labels.extend(result.labels)
#         reporting.capture(result.key, labels, result.result, result.description)
#     else:
#         node_id = pyfuncitem.nodeid
#         reporting.capture(node_id, labels, result, "")
