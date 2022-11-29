import json


def writingJson(dictCPE):
    json_object = json.dumps(dictCPE, indent=11)

    with open("DictCPE.json", "w") as outfile:
        outfile.write(json_object)
