import pytest

from europy.lifecycle import reporting


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
    reporting.save_output()


@pytest.hookimpl(hookwrapper=True)
def pytest_pyfunc_call(pyfuncitem):
    # do_something_before_next_hook_executes()

    outcome = yield

    # Will raise an error if the outcome throws
    res = outcome.get_result()
    key = str(pyfuncitem)

    # TODO: We somehow should try to get the function name and description
    reporting.capture(res, key)
