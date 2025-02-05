from fastapi import FastAPI, status, Body, HTTPException
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()

class UserCreate(BaseModel):
    username: str = Field(...,
                          min_length=5,
                          max_length=100,
                          description="Enter username",
                          example='UrbanUser')
    age: int = Field(...,
                     ge=18,
                     le=120,
                     description='Enter age',
                     example=24)

class User(UserCreate):
    id: int = None

users: List[User] = []

@app.get("/users", response_model=List[User])
def get_users():
    return users

@app.post("/users", response_model=User)
async def post_user(user: UserCreate):
    new_id = max((u.id for u in users), default=0) + 1

    new_user = User(id=new_id, username=user.username, age=user.age)
    users.append(new_user)
    return new_user

@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, user: UserCreate):
    for u in users:
        if u.id == user_id:
            u.username = user.username
            u.age = user.age
            return u
    raise HTTPException(status_code=404, detail="User was not found")

@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    for u in users:
        if u.id == user_id:
            users.remove(u)
            return u
    raise HTTPException(status_code=404, detail="User was not found")

