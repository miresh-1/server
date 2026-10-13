from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

computers = []


class Computer(BaseModel):
    mac: str
    name: str


@app.get("/")
def home():
    return {"message": "Сервер работает"}


@app.post("/register")
def register(computer: Computer):
    computers.append(computer.model_dump())
    return {"message": "Компьютер зарегистрирован"}


@app.get("/computers")
def get_computers():
    return computers
