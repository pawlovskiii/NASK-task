from src.extractString import stripString


def extractDictValues(stringCPE):

    arrayForValuesToDict = []

    for i in stripString(stringCPE).split(":"):
        if i == "*":
            arrayForValuesToDict.append("ANY")
            continue
        arrayForValuesToDict.append(i)
    return arrayForValuesToDict
