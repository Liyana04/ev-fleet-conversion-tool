from typing import Union

from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/")
async def name(request: Request):
    return templates.TemplateResponse("home.html",{"request": request, "title": "TCO tool"})

async def name(request: Request):
    return templates.TemplateResponse("form.html",{"request": request, "title": "TCO tool"})

# def read_root():
#     return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return { "item_name": item.name,"item_price": item.price, "item_id": item_id}