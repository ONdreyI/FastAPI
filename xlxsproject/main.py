from typing import Annotated
from pydantic import (
    EmailStr,
    BaseModel,
)
import uvicorn

from fastapi import (
    FastAPI,
    UploadFile,
    File,
    Body,
)


class CreateUser(BaseModel):
    email: EmailStr


app = FastAPI(
    title="My fastapi app",
    description="This is my fastapi app",
    version="0.1.0",
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/users/")
async def create_user(user: CreateUser):
    return {
        "message": "success",
        "email": user.email,
    }


@app.post("/calck/add/")
async def add(a: int, b: int):
    return {
        "a": a,
        "b": b,
        "result": a + b,
    }


@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        reload=True,
    )
