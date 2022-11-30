# Parser Formatted String Binding for CPE 2.3

## Table of contents

- [General info](#general-info)
- [Setup](#setup)
  - [Run the project](#run-the-project)

## General info

The task is about writing own parser Formatted String Binding for CPE 2.3

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

The result will be visible in two places. The first one is the terminal. The second one is a JSON file, which will create after executing the main function. To see both results it's needed to run the project within the below command. Additional JSON file with proper indents is for increased readability purpose, which the terminal doesn't provide.

### Run the project

```python
python .\main.py
```
