import json


def writingJsonFile(dictCPE: dict) -> None:
    json_object = json.dumps(dictCPE, indent=11)

    with open("DictCPE.json", "w") as outfile:
        outfile.write(json_object)
    
    print('DictCPE.json was successfully created!')