from src.extractStringCPE import stripString


def extractDictValues(stringCPE: str) -> list:
    return ["ANY" if i == "*" else i for i in stripString(stringCPE).split(":")]
