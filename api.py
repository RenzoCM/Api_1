from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Text, Optional
from datetime import datetime
app = FastAPI()

#postModel
class Post(BaseModel):
    id:Optional[str]
    title:str
    author:str
    content:Text
    created_At:datetime = datetime.now()
    published_At:Optional[datetime]
    published:bool = False


posts = [

]

@app.get("/")
def read_root():
    return{"welcome":"Hola puerk ;)"}

@app.get("/posts")
def get_posts():
    return posts

@app.post("/posts")
def save_posts(post:Post):
    posts.append(post)
    print(post.dict())
    return "recibido"

@app.get("/posts/{post_id}")
def get_post(post_id:str):
    for post in posts:
        print(post)
        if post.id == post_id:
            result = post
            return result
    raise HTTPException(status_code=404, detail= "Not Found")

@app.delete("/borrar_posts/{post_id}")
def delete_post(post_id:str):
    for index, post in enumerate(posts):
        if post.id == post_id:
            posts.remove(post)
            return "Borrado"
    raise HTTPException(status_code=404, detail= "Not Found")

@app.put("/posts/{post_id}")
def update_post(post_id:str, newpost:Post):
    for index, post in enumerate(posts):
        if post.id == post_id:
            post.author = newpost.author
            post.content = newpost.content
            post.title = newpost.title
            return post
    raise HTTPException(status_code=404, detail= "Not Found")
    ##uuid