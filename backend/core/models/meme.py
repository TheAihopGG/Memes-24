from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import func
from datetime import datetime
from .base import Base

if TYPE_CHECKING:
    from .tag import Tag
    from .meme_tag_association import MemeTagAssociation


class Meme(Base):
    __tablename__ = "memes"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(default="Untitled", server_default="Untitled")
    image: Mapped[bytes]
    author_name: Mapped[str] = mapped_column(
        default="Unknown", server_default="Unknown"
    )
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), default=datetime.now
    )
    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), default=datetime.now
    )
