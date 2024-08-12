from fastapi_crash_course.database import new_session
from fastapi_crash_course.main import STaskAdd


class TaskRepository:
    @classmethod
    async def add_one(cls, task: STaskAdd):
        async with new_session() as session:
            task_dict = task.model_dump()

    @classmethod
    async def get_all(cls): ...
