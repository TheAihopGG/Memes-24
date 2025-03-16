import routers.tags.schemes as schemes
from crud import Tags
from core import settings
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from core import session_factory


router = APIRouter(prefix=settings.prefixes.tags)


@router.post("/create")
async def create_tag(query: schemes.CreateTag):
    if query.app_token == settings.app_token:
        async with session_factory() as session:
            await Tags.create(session, name=query.name)

        return JSONResponse({})

    else:
        return JSONResponse({}, status.HTTP_403_FORBIDDEN)


@router.get("/tag")
async def get_tag(query: schemes.GetTag):
    async with session_factory() as session:
        tag = await Tags.get(
            session,
            id=query.id,
            name=query.name,
        )

    if tag:
        return JSONResponse(
            {
                "id": tag.id,
                "name": tag.name,
            }
        )

    else:
        return JSONResponse({}, status.HTTP_403_FORBIDDEN)


@router.put("/update")
async def update_tag(query: schemes.UpdateTag):
    if query.app_token == settings.app_token:
        async with session_factory() as session:
            tag = await Tags.update(
                session,
                id=query.id,
                name=query.name,
            )

        if tag:
            return JSONResponse({})

        else:
            return JSONResponse({}, status.HTTP_404_NOT_FOUND)

    else:
        return JSONResponse({}, status.HTTP_403_FORBIDDEN)


@router.delete("/delete")
async def delete_tag(query: schemes.DeleteTag):
    if query.app_token == settings.app_token:
        async with session_factory() as session:
            tag = await Tags.delete(session, id=query.id)

        if tag:
            return JSONResponse({})

        else:
            return JSONResponse({}, status.HTTP_404_NOT_FOUND)

    else:
        return JSONResponse({}, status.HTTP_403_FORBIDDEN)
