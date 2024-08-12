from contextlib import asynccontextmanager
from typing import Annotated, Optional

from fastapi import FastAPI, Depends
from pydantic import BaseModel

from database_01 import delete_tables, create_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("База очищена")
    await create_tables()
    print("База готова")
    yield
    print("Выключение")


app = FastAPI(lifespan=lifespan)


class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None


class STask(STaskAdd):
    id: int


tasks = []


@app.post("/tasks")
async def add_task(
    task: Annotated[STaskAdd, Depends()],
):
    tasks.append(task)
    return {"message": "Task created successfully", "task": task}


# @app.get("/tasks")
# def get_tasks():
#     task = STaskAdd(
#         name="Task",
#         description="Task description",
#     )
#     return {"message": "Welcome to the home page", "task": task}
