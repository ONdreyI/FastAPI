from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class Order(Base):

    promocode: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        default=datetime.now,  # вызов без скобок позволит вызвать сразу
    )
