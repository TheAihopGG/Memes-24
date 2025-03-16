import asyncio
from datetime import datetime
from core import (
    Meme,
    SuggestedMeme,
    Tag,
)
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from core import session_factory


class Memes:
    @staticmethod
    async def create(
        session: AsyncSession,
        image: bytes,
        author_name: str | None = None,
        title: str | None = None,
    ) -> Meme:
        meme = Meme(
            title=title,
            image=image,
            author_name=author_name,
        )
        session.add(meme)
        await session.commit()
        return meme

    @staticmethod
    async def read(
        session: AsyncSession,
        id: int,
    ) -> Meme | None:
        meme = await session.get(
            Meme,
            id,
        )
        return meme

    @staticmethod
    async def update(
        session: AsyncSession,
        id: int,
        title: str | None = None,
        image: bytes | None = None,
        author_name: str | None = None,
    ) -> Meme | None:
        meme = await session.get(
            Meme,
            id,
        )
        if meme:
            meme.title = title or meme.title
            meme.image = image or meme.image
            meme.author_name = author_name or meme.author_name
            meme.updated_at = datetime.now()
            await session.commit()

        return meme

    @staticmethod
    async def delete(
        session: AsyncSession,
        id: int,
    ) -> Meme | None:
        meme = await session.get(
            Meme,
            id,
        )
        if meme:
            await session.delete(meme)
            await session.commit()

        return meme


class SuggestedMemes:
    @staticmethod
    async def get(
        session: AsyncSession,
        id: int,
    ) -> SuggestedMeme | None:
        suggested_meme = await session.get(
            SuggestedMeme,
            id,
        )
        return suggested_meme

    @staticmethod
    async def update(
        session: AsyncSession,
        id: int,
        title: str | None = None,
        image_url: str | None = None,
        author_name: str | None = None,
    ) -> SuggestedMeme | None:
        suggested_meme = await session.get(
            SuggestedMeme,
            id,
        )
        if suggested_meme:
            suggested_meme.title = title or suggested_meme.title
            suggested_meme.image_url = image_url or suggested_meme.image_url
            suggested_meme.author_name = author_name or suggested_meme.author_name
            suggested_meme.updated_at = datetime.now()
            await session.commit()

        return suggested_meme

    @staticmethod
    async def delete(
        session: AsyncSession,
        id: int,
    ) -> SuggestedMeme | None:
        suggested_meme = await session.get(
            SuggestedMeme,
            id,
        )
        if suggested_meme:
            await session.delete(suggested_meme)
            await session.commit()

        return suggested_meme

    @staticmethod
    async def create(
        session: AsyncSession,
        title: str,
        image_url: str,
        author_name: str | None,
    ) -> SuggestedMeme:
        requested_meme = SuggestedMeme(
            title=title,
            image_url=image_url,
            author_name=author_name or "Unknown",
        )
        session.add(requested_meme)
        await session.commit()
        return requested_meme

    @staticmethod
    async def approve(
        session: AsyncSession,
        id: int,
    ) -> SuggestedMeme | None:
        suggested_meme = await SuggestedMemes.get(session, id)
        if suggested_meme:
            await Memes.create(
                session,
                title=suggested_meme.title,
                image_url=suggested_meme.image_url,
                author_name=suggested_meme.author_name,
            )
            await SuggestedMemes.delete(session, suggested_meme.id)

        return suggested_meme

    @staticmethod
    async def reject(
        session: AsyncSession,
        id: int,
    ) -> SuggestedMeme | None:
        return await SuggestedMemes.delete(session, id)

    @staticmethod
    async def get_all(session: AsyncSession) -> list[SuggestedMeme]:
        return await session.execute(select(SuggestedMeme))


class Tags:
    @staticmethod
    async def create(
        session: AsyncSession,
        name: str,
    ) -> Tag:
        tag = Tag(name=name)
        session.add(tag)
        await session.commit()
        return tag

    @staticmethod
    async def get(
        session: AsyncSession,
        id: int,
    ) -> Tag | None:
        tag = await session.get(
            Tag,
            id,
        )
        return tag

    @staticmethod
    async def update(
        session: AsyncSession,
        id: int,
        name: str | None = None,
    ) -> Tag | None:
        tag = await session.get(
            Tag,
            id,
        )
        if tag:
            tag.name = name or tag.name
            await session.commit()

        return tag

    @staticmethod
    async def delete(
        session: AsyncSession,
        id: str,
    ) -> Tag | None:
        tag = await session.get(
            Tag,
            id,
        )
        if tag:
            await session.delete(tag)
            await session.commit()

        return tag


async def create_memes(session: AsyncSession):
    await Memes.create(session, image=open("./photo.jpeg", "rb").read())
    await Memes.create(session, image=open("./photo.jpeg", "rb").read())
    await Memes.create(session, image=open("./photo.jpeg", "rb").read())


async def main():
    async with session_factory() as session:
        # await create_memes(session)
        pass


if __name__ == "__main__":
    asyncio.run(main())
