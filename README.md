# EuroPy

EuroPy is a declarative python testing framework designed for the machine learning (ML) pipeline. Inspired by other testing frameworks (such as JUnit and NUnit) EuroPy uses test decorators to register and execute tests.

EuroPy is designed to work within an Iron Python interactive environment (i.e. Jupyter Notebook) as well as within the typical python kernel. 

## Philosophy
TODO: Fill this in

## Usage

Creating a test function is accmplished by simply decorating any function with decorators from `europy.decorators`. This will register your test function with the EuroPy lifecycle. In order to execute all registered tests you simply need to execute the `europy.lifecycle.reporting.execute_tests` function. Any parameters passed to the `execute_tests` function will also be passed to all registered functions. 

```python
from europy.decorators import bias, fairness
from europy.lifecycle.reporting import execute_tests

@bias("My example bias test", "Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
def foo(input):
    assert input % 2 == 0
    return input

@fairness("My example fairness test that fails")
@bias()
def foo_failure(input): 
    assert input % 2 == 1
    return input


execute_tests(100)
```

### Example Notebook Output
![Notebook Output](./.img/notebook-output-1.png)

### Example Standard Output
![Standard Output](./.img/standard-output-1.png)


## Testing Report
TODO: Fill me in after this is incorporated

## Model Card

TODO: Help fill me in @blaine


## Test Decorators
EuroPy supports a number of test classes out of the box. These test classes have been created by surveying industry practitioners and creating a list of well known testing labels. When defining a testing function you may pass two optional parameters to any decorator: name and description. These parameters are used as metadata and will be included in the resulting test report. The supported labels are listed below. 
    
- `@bias()`
- `@data_bias()`
- `@fairness()`
- `@transparency()`
- `@accountability()`
- `@accuracy()`
- `@unit()`
- `@integration()`
- `@minimum_functionality()`

### Custom Test Decorators
While we believe these decorators should be comprehensive we have provided two ways in which you can add your own custom label to the test reports. For the examples below we will be adding a custom "end-to-end" testing label to our testing function. 

- Using the  generic `@test()` decorator you can provide a custom string label
    ```python
    from europy.decorators import test
    from europy.lifecycle.reporting import execute_tests

    EXAMPLE_LABEL_NAME = "end-to-end"

    @test(EXAMPLE_LABEL_NAME, "My custom label test")
    def foo(input):
        assert input % 2 == 0
        return input

    execute_tests(100)
    ```
- Defining your own test decorator using the decorator_factory
    ```python
    from europy.decorators import decorator_factory
    from europy.lifecycle.reporting import execute_tests

    def end_to_end(name: str = ""):
        # here you can add multiple labels if you wish
        labels = ["end-to-end"]
        return decorator_factory(labels, name)


    @end_to_end("Test with custom decorator")
    def foo(input):
        assert input % 2 == 0
        return input

    execute_tests(100)
    ```