import json
import urllib.request
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from typing import List
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import requests
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root(request: Request):
    return RedirectResponse(url="/login")

@app.get("/login")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/posts/", response_class=HTMLResponse)
async def read_posts(request: Request):
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
        response.raise_for_status()
        posts = response.json()
    except (requests.RequestException, ValueError) as e:
        return {"error": str(e)}

    return templates.TemplateResponse(
        "index1.html",
        {"request": request, "posts": posts}
    )

@app.get("/posts/{post_id}/comments")
async def get_post_comments(post_id: int) -> List[dict]:
    with urllib.request.urlopen(f"https://jsonplaceholder.typicode.com/comments?postId={post_id}") as response:
        data = response.read().decode()
        comments = json.loads(data)
        return comments