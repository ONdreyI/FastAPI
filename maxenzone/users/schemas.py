from typing import Annotated
from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, EmailStr, ConfigDict


class CreateUser(BaseModel):
    username: Annotated[str, MinLen(3), MaxLen(20)]
    email: EmailStr


class UserSchema(BaseModel):
    model_config = ConfigDict(
        strict=True
    )  # строго должны быть указаны те типы, которые мы сюда передали.
    username: str
    password: bytes
    email: EmailStr | None = None
    active: bool = True
