from src.data import listOfKeysToOutputDictCPE, stringCPE
from src.validationOfStringCPE import (
    validationOfInputType,
    validationOfTheBeginningOfTheString,
    regExValidationOfStringCPE,
)
from src.extractStringCPE import stripString
from src.mergeArrays import mergeArraysToDict
from src.extractValuesOfDict import extractDictValuesToList
from src.writingJsonFile import writingJsonFile


def main() -> None:

    validatedInputType = validationOfInputType(stringCPE)
    validatedTheBeginningOfTheString = validationOfTheBeginningOfTheString(validatedInputType)

    strippedStringCPE = stripString(validatedTheBeginningOfTheString)
    regExValidation = regExValidationOfStringCPE(strippedStringCPE)

    dictCPE = mergeArraysToDict(listOfKeysToOutputDictCPE, extractDictValuesToList(regExValidation))
    writingJsonFile(dictCPE)

    print(dictCPE)


if __name__ == "__main__":
    main()
