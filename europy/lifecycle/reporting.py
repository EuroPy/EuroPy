import json
from typing import Union, List

from pandas import DataFrame


class TestResult:
    def __init__(self, key: str, description: str, result: Union[str, DataFrame]):
        self.key = key
        self.description = description
        self.result = result


# Global member
REPORTS: List[TestResult] = []


# Ideally descri
def capture(result: Union[str, DataFrame], key: str = "", description: str = ""):
    REPORTS.append(TestResult(description, key, result))


def flush():
    with open('test_output.json', 'w') as outfile:
        json.dump(REPORTS, outfile)
