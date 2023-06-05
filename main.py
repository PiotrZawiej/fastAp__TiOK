import json
import urllib.request
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi import FastAPI
from typing import List
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.templating import _TemplateResponse

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root(request: Request):
    return RedirectResponse(url="/login")

@app.get("/login")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/posts")
async def get_posts(request: Request) -> _TemplateResponse:
    with urllib.request.urlopen(f"https://jsonplaceholder.typicode.com/posts") as response:
        data = response.read().decode()
        posts = json.loads(data)
        return templates.TemplateResponse("index1.html", {"request": request})

@app.get("/posts/{post_id}/comments")
async def get_post_comments(post_id: int) -> List[dict]:
    with urllib.request.urlopen(f"https://jsonplaceholder.typicode.com/comments?postId={post_id}") as response:
        data = response.read().decode()
        comments = json.loads(data)
        return comments