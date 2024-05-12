from fastapi import FastAPI, HTTPException
from typing import List
from app.models import *
from app.database import Database
from bson import ObjectId

app = FastAPI()
db = Database()

@app.on_event("shutdown")
def shutdown_event():
    db.close_connection()

@app.post("/users/", response_model=User)
def create_user(user: User):
    db.users_collection.insert_one(user.dict())
    return user

@app.get("/users/", response_model=List[User])
def get_users():
    users = list(db.users_collection.find())
    return users

@app.post("/posts/", response_model=Post)
def create_post(post: Post):
    post_dict = post.dict()
    post_id = db.posts_collection.insert_one(post_dict).inserted_id
    return {**post_dict, "_id": str(post_id)}

@app.get("/posts/", response_model=List[Post])
def get_posts():
    return list(db.posts_collection.find())

@app.get("/posts/{post_id}", response_model=Post)
def get_single_post(post_id: str):
    post = db.posts_collection.find_one({"_id": ObjectId(post_id)})
    if post:
        return post
    else:
        raise HTTPException(status_code=404, detail="Post not found")


@app.post("/posts/{post_id}/comments/", response_model=Comment)
def add_comment_to_post(post_id: str, comment: Comment):

    post = db.posts_collection.find_one({"_id": ObjectId(post_id)})
    if post:
        comment_dict = comment.dict()
        db.posts_collection.update_one({"_id": ObjectId(post_id)}, {"$push": {"comments": comment_dict}})
        return comment
    else:
        raise HTTPException(status_code=404, detail="Post not found")
    

@app.put("/posts/{post_id}/like/")
def like_post(post_id: str):
    db.posts_collection.update_one({"_id": ObjectId(post_id)}, {"$inc": {"likes": 1}})
    return {"message": "Post liked successfully"}

@app.put("/posts/{post_id}/dislike/")
def dislike_post(post_id: str):
    db.posts_collection.update_one({"_id": ObjectId(post_id)}, {"$inc": {"dislikes": 1}})
    return {"message": "Post disliked successfully"}

@app.delete("/posts/{post_id}/", response_model=dict)
def delete_post(post_id: str):
    try:
        post = db.posts_collection.find_one({"_id": ObjectId(post_id)})
        if post:
            db.posts_collection.delete_one({"_id": ObjectId(post_id)})
            return {"message": "Post deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail="Post not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")