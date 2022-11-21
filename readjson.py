import json

f = open('data.json', encoding = "utf8")

data = json.load(f)

def Data():
    return data