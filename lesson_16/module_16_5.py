from fastapi import FastAPI, Request, HTTPException, Path
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from fastapi.templating import Jinja2Templates
from typing import Annotated, List

app = FastAPI(swagger_ui_parameters={"tryltOutEnabled": True}, debug=True)

templates = Jinja2Templates(directory="templates")

class UserCreate(BaseModel):
    username: str
    age: int

class User(UserCreate):
    id: int = None

users: List[User] = [
    User(id=1, username='Urbanuser', age=35)
]

@app.get("/", response_class=HTMLResponse)
async def get_users(request: Request):
    return templates.TemplateResponse('users.html', {'request': request, 'users': users})


@app.get("/user/{user_id}", response_class=HTMLResponse)
async def get_users(user_id: int, request: Request):
    for u in users:
        if u.id == user_id:
            return templates.TemplateResponse('users.html', {'request': request, 'user': u})
    raise HTTPException(status_code=404, detail="User was not found")

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

