from datetime import datetime
from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from .base import Base


class SuggestedMeme(Base):
    __tablename__ = "suggested_memes"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(default="Untitled")
    image_url: Mapped[str]
    author_name: Mapped[str] = mapped_column(default="Unknown")
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), default=datetime.now
    )
