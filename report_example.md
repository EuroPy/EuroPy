# EuroPy Test Report

## Model Card

### Model Details


**Organization**: Open Source Org (NU)

**Authors**:

* Matthew Alvarez (matt@email.com)
* Jenny Lam (jenny@email.com)
* Sundar Rajar (sundar@email.com)
* Blaine Rothrock (blaine@email.com)


**Created Date**: 2020-11-15 10:20:56.836960

**Version**: 0.0.1

**Citation**: 
```
@inproceedings{reftoken, title={EuroPy Example Title}, author={Matthew Alvarez, Jenny Lam, Sundar Rajar, Blaine Rothrock}, booktitle={Proceedings of the conference on fairness, accountability, and transparency} }
```

**Model License**: Apache License Version 2.0

**Model URL**: http://sample.com

**Data License**: Apache License Version 2.0

**Data URL**: http://sampledata.com

**Description**:

some long description

### Parameters


* **global**
	* a_global_param: 1e-06
* **test_params**
	* op1: 4
	* op2: 3
	* text_example: some text
	* list_example: 
		* 1.2
		* 1.3
		* 1.4
		* 1.5

* **not_test_params**
	* title: something that is not included


___
## Test Results

### My custom label test




**Labels**: `my-custom-label`

**Results**: (Success: True)


|    |   odds |   evens |
|---:|-------:|--------:|
|  0 |      1 |       2 |
|  1 |      3 |       4 |
___
### Test with custom decorator




**Labels**: `my-custom-decorator-label`, `minimum-functionality`

**Results**: (Success: True)


|    |   odds |   evens |
|---:|-------:|--------:|
|  0 |      1 |       2 |
|  1 |      3 |       4 |
___
### Testing it out




**Labels**: `bias`

**Results**: (Success: True)


|    |   odds |   evens |
|---:|-------:|--------:|
|  0 |      1 |       2 |
|  1 |      3 |       4 |
___
### example data bias test




**Labels**: `data-bias`

**Results**: (Success: True)


|    |   odds |   evens |
|---:|-------:|--------:|
|  0 |      1 |       2 |
|  1 |      3 |       4 |
___
### Example Fairness Test




**Labels**: `fairness`

**Results**: (Success: True)

Its Fair!


___
### Example Transparency Test




**Labels**: `transparency`

**Results**: (Success: True)

It's easy to understand!

#### Figures


![transparency](figures/transparency.png)



___
### Example Accountability Test




**Labels**: `accountability`

**Results**: (Success: True)

expectations are defined!


___
### Example Unit Test




**Labels**: `unit`

**Results**: (Success: True)


___
### Example Integration Test




**Labels**: `integration`

**Results**: (Success: True)


___
### Example Minimum Functionality Test




**Labels**: `minimum-functionality`

**Results**: (Success: True)


___
### Example with multiple labels




**Labels**: `my-custom-label`, `bias`, `integration`, `minimum-functionality`, `fairness`, `unit`

**Results**: (Success: True)

Woah, what a fair unit test


___


