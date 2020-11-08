from functools import wraps

from europy.lifecycle import reporting


def bias(description: str):
    def inner_bias_wrapper(func):
        @wraps(func)
        def bias_wrapper(*args, **kwargs):
            key = str(func)
            result = func(*args, **kwargs)
            reporting.capture(result, key, description)
            return result

        return bias_wrapper

    return inner_bias_wrapper
