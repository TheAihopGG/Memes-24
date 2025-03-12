import asyncio
from datetime import datetime
from models import (
    Object,
    SuggestedObject,
)
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.engine import session_factory


class Objects:
    @staticmethod
    async def create(
        session: AsyncSession,
        title: str,
        image_url: str,
        author_name: str | None,
    ) -> Object:
        object = Object(
            title=title,
            image_url=image_url,
            author_name=author_name or "Unknown",
        )
        session.add(object)
        await session.commit()
        return object

    @staticmethod
    async def read(
        session: AsyncSession,
        id: int,
    ) -> Object | None:
        object = await session.get(
            Object,
            id,
        )
        return object

    @staticmethod
    async def update(
        session: AsyncSession,
        id: int,
        title: str | None = None,
        image_url: str | None = None,
        author_name: str | None = None,
    ) -> Object | None:
        object = await session.get(
            Object,
            id,
        )
        if object:
            object.title = title or object.title
            object.image_url = image_url or object.image_url
            object.author_name = author_name or object.author_name
            object.updated_at = datetime.now()
            await session.commit()

        return object

    @staticmethod
    async def delete(
        session: AsyncSession,
        id: int,
    ) -> Object | None:
        object = await session.get(
            Object,
            id,
        )
        if object:
            await session.delete(object)
            await session.commit()

        return object


class SuggestedObjects:
    @staticmethod
    async def read(
        session: AsyncSession,
        id: int,
    ) -> SuggestedObject | None:
        suggested_object = await session.get(
            SuggestedObject,
            id,
        )
        return suggested_object

    @staticmethod
    async def update(
        session: AsyncSession,
        id: int,
        title: str | None = None,
        image_url: str | None = None,
        author_name: str | None = None,
    ) -> SuggestedObject | None:
        suggested_object = await session.get(
            SuggestedObject,
            id,
        )
        if suggested_object:
            suggested_object.title = title or suggested_object.title
            suggested_object.image_url = image_url or suggested_object.image_url
            suggested_object.author_name = author_name or suggested_object.author_name
            suggested_object.updated_at = datetime.now()
            await session.commit()

        return suggested_object

    @staticmethod
    async def delete(
        session: AsyncSession,
        id: int,
    ) -> SuggestedObject | None:
        suggested_object = await session.get(
            SuggestedObject,
            id,
        )
        if suggested_object:
            await session.delete(suggested_object)
            await session.commit()

        return suggested_object

    @staticmethod
    async def create(
        session: AsyncSession,
        title: str,
        image_url: str,
        author_name: str | None,
    ) -> SuggestedObject:
        requested_object = SuggestedObject(
            title=title,
            image_url=image_url,
            author_name=author_name or "Unknown",
        )
        session.add(requested_object)
        await session.commit()
        return requested_object

    @staticmethod
    async def approve(
        session: AsyncSession,
        id: int,
    ) -> SuggestedObject | None:
        suggested_object = await SuggestedObjects.read(session, id)
        if suggested_object:
            await Objects.create(
                session,
                title=suggested_object.title,
                image_url=suggested_object.image_url,
                author_name=suggested_object.author_name,
            )
            await SuggestedObjects.delete(session, suggested_object.id)

        return suggested_object

    @staticmethod
    async def reject(
        session: AsyncSession,
        id: int,
    ) -> SuggestedObject | None:
        return await SuggestedObjects.delete(session, id)

    @staticmethod
    async def read_all(session: AsyncSession) -> list[SuggestedObject]:
        return await session.execute(select(SuggestedObject))


async def test_objects_crud(session: AsyncSession):
    await Objects.create(
        session,
        "Test1",
        "url",
        "Alex",
    )
    obj1 = await Objects.read(session, 1)
    print(obj1.title)
    await Objects.update(
        session,
        1,
        "Test2",
        "url2",
    )
    obj1 = await Objects.read(session, 1)
    print(obj1.title)
    await Objects.delete(session, 1)


async def test_requested_objects_crud(session: AsyncSession):
    await SuggestedObjects.create(
        session,
        "Test1",
        "url",
        "Alex",
    )
    await SuggestedObjects.create(
        session,
        "Test2",
        "url",
        "Alex",
    )
    # await RequestedObjects.approve(session, 1)
    # await RequestedObjects.reject(session, 2)


async def main():
    async with session_factory() as session:
        # await test_objects_crud(session)
        # await test_requested_objects_crud(session)
        pass


if __name__ == "__main__":
    asyncio.run(main())
