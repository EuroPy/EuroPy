#!/usr/bin/env python
# coding: utf-8



from europy.lifecycle.reporting import report_model_params, report_model_details


# In[3]:


from europy.decorator import bias, fairness
from europy.lifecycle.reporting import execute_tests, generate_report

@bias("My example bias test", "Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
def foo(input):
    assert input % 2 == 0
    return input

@fairness("My example fairness test that fails")
@bias()
def foo_failure(input):
    assert input % 2 == 1
    return input

@bias("example_figure")
def save_image_example(plots: dict):
    import matplotlib.pyplot as plt
    import numpy as np

    plt.style.use('fivethirtyeight')

    x = np.linspace(0, 10)

    # Fixing random state for reproducibility
    np.random.seed(19680801)

    fig, ax = plt.subplots()

    ax.plot(x, np.sin(x) + x + np.random.randn(50))
    ax.plot(x, np.sin(x) + 0.5 * x + np.random.randn(50))
    ax.plot(x, np.sin(x) + 2 * x + np.random.randn(50))
    ax.plot(x, np.sin(x) - 0.5 * x + np.random.randn(50))
    ax.plot(x, np.sin(x) - 2 * x + np.random.randn(50))
    ax.plot(x, np.sin(x) + np.random.randn(50))
    ax.set_title("'fivethirtyeight' style sheet")

    plots['fivethirtyeight fig'] = plt


report_model_params('tests/param_example.yml')
report_model_details('tests/model_details_example.yml')
execute_tests(clear=True, input=1)
generate_report(export_type='markdown', clear_report=True)


# In[ ]:





# In[ ]:




