from src.data import listOfKeysToOutputDictCPE, stringCPE
from src.mergeArrays import mergeArraysToDict
from src.extractValuesOfDict import extractDictValuesToList
from src.writingJsonFile import writingJsonFile


def main() -> dict:

    dictCPE = mergeArraysToDict(listOfKeysToOutputDictCPE, extractDictValuesToList(stringCPE))
    writingJsonFile(dictCPE)

    return dictCPE


print(main())


if __name__ == "__main__":
    main()
