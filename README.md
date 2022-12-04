# Parser Formatted String Binding for CPE 2.3

## Table of contents

- [General info](#general-info)
- [Setup](#setup)
  - [Installing dependencies](#installing-dependencies)
  - [Recommended commands to use for the project](#recommended-commands-to-use-for-the-project)

## General info

The task is about writing your parser Formatted String Binding for CPE 2.3. The key thing about the project is the correctness of the inputted string CPE. I firmly focused on various validations including regex to test them within unit tests nextly. Moreover, even if the user provides an invalid string CPE, the error messages explain where exactly the problem lies and how the sample valid input looks.

In the case of launching an application through the terminal, the user will be provided with two choices.

1. Write his own string CPE 2.3
2. Use sample string CPE 2.3

The result will be visible in two places:

1. Terminal
2. DictCPE.json

Additional JSON file with proper indents is for increased readability purpose, which the terminal doesn't provide. It'll create after the execution of the main function.

```python
# Sample input
stringCPE = cpe:2.3:a:microsoft:internet_explorer:8.0.6001:beta:*:*:*:*:*:*

# Desired output
output = {
           "part": "a",
           "vendor": "microsoft",
           "product": "internet_explorer",
           "version": "8.0.6001",
           "update": "beta",
           "edition": "ANY",
           "language": "ANY",
           "sw_edition": "ANY",
           "target_sw": "ANY",
           "target_hw": "ANY",
           "other": "ANY"
}
```

## Setup

These are the crucial steps to configuring and running the project. To clone and run this application, you'll need [Git](https://git-scm.com) and [Python](https://www.python.org/downloads/) (which comes with [pip](https://pypi.org/project/pip/)) installed on your computer.

```bash
# Clone this repository
$ git clone https://github.com/pawlovskiii/NASK-task

# Go into the repository
$ cd NASK-task
```

### Installing dependencies

```bash
# To download all the necessary Python packages needed for the project
$ pip install -r requirements.txt
```

### Recommended commands to use for the project

To run the project

```bash
$ python .\main.py
```

To run the tests within pytest

```bash
$ cd tests

$ pytest
```
