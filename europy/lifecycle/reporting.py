from typing import Union, List, Dict
import os
from typing import Union, List

from pandas import DataFrame

from matplotlib import pyplot

from europy import report_directory, root_report_directory
from europy.lifecycle.report import Report
from europy.lifecycle.model_details import ModelDetails
from europy.lifecycle.report_figure import ReportFigure
from europy.lifecycle.result import TestResult, TestLabel
from europy.lifecycle.result_promise import TestPromise

tests: dict = dict()

report=Report()

def put_test(promise: TestPromise):
    key = str(promise.func.__name__)
    if key in tests.keys():
        current: TestPromise = tests[key]
        current.merge(promise)
        tests[key] = current
    else:
        tests[key] = promise


def get_report() -> Report:
    return report


def capture(key: str,
            labels: List[Union[str, TestLabel]],
            result: Union[float, str, bool, DataFrame, TestResult],
            figures: [ReportFigure] = [],
            description: str = None,
            success: bool = None) -> TestResult:
    test_result = TestResult(key, labels, result, figures, description, success)
    report.capture(test_result)
    return test_result


def capture_model_details(details: ModelDetails):
    report.model_card['details'] = details

def capture_parameters(name: str, params: Dict):
    # combine parameters
    report.model_card['parameters'][name] = {**report.model_card['parameters'].get(name, {}), **params}

def capture_figure(name: str, plot: pyplot):
    metadata = ReportFigure.of(name, plot)
    
    report.figures.append(metadata)

def make_report_dir():
    if not os.path.exists(report_directory):
        os.makedirs(report_directory)
    
    img_dir = os.path.join(report_directory, 'figures')
    if not os.path.exists(img_dir):
        os.makedirs(img_dir)

make_report_dir()

def flush():
    file_name = f'report.json'
    file_path = os.path.join(report_directory, file_name)
    with open(file_path, 'w') as outfile:
        outfile.write(report.to_dictionaries(pretty=True))


def execute_tests(*args, **kwargs):
    test_results: List[TestResult] = [tests[key].execute(*args, **kwargs) for key in tests.copy()]
    test_result_df = DataFrame([x.__dict__ for x in test_results])

    passing_count = len(list(filter(lambda x: x.success, test_results)))
    failing_count = len(list(filter(lambda x: not x.success, test_results)))
    print("========= EuroPy Test Results =========")
    print(f"Total Tests: {len(test_results)}")
    print(f"Passing: {passing_count}")
    print(f"Failing: {failing_count}")

    return DataFrame(test_result_df)
