from sqlalchemy.orm import Mapped
from pydantic import EmailStr

from .base import Base


class PeopleTable(Base):

    first_mane: Mapped[str]
    last_mane: Mapped[str]
    phone_number: Mapped[str]
    email: Mapped[str]
