from sqlalchemy import Column, ForeignKey, Table, Integer, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base
from .meme import Meme
from .tag import Tag

# frozen


class MemeTagAssociation(Base):
    __tablename__ = "meme_tag_association"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    meme_id: Mapped[int] = mapped_column(ForeignKey("memes.id"))
    tag_id: Mapped[int] = mapped_column(ForeignKey("tags.id"))
