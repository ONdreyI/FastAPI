from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class STaskAdd(BaseModel):
    name: str
    description: str | None = None


class STask(STaskAdd):
    id: int


@app.get("/tasks")
def get_tasks():
    task = STaskAdd(name="Запиши это видео")
    return {"data": task}
