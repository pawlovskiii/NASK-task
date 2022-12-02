from src.data import listOfKeysToOutputDictCPE, stringCPE
from src.validationOfStringCPE import initialValidationOfStringCPE, regExValidationOfStringCPE
from src.extractStringCPE import stripString
from src.mergeArrays import mergeArraysToDict
from src.extractValuesOfDict import extractDictValuesToList
from src.writingJsonFile import writingJsonFile


def main() -> dict:

    validatedStringCPE = initialValidationOfStringCPE(stringCPE)
    strippedStringCPE = stripString(validatedStringCPE)
    regExValidation = regExValidationOfStringCPE(strippedStringCPE)

    dictCPE = mergeArraysToDict(listOfKeysToOutputDictCPE, extractDictValuesToList(regExValidation))
    writingJsonFile(dictCPE)

    return dictCPE


print(main())


if __name__ == "__main__":
    main()
