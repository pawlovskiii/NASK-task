import pytest
import sys

# setting path
sys.path.append("../src")
from validationOfStringCPE import regExValidationOfStringCPE


def test_input_within_whitespaces():

    listOfPossibleInputs = [
        " a:microsoftinternet_explorer:8.0.6001:beta:*:*:*:*:*:*",
        "a:microsoftinternet_explorer:8.0.6001:beta:*:*:*:*:*:* ",
        "a:microsoftinternet _ explorer:8.0.6001:beta:*:*:*:*:*:*",
        "a : microsoftinternet_explorer : 8.0.6001 : beta:*:*:*:*:*:*",
        "a:microsoftinternet_explorer:8.0.6001:beta: * : * : * : * : * : *"
    ]

    for item in listOfPossibleInputs:
        with pytest.raises(ValueError):
            regExValidationOfStringCPE(item)
