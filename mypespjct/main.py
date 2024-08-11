from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn
from core.models import Base, db_helper
from users.veiws import router as users_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    async with db_helper.engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)
    yield
    # Clean up the ML models and release the resources


app = FastAPI(lifespan=lifespan)
app.include_router(users_router)


@app.get("/")
async def read_root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
