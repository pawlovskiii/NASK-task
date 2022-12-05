import pytest
import sys

# setting path
sys.path.append("../src")
from validationOfStringCPE import regExValidationOfStringCPE


def test_input_within_regex_error() -> None:

    listOfPossibleInputs = [
        "amicrosoft:internet_explorer:8.0.6001:beta:*:*:*:*:*:*",
        "a:microsoft:internet_explorer:8.0.6001:beta:*:*:*:*:*:*:65",
        "a:microsoft:internet_explorer:8.0.6001:beta:*:*:*:*:*:*:9\.?:foo\:bar",
        "amicrosoftinternet_explorer8.0.6001beta******",
        "a:microsoft:",
    ]

    for item in listOfPossibleInputs:
        with pytest.raises(ValueError):
            regExValidationOfStringCPE(item)


def test_input_within_regex_assert() -> None:

    listOfPossibleInputs = [
        "a:microsoft:internet_explorer:8.0.6001:foobar:*:*:*:*:*:*",
        "a:back\\-=slash_software:internet_explorer:8.0.6001:beta:*:*:*:*:*:*",
        "a:foo\-bar:internet_explorer:8.0.6001:beta:*:*:*:*:*:*",
        "a:*8\.??:internet_explorer:8.0.6001:beta:*:*:*:*:*:*",
        "a:microsoft:big\$money:8.0.6001:sr*:*:da:*:*:*:*",
        "a:g\+\+:g\+\+:8.0.6001:sr*:big\money:english:*:*:*:*",
        "a:g\+\+:g\+\+:8.0.6001:sr*:big\money:english:test:*:*:*", 
    ]

    for item in listOfPossibleInputs:
        assert regExValidationOfStringCPE(item) == item
