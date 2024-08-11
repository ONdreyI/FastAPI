"""
Create an engine
Create session factory
"""

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    async_scoped_session,
    AsyncSession,
)
from asyncio import current_task
from core.config import settings


class DatabaseHelper:
    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(
            url=url,
            echo=echo,
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,  # Это тот самый движок
            autoflush=False,  # подготовка к коммит
            autocommit=False,  #
            expire_on_commit=False,  # автоматическое удаление о текущих объектах из сессии
        )

    def get_scoped_session(self):
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task,
        )
        return session

    async def session_dependencies(self) -> AsyncSession:
        """
        Для создания сессии каждый раз, то есть при новом обращении в View
         мы инициализируем новую сессию
        :return: session
        """
        async with self.session_factory() as session:
            yield session
            await session.close()

    async def scoped_session_dependencies(self) -> AsyncSession:
        """
        Для работы с одной конкретной сессией
        :return: session
        """
        session = self.get_scoped_session()
        yield session
        await session.close()


db_helper = DatabaseHelper(
    url=settings.db.url,
    echo=settings.db.echo,
)
