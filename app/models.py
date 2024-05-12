from pydantic import BaseModel
from typing import List

class User(BaseModel):
    username: str
    email: str

class Comment(BaseModel):
    text: str
    user: User

class Post(BaseModel):
    title: str
    content: str
    author: User
    comments: List[Comment] = []
    likes: int = 0
    dislikes: int = 0

class PostInDB(Post):
    _id: str
