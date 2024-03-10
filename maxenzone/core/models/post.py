from typing import TYPE_CHECKING

from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


if TYPE_CHECKING:
    from .user import User


class Post(Base):
    title: Mapped[str] = mapped_column(String(200), unique=False)
    body: Mapped[str] = mapped_column(
        Text,
        default="",  # исп. если создается новый экземпляр прямо в Алхимии
        server_default="",  # исп. если мы будем вносить новую запись со стороны сервера
    )

    user_id: Mapped[str] = mapped_column(
        ForeignKey("users.id"),
    )
    user: Mapped["User"] = relationship(back_populates="posts")
