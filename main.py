from src.data import listOfKeysOfDict, stringCPE
from src.extractString import stripString
from src.mergeArrays import mergeArraysToDict


def extractDictValues(stringCPE):

    arrayForValuesToDict = []

    for i in stripString(stringCPE).split(":"):
        if i == "*":
            arrayForValuesToDict.append("ANY")
            continue
        arrayForValuesToDict.append(i)
    return arrayForValuesToDict


print(mergeArraysToDict(listOfKeysOfDict, extractDictValues(stringCPE)))
