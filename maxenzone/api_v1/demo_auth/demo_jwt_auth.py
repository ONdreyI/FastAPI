from fastapi import APIRouter, Depends
from pydantic import BaseModel
from maxenzone.users.schemas import UserSchema
from maxenzone.auth import utils as auth_utils


class TokenInfo(BaseModel):
    access_token: str
    token_type: str


router = APIRouter(prefix="/jwt", tags=["JWT"])

john = UserSchema(
    username="john",
    password=auth_utils.hash_password("qwerty"),
    email="john@example.com",
)
sam = UserSchema(
    username="sam",
    password=auth_utils.hash_password("secret"),
)
users_db: dict[str, UserSchema] = {
    john.username: "john",
    sam.username: "sam",
}


def validate_auth_user_login():
    pass


@router.post("/login")
def auth_user_issue_jwt(
    user: UserSchema = Depends(validate_auth_user_login),
):
    jwt_payload = {
        "username": user.username,
        "email": user.email,
    }
    token = auth_utils.encode_jwt()
    return TokenInfo(
        access_token=token,
        token_type="Bearer",
    )
