import pytest

REPORTS = []


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
    # TODO: this should be where to build the report JSON object
    pass


@pytest.hookimpl(hookwrapper=True)
def pytest_pyfunc_call(pyfuncitem):
    # do_something_before_next_hook_executes()

    outcome = yield

    res = outcome.get_result()  # will raise if outcome was exception

    # TODO: maybe add to the report here
    print()
