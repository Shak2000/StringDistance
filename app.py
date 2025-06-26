from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

from main import Pair


class StringPair(BaseModel):
    a: str
    b: str


pair = Pair("", "")
app = FastAPI()


@app.get("/")
async def get_ui():
    return FileResponse("index.html")


@app.post("/enter")
async def enter(strings: StringPair):
    global pair
    pair = Pair(strings.a, strings.b)
    return pair.calc_distance()
