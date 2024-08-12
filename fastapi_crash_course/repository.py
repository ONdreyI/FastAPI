from fastapi_crash_course.database import new_session, TaskOrm
from fastapi_crash_course.main import STaskAdd


class TaskRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd):
        async with new_session() as session:
            task_dict = data.model_dump()

            task = TaskOrm(**task_dict)

    @classmethod
    async def get_all(cls): ...
