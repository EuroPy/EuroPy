import json
from typing import Union
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

    # Please help me with debugging if you have some time - else will take a look tomorrow
    # Also noticed when i run this call executes multiple tests and doesnt create m
    def to_markdown(self, report_directory):
        md = Markdown()
        md.add_header(f'{self.title}', 0)
        md.add_horizontal_line()
        
        md.add_header('Model Card', 2)
        md += self.model_card['details'].to_markdown()

        md.add_header('Parameters', 3)
        md.add_dict_content(self.model_card['parameters'])

        md.add_horizontal_line()

        md.add_header('Test Results', 2)
        
        

        # help me test this part - couldn't test and will be testing later
        # for result in self.test_results:
        #     if not isinstance(result, TestResult):
        #         md.add_linebreak()
        #         return self
        #     md.add_linebreak()
        #     md.add_md_content(result.to_markdown())
        # md.add_linebreak()
        # print(md.content)
        md.saveToFile(report_directory, 'result.md')

    # this one is old code works with image but will be removed once the new one works
    def to_markdown_old(self, report_directory):
        md = Markdown()
        md.add_header(self.title, 0)
        md.add_header('Model Information', 0)
        md.add_dict_content(self.model_card['details'].__dict__)
        md.add_dict_content(self.model_card['parameters'])
        md.add_horizontal_line()
        md.add_header('Test Results', 0)
        md.add_horizontal_line()
        md.add_dict_content(json.loads(json.dumps(self.test_results, cls=Encoder)))
        md.add_image_temp(report_directory + '/figures/transparency.png',
                                      'Transparency')  # this is temp as images were getting generated separately
        md.saveToFile(report_directory, 'result.md')

    def to_dictionaries(self, pretty: bool = False):
        indent = 4 if pretty else None
        return json.dumps(self, cls=Encoder, indent=indent)

    def capture(self, test_result: TestResult):
        self.test_results[test_result.key] = test_result
