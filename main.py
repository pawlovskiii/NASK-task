from src.data import listOfKeysOfDict, stringCPE
from src.mergeArrays import mergeArraysToDict
from src.extractValuesOfDict import extractDictValues
from src.writingJsonFile import writingJson


def main() -> None:

    dictCPE = mergeArraysToDict(listOfKeysOfDict, extractDictValues(stringCPE))
    writingJson(dictCPE)

    print(dictCPE)


main()


if __name__ == "__main__":
    main()
