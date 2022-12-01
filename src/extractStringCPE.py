from src.initialValidationOfStringCPE import validationOfStringCPE, regExValidationOfStringCPE


def stripString(stringCPE: str) -> str:
    validatedStringCPE = validationOfStringCPE(stringCPE)
    strippedStringCPE = validatedStringCPE.strip("cpe:2.3")
    regExValidation = regExValidationOfStringCPE(strippedStringCPE)

    return regExValidation
