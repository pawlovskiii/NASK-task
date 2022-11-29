from src.data import listOfKeysOfDict, stringCPE


def stripString(stringCPE):
    return stringCPE.strip("cpe:2.3")


def extractDictValues(stringCPE):

    arrayForValuesToDict = []

    for i in stripString(stringCPE).split(":"):
        if i == "*":
            arrayForValuesToDict.append("ANY")
            continue
        arrayForValuesToDict.append(i)
    return arrayForValuesToDict


def mergeArraysToDict(keys, values):
    return dict(zip(keys, values))


print(
    mergeArraysToDict(
        listOfKeysOfDict, extractDictValues(stringCPE)
    )
)
