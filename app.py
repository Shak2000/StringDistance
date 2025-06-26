from fastapi import FastAPI
from fastapi.responses import FileResponse

from main import Pair

pair = Pair("", "")
app = FastAPI()


@app.get("/")
async def get_ui():
    return FileResponse("index.html")


@app.post("/enter")
async def enter(a, b):
    global pair
    pair = Pair(a, b)
    return pair.calc_distance()
