from typing import Annotated

from fastapi import APIRouter, Depends

from fastapi_crash_course.schemas import STaskAdd
from fastapi_crash_course.repository import TaskRepository

router = APIRouter(
    prefix="/tasks",
)


@router.post("")
async def add_task(
    task: Annotated[STaskAdd, Depends()],
):
    task_id = await TaskRepository.add_one(task)
    return {
        "ok": True,
        "task_id": task_id,
    }


# @app.get("")
# def get_tasks():
#     task = STaskAdd(name="Запиши это видео")
#     return {"data": task}
