from src.extractStringCPE import stripString


def extractDictValuesToList(stringCPE: str) -> list:
    return ["ANY" if i == "*" else i for i in stripString(stringCPE).split(":")]
