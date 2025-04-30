from typing import Union

from fastapi import FastAPI, Request, Body, File, UploadFile, Form
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
    return templates.TemplateResponse("home.html",{
        "request": request, 
        "title": "TCO tool"
        })

@app.get("/tco-form")
async def name(request: Request):
    return templates.TemplateResponse("tco-tool.html",{
        "request": request, 
        "assignment" : "", 
        "title": "TCO tool"})

@app.post("/submitform")
# async means need to wait for the response
async def handle_form(request: Request, assignment: str = Form(...)):
    # assignment_file: UploadFile = File(...)
    # print(assignment)
    # print(assignment_file.filename)
    # content_assignment = await assignment_file.read()
    # print(content_assignment)
    return templates.TemplateResponse("tco-tool.html",{
        "request" : request, 
        "assignment" : assignment, 
        "title": "TCO tool"
        })

@app.get("/about")
async def name(request: Request):
    return templates.TemplateResponse("about.html",{"request": request, "title": "TCO tool"})

# def read_root():
#     return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return { "item_name": item.name,"item_price": item.price, "item_id": item_id}