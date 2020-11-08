from functools import wraps


def report_bias(description: str):
    def inner_bias_wrapper(func):
        @wraps(func)
        def bias_wrapper(*args, **kwargs):
            test = func(*args, **kwargs)
            print(test)
            return test

        return bias_wrapper

    return inner_bias_wrapper
