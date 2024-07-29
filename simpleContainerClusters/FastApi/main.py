from fastapi import FastAPI, HTTPException
import random
from pydantic import BaseModel


app = FastAPI()

class User(BaseModel):
    name : str
    username : str
    age : str

    
users = {}

@app.get("/")
def root():
    return "Welcome to Fastapi Youtube"

@app.post("/create-user")
def create_user(user : User):
    users[user.name] = user
    return {"user" : user}


@app.get("/users")
def get_users():
    return {"users" : users}
