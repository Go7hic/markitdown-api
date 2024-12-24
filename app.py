from fastapi import FastAPI, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request
import shutil
from markitdown import MarkItDown
from uuid import uuid4
import os

md = MarkItDown()

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/convert")
async def convert_markdown(file: UploadFile):
    unique_id = uuid4()
    # temp_dir = f"./temp/{unique_id}"
    temp_dir = f"./temp"
    os.makedirs(temp_dir, exist_ok=True, mode=0o777)    
    file_path = f"{temp_dir}/{file.filename}"
    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    result = md.convert(file_path)
    content = result.text_content

    shutil.rmtree(temp_dir)

    return {"result": content}
