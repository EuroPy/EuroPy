import functools

import pytest


def deco(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@pytest.fixture
def x():
    return 0


@deco
def test_something(x):
    assert x == 0
