import re


def validationOfStringCPE(stringCPE: str) -> str:
    if not isinstance(stringCPE, str):
        raise TypeError("Wrong type! Input must be a string.")
    if not stringCPE.startswith("cpe:2.3"):
        raise ValueError("Incorrect beginning of a string CPE 2.3 It must starts with 'cpe:2.3'")
    return stringCPE


def regExValidationOfStringCPE(strippedStringCPE: str) -> str:
    regex = "^[a-z]:[a-z]+:[a-z, _]+:[0-9, .]+:[a-z]+:[a-z, *]+:[a-z, *]+:[a-z, *]+:[a-z, *]+:[a-z, *]+:[a-z, *]+$"
    if not re.search(regex, strippedStringCPE):
        raise ValueError("Invalid string CPE 2.3")
    return strippedStringCPE
