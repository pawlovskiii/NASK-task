def validationOfStringCPE(stringCPE: str) -> str:
    if not isinstance(stringCPE, str):
        raise TypeError("Wrong type! Input must be a string.")
    if not stringCPE.startswith("cpe:2.3"):
        raise ValueError("Incorrect beginning of a string. It must starts with 'cpe:2.3'")
    return stringCPE