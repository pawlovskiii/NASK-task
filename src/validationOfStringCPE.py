import re


def validationOfInputType(takeInputFromUserOrUseSampleStringCPE: str) -> str:
    if not isinstance(takeInputFromUserOrUseSampleStringCPE, str):
        raise TypeError("Wrong type! Input must be a string.")
    return takeInputFromUserOrUseSampleStringCPE


def validationOfTheBeginningOfTheString(takeInputFromUserOrUseSampleStringCPE: str) -> str:
    if not takeInputFromUserOrUseSampleStringCPE.startswith("cpe:2.3"):
        raise ValueError("Incorrect beginning of a string CPE 2.3 It must starts with 'cpe:2.3'")
    return takeInputFromUserOrUseSampleStringCPE


def regExValidationOfStringCPE(strippedStringCPE: str) -> str:
    regex = "^[a-z]:[a-z]+:[a-z, _]+:[0-9, .]+:[a-z]+:[a-z, *]+:[a-z, *]+:[a-z, *]+:[a-z, *]+:[a-z, *]+:[a-z, *]+$"
    if not re.search(regex, strippedStringCPE):
        raise ValueError("Invalid string CPE 2.3")
    return strippedStringCPE
