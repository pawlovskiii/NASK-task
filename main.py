from src.data import listOfKeysOfDict, stringCPE
from src.mergeArrays import mergeArraysToDict
from src.extractValuesOfDict import extractDictValues
from src.writingJsonFile import writingJson


def main() -> dict:

    dictCPE = mergeArraysToDict(listOfKeysOfDict, extractDictValues(stringCPE))
    writingJson(dictCPE)

    return dictCPE


print(main())


if __name__ == "__main__":
    main()
