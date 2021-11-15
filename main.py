from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()

class Post(BaseModel):
    name: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [
    {
        "title": "Hello World",
        "content": "This is my first post",
        "id": 1
    },
    {
        "title": "Hello World 2",
        "content": "This is my second post",
        "id": 2
    }
]

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/posts")
async def get_posts():
    return {"data": my_posts}

@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict["id"] = randrange(0, 100000000)
    my_posts.append(post_dict)
    return {"data": post_dict}
