from fastapi import APIRouter, Depends

from maxenzone.users.schemas import UserSchema
from maxenzone.auth import utils as auth_utils

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
    pass
