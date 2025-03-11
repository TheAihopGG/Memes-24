import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI
from models import (
    Base,
    engine,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as session:
        await session.run_sync(Base.metadata.create_all)
        await session.commit()

    yield


app = FastAPI(lifespan=lifespan)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        reload=True,
    )
