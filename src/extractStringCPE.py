from src.initialValidationOfStringCPE import validationOfStringCPE


def stripString(stringCPE: str) -> str:
    validatedStringCPE = validationOfStringCPE(stringCPE)
    return validatedStringCPE.strip("cpe:2.3")
