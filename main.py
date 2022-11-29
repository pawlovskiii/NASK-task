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


a = [
    "part",
    "vendor",
    "product",
    "version",
    "update",
    "edition",
    "language",
    "sw_edition",
    "target_sw",
    "target_hw",
    "other",
]


def mergeArraysToDict(keys, values):
    return dict(zip(keys, values))


print(mergeArraysToDict(a, extractDictValues("cpe:2.3:a:microsoft:internet_explorer:8.0.6001:beta:*:*:*:*:*:*")))
