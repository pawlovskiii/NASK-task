import pytest
import sys

# setting path
sys.path.append("../src")
from validationOfStringCPE import regExValidationOfStringCPE


def test_input_within_regex():

    listOfPossibleInputs = [
        "amicrosoft:internet_explorer:8.0.6001:beta:*:*:*:*:*:*",
        "amicrosoft:internet_explorer8.0.6001beta:*:*:*:*:*:*",
        "amicrosoftinternet_explorer8.0.6001beta******"
    ]

    for item in listOfPossibleInputs:
        with pytest.raises(ValueError):
            regExValidationOfStringCPE(item)
