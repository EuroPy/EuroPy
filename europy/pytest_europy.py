import pytest

def pytest_addoption(parser):
    parser.addini('europy', 'placeholder pytest.ini setting')

def pytest_configure(config):
    config.addinivalue_line(
        "markers", 
        "bias_test: this is a marker for bias tests"
    )