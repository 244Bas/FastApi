from fastapi import FastAPI
from readjson import *

apidata = Data()

app = FastAPI()

@app.get("/dict/{word}")
async def print(word):
    cnt = 0
    description = ""
    for i in apidata:
        cnt = cnt + 1
        if i.get("word") == word:
            description = i["description"]
    return {"word" : word, "description" : description}
    
