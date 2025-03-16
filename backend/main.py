import uvicorn
from routers import api_v1
from contextlib import asynccontextmanager
from fastapi import FastAPI
from core import (
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

app.include_router(api_v1.router)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        reload=True,
    )
