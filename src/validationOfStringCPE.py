import re


def checkSpaceInStringCPE(takeInputFromUserOrUseSampleStringCPE):
    if " " in takeInputFromUserOrUseSampleStringCPE:
        raise ValueError("String CPE 2.3 cannot include whitespace. Please Try again.")
    return takeInputFromUserOrUseSampleStringCPE


def validationOfInputType(takeInputFromUserOrUseSampleStringCPE: str) -> str:
    if not isinstance(takeInputFromUserOrUseSampleStringCPE, str):
        raise TypeError("Wrong type! Input must be a string.")
    return takeInputFromUserOrUseSampleStringCPE


def validationOfTheBeginningOfTheString(takeInputFromUserOrUseSampleStringCPE: str) -> str:
    if not takeInputFromUserOrUseSampleStringCPE.startswith("cpe:2.3"):
        raise ValueError("Incorrect beginning of a string CPE 2.3 It must starts with 'cpe:2.3'")
    return takeInputFromUserOrUseSampleStringCPE


def regExValidationOfStringCPE(strippedStringCPE: str) -> str:
    regex = f"^[h, o, a, *]:[A-Z, a-z, _, *]+:[A-Z, a-z, _, *]+:[A-Z, 0-9, ., *]+:[0-9, A-Z, a-z, *]+:[0-9, A-Z, a-z, _, *]+:[0-9, A-Z, a-z, *]+:[0-9, A-Z, a-z, _, *]+:[0-9, A-Z, a-z, _, *]+:[0-9, A-Z, a-z, _, *]+:[0-9, A-Z, a-z, _, *]+$"
    if not re.search(regex, strippedStringCPE):
        raise ValueError("Invalid string CPE 2.3")
    return strippedStringCPE
