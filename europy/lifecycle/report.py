import json
from typing import Union

from pandas import DataFrame

from europy.lifecycle.test_result import TestResult, TestLabel


class Encoder(json.JSONEncoder):
    def default(self, obj: Union[TestLabel, DataFrame]):
        if isinstance(obj, TestLabel):
            return {"__enum__": str(obj)}
        if isinstance(obj, DataFrame):
            return obj.to_dict()
        if isinstance(obj, Report):
            return obj.__dict__
        if isinstance(obj, TestResult):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)


class Report:
    def __init__(self, title: str = "EuroPy Test Report"):
        self.test_results: dict = dict()
        self.title = title

    def to_dictionaries(self):
        return json.dumps(self, cls=Encoder)

    def capture(self, test_result: TestResult):
        self.test_results[test_result.key] = test_result
