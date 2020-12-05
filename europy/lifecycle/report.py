import json
from typing import Union
from datetime import datetime

from europy.lifecycle.markdowner import Markdown
from europy.lifecycle.model_details import ModelDetails
from europy.lifecycle.model_card import ModelCard
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
        if isinstance(obj, ModelCard):
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
        self.model_card: ModelCard = ModelCard(ModelDetails(title=title))
        self.figures: [ReportFigure] = []

        self.timestamp = datetime.now()


    def to_markdown(self) -> Markdown:
        md = Markdown()
        md.add_header(f'{self.title}', 1)
        # md.add_horizontal_line()
        
        md += self.model_card.to_markdown()

        md.add_horizontal_line()

        md.add_header('Test Results', 2)
        for test_title, test in self.test_results.items():
            test_md = test.to_markdown()
            md += test_md
            md.add_horizontal_line()
        
        md.add_md_content("")
        return md

    def to_dictionaries(self, pretty: bool = False):
        indent = 4 if pretty else None
        return json.dumps(self, cls=Encoder, indent=indent)

    def capture(self, test_result: TestResult):
        self.test_results[test_result.key] = test_result
