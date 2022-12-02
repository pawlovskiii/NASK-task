from src.data import listOfKeysToOutputDictCPE, stringCPE
from src.validationOfStringCPE import (
    validationOfInputType,
    validationOfTheBeginningOfTheString,
    regExValidationOfStringCPE,
)
from src.stripStringCPE import stripString
from src.mergeArraysToDict import mergeArraysToDict
from src.listOfValuesToOutputDictCPE import listOfValuesToOutputDictCPE
from src.writingJsonFile import writingJsonFile


def main() -> None:

    validatedInputType = validationOfInputType(stringCPE)
    validatedTheBeginningOfTheString = validationOfTheBeginningOfTheString(validatedInputType)

    strippedStringCPE = stripString(validatedTheBeginningOfTheString)
    regExValidation = regExValidationOfStringCPE(strippedStringCPE)

    dictCPE = mergeArraysToDict(listOfKeysToOutputDictCPE, listOfValuesToOutputDictCPE(regExValidation))
    writingJsonFile(dictCPE)

    print(dictCPE)


if __name__ == "__main__":
    main()
