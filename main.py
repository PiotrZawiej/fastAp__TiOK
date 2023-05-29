import json
import urllib.request
from fastapi import FastAPI
from typing import List

app = FastAPI()

@app.get("/")
def read_root():
    return {"Aplication": "simple Fastapi aplication"}

@app.get("/posts")
async def get_posts() -> List[dict]:
    with urllib.request.urlopen(f"https://jsonplaceholder.typicode.com/posts") as response:
        data = response.read().decode()
        posts = json.loads(data)
        return posts[:10]

@app.get("/posts/{post_id}/comments")
async def get_post_comments(post_id: int) -> List[dict]:
    with urllib.request.urlopen(f"https://jsonplaceholder.typicode.com/comments?postId={post_id}") as response:
        data = response.read().decode()
        comments = json.loads(data)
        return comments
