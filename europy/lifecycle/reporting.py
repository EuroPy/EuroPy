import os
import json, yaml
from datetime import datetime
from typing import Dict
from typing import List

from pandas import DataFrame

from europy.lifecycle.model_details import ModelDetails
from europy.lifecycle.report import Report
from europy.lifecycle.result import TestResult
from europy.lifecycle.result_promise import TestPromise
from europy.utils import isnotebook

__tests: dict = dict()
__report = Report()


def put_test(promise: TestPromise):
    key = str(promise.func.__name__)
    if key in __tests.keys():
        current: TestPromise = __tests[key]
        current.merge(promise)
        __tests[key] = current
    else:
        __tests[key] = promise


def clear_tests():
    keys = list(__tests.keys())
    for key in keys:
        del __tests[key]


def capture_model_details(details: ModelDetails):
    __report.model_card['details'] = details


def capture_parameters(name: str, params: Dict):
    # combine parameters
    __report.model_card['parameters'][name] = {**__report.model_card['parameters'].get(name, {}), **params}


def make_report_dir():
    root_report_directory = '.europy/reports'
    report_directory = os.path.join(root_report_directory, f'{datetime.now().strftime("%d%m%Y_%H%M%S")}')
    if not os.path.exists(report_directory):
        os.makedirs(report_directory)

    img_dir = os.path.join(report_directory, 'figures')
    if not os.path.exists(img_dir):
        os.makedirs(img_dir)
    return report_directory


def report_model_params(file_path: str):
    params = {}
    with open(file_path, 'r') as f:
        if os.path.split(file_path)[-1].split('.')[-1] in ['yml', 'yaml']:
            params = yaml.load(f, Loader=yaml.FullLoader)
        else:
            params = json.load(f)

    __report.model_card.parameters = params


def report_model_details(path: str):
    details = ModelDetails.of(path)
    __report.model_card.model_details = details

def execute_tests(clear: bool = False, *args, **kwargs):
    report = Report()
    report_directory = make_report_dir()
    test_results: List[TestResult] = [__tests[key].execute(report_directory, *args, **kwargs) for key in __tests.copy()]
    test_result_df = DataFrame([x.__dict__ for x in test_results])

    for result in test_results:
        report.capture(result)
        for figure in result.figures:
            report.figures.append(figure)

    ## TODO: The model card and params should come from some test results
    ## Then those should be combined into the report itself
    report.model_card = __report.model_card

    passing_count = len(list(filter(lambda x: x.success, test_results)))
    failing_count = len(list(filter(lambda x: not x.success, test_results)))

    file_name = f'report.json'
    file_path = os.path.join(report_directory, file_name)
    # this is new call
    md = report.to_markdown()
    md.save(report_directory, 'report.md')
    # this is old call
    # report.to_markdown_old(report_directory)
    with open(file_path, 'w') as outfile:
        outfile.write(report.to_dictionaries(pretty=True))

    print("========= EuroPy Test Results =========")
    # TODO: Replace this with the markdown file instead of JSON
    print(f"Report output: file://{os.environ['PWD']}/{report_directory}/report.json")
    print(f"Total Tests: {len(test_results)}")
    print(f"Passing: {passing_count}")
    print(f"Failing: {failing_count}")

    if clear:
        clear_tests()

    return DataFrame(test_result_df) if isnotebook() else test_results
