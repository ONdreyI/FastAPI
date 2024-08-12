from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import FastAPI, Depends

from database import create_tables, delete_tables
from fastapi_crash_course.schemas import STaskAdd


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("База очищена")
    await create_tables()
    print("База готова к работе")

    yield

    print("Выключение!")


app = FastAPI(lifespan=lifespan)

tasks = []


@app.post("/tasks")
async def add_task(
    task: Annotated[STaskAdd, Depends()],
):
    tasks.append(task)
    return {"ok": True}


# @app.get("/tasks")
# def get_tasks():
#     task = STaskAdd(name="Запиши это видео")
#     return {"data": task}
