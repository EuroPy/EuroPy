import os
from typing import Dict
from typing import List

from pandas import DataFrame

from europy import report_directory
from europy.lifecycle.model_details import ModelDetails
from europy.lifecycle.report import Report
from europy.lifecycle.result import TestResult
from europy.lifecycle.result_promise import TestPromise
from europy.utils import isnotebook

tests: dict = dict()

__report = Report()


def put_test(promise: TestPromise):
    key = str(promise.func.__name__)
    if key in tests.keys():
        current: TestPromise = tests[key]
        current.merge(promise)
        tests[key] = current
    else:
        tests[key] = promise


def capture_model_details(details: ModelDetails):
    __report.model_card['details'] = details


def capture_parameters(name: str, params: Dict):
    # combine parameters
    __report.model_card['parameters'][name] = {**__report.model_card['parameters'].get(name, {}), **params}


def make_report_dir():
    if not os.path.exists(report_directory):
        os.makedirs(report_directory)

    img_dir = os.path.join(report_directory, 'figures')
    if not os.path.exists(img_dir):
        os.makedirs(img_dir)


def execute_tests(*args, **kwargs):
    report = Report()
    make_report_dir()
    test_results: List[TestResult] = [tests[key].execute(*args, **kwargs) for key in tests.copy()]
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
    with open(file_path, 'w') as outfile:
        outfile.write(report.to_dictionaries(pretty=True))

    print("========= EuroPy Test Results =========")
    print(f"Total Tests: {len(test_results)}")
    print(f"Passing: {passing_count}")
    print(f"Failing: {failing_count}")

    return DataFrame(test_result_df) if isnotebook() else test_results
