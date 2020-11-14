from typing import Union, List

from pandas import DataFrame

from europy.lifecycle.report import Report
from europy.lifecycle.result import TestResult, TestLabel

report: Report = Report()


def get_report() -> Report:
    return report


def capture(key: str,
            labels: List[Union[str,TestLabel]],
            result: Union[float, str, bool, DataFrame, TestResult],
            description: str = "") -> TestResult:
    test_result = TestResult(key, labels, result, description)
    report.capture(test_result)
    return test_result



def flush():
    with open('europy_output.json', 'w') as outfile:
        outfile.write(report.to_dictionaries())
