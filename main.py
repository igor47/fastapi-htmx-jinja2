from fastapi import FastAPI, Header
from fastapi.responses import HTMLResponse

from typing import Annotated

import templates


app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def index():
    return templates.index(as_frag=False)


@app.get("/new", response_class=HTMLResponse)
async def new(hx_request: Annotated[bool, Header()] = False):
    print('hx_request', hx_request)
    return templates.new(as_frag=hx_request)
