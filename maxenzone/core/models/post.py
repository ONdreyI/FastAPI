from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .mixins import UserRelationMixin


class Post(UserRelationMixin, Base):
    # _user_id_unique = False
    # _user_id_nullable = False
    _user_back_populates = "posts"

    title: Mapped[str] = mapped_column(String(200), unique=False)
    body: Mapped[str] = mapped_column(
        Text,
        default="",  # исп. если создается новый экземпляр прямо в Алхимии
        server_default="",  # исп. если мы будем вносить новую запись со стороны сервера
    )
