from typing import TYPE_CHECKING

from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .mixins import UserRelationMixin


if TYPE_CHECKING:
    from .user import User


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
