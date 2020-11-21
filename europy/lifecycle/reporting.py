from typing import Union, List, Dict
import os

from pandas import DataFrame

from europy.lifecycle.report import Report
from europy.lifecycle.result import TestResult, TestLabel
from europy.lifecycle.model_details import ModelDetails

report: Report = Report()
root_report_directory = '.europy/reports'


def get_report() -> Report:
    return report


def capture(key: str,
            labels: List[Union[str,TestLabel]],
            result: Union[float, str, bool, DataFrame, TestResult],
            description: str = "") -> TestResult:
    test_result = TestResult(key, labels, result, description)
    report.capture(test_result)
    return test_result

def capture_model_details(details: ModelDetails):
    report.model_card['details'] = details

def capture_parameters(name: str, params: Dict):
    report.model_card['parameters'][name] = params




def flush():

    date_str = report.timestamp.strftime('%d%m%Y_%H%M%S')
    title = report.title.replace(' ', '_') 
    report_directory = os.path.join(root_report_directory, f'{date_str}_{title}')
    
    if not os.path.exists(report_directory):
        os.makedirs(report_directory)

    
    file_name = f'report.json'
    file_path = os.path.join(report_directory, file_name)
    with open(file_path, 'w') as outfile:
        outfile.write(report.to_dictionaries(pretty=True))
