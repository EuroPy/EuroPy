import json
from typing import Union, Optional
from datetime import datetime

from europy.lifecycle.markdowner import Markdown
from europy.lifecycle.model_details import ModelDetails
from europy.lifecycle.report_figure import ReportFigure

from pandas import DataFrame

from europy.lifecycle.result import TestResult, TestLabel


class Encoder(json.JSONEncoder):
    def default(self, obj: Union[TestLabel, DataFrame]):
        if isinstance(obj, TestLabel):
            return {"__enum__": str(obj)}
        if isinstance(obj, DataFrame):
            return obj.to_dict()
        if isinstance(obj, Report):
            return obj.__dict__
        if isinstance(obj, ModelDetails):
            return obj.__dict__
        if isinstance(obj, TestResult):
            return obj.__dict__
        if isinstance(obj, ReportFigure):
            return obj.__dict__
        if isinstance(obj, datetime):
            return str(obj)
        return json.JSONEncoder.default(self, obj)


class Report:
    def __init__(self, title: str = "EuroPy Test Report"):
        self.title = title
        self.test_results: dict = dict()
        self.model_card: dict = dict()
        self.figures: [ReportFigure] = []

        # TODO: make ModelCard class
        self.model_card['details'] = ModelDetails(title=title)
        self.model_card['parameters'] = {}

        self.timestamp = datetime.now()

    def to_markdown(self):
        markdownReport = Markdown()
        markdownReport.add_header(self.title)
        markdownReport.add_header('Model Information')
        markdownReport.add_dict_content(self.model_card['details'].__dict__)
        markdownReport.add_dict_content(self.model_card['parameters'])
        markdownReport.add_horizontal_line()
        markdownReport.add_header('Test Results')
        markdownReport.add_horizontal_line()
        markdownReport.add_dict_content(json.loads(json.dumps(self.test_results, cls=Encoder)))
        markdownReport.add_image('example_figure.png',
                                 'Stand Alone Figure')  # this is temp as images were getting generated separately
        markdownReport.add_image('transparency.png',
                                 'Stand Alone Figure')  # this is temp as images were getting generated separately
        markdownReport.saveToFile('result.md')

    def to_dictionaries(self, pretty: bool = False):
        indent = 4 if pretty else None
        return json.dumps(self, cls=Encoder, indent=indent)

    def capture(self, test_result: TestResult):
        self.test_results[test_result.key] = test_result
