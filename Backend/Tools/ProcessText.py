import json


def ReadText():
    # with open("./Cache/cache.txt") as file:
    #     data = file.read()

    with open("./Backend/Config/SavedData.json", 'r') as f:
        out = json.load(f)

    return out