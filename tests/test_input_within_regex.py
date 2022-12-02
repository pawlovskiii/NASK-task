import pytest
import sys

# setting path
sys.path.append("../src")
from validationOfStringCPE import regExValidationOfStringCPE


def test_input_within_regex():

    listOfPossibleInputs = [
        "a:microsoftinternet_explorer:8.0.6001:beta:*:*:*:*:*:*",
        "a:microsoft:internet_explorer:high:beta:*:*:*:*:*:*",
        "a:microsoft:internet_explorer:8.0.6001:55:*:*:*:*:*:*",
        "23:microsoft:internet_explorer:8.0.6001:beta:*:*:*:*:*:*",
        "a:123:internet_explorer:8.0.6001:beta:*:*:*:*:*:*"
    ]

    for item in listOfPossibleInputs:
        with pytest.raises(ValueError):
            regExValidationOfStringCPE(item)
