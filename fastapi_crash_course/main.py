from fastapi import FastAPI
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()


class STaskAdd(BaseModel):
    name: str
    description: str | None = None


class STask(STaskAdd):
    id: int


tasks = []


@app.post("/tasks")
async def add_task(
    task: STaskAdd,
):
    return {"ok": True}


# @app.get("/tasks")
# def get_tasks():
#     task = STaskAdd(name="Запиши это видео")
#     return {"data": task}
