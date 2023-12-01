from fastapi import FastAPI
from fastapi.responses import HTMLResponse

import templates


app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def index():
    return templates.index()
