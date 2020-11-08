import pytest

from europy.report import BasicReport


@pytest.fixture()
def basic_report():
    report = BasicReport("")
    return report
