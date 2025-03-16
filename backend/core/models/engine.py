from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
)
from core.config import settings


engine = create_async_engine(
    settings.db.url,
    echo=settings.db.echo,
)
session_factory = async_sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)
