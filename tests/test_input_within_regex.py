import pytest
import sys

# setting path
sys.path.append("../src")
from validationOfStringCPE import regExValidationOfStringCPE


def test_input_within_regex_error():

    listOfPossibleInputs = [
        "amicrosoft:internet_explorer:8.0.6001:beta:*:*:*:*:*:*",
        "amicrosoftinternet_explorer8.0.6001beta******",
        "a:microsoft:",
    ]

    for item in listOfPossibleInputs:
        with pytest.raises(ValueError):
            regExValidationOfStringCPE(item)


def test_input_within_regex_assert():

    listOfPossible = [
        "a:microsoft:internet_explorer:8.0.6001:foo-bar:*:*:*:*:*:*",
        "a:back\\-=slash_software:internet_explorer:8.0.6001:beta:*:*:*:*:*:*",
        "a:foo\-bar:internet_explorer:8.0.6001:beta:*:*:*:*:*:*",
        "a:*8\.??:internet_explorer:8.0.6001:beta:*:*:*:*:*:*",
        "a:*8\.??:foo\:bar:foo\:bar:foo\:bar:foo\:bar:foo\:bar:foo\:bar:foo\:bar:foo\:bar:foo\:bar",
        "a:*8\\.??:foo\\:bar:foo\\:bar:foo\\:bar:foo\\:bar:foo\\:bar:foo\\:bar:foo\\:bar:foo\\:bar:foo\\:bar",
    ]

    for item in listOfPossible:
        assert regExValidationOfStringCPE(item) == item
