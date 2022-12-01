from src.validationOfStringCPE import initialValidationOfStringCPE, regExValidationOfStringCPE


def stripString(stringCPE: str) -> str:
    validatedStringCPE = initialValidationOfStringCPE(stringCPE)
    strippedStringCPE = validatedStringCPE.strip("cpe:2.3")
    regExValidation = regExValidationOfStringCPE(strippedStringCPE)

    return regExValidation
