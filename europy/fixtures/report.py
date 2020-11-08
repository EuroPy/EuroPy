import pytest

from europy.pytest_europy import REPORTS
from europy.report import BasicReport


@pytest.fixture()
def basic_report():
    report = BasicReport("")
    REPORTS.append(report)
    return report
