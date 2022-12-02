def listOfValuesToOutputDictCPE(regExValidation: str) -> list:
    return ["ANY" if i == "*" else i for i in regExValidation.split(":")]
