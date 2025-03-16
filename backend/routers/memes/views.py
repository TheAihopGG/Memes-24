import routers.memes.schemes as schemes
from crud import Memes
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from core import session_factory, settings


router = APIRouter(prefix=settings.prefixes.memes)


@router.post("/create")
async def create_meme(query: schemes.CreateMeme) -> JSONResponse:
    if query.app_token == settings.app_token:
        async with session_factory() as session:
            result = await Memes.create(
                session,
                title=query.title,
                image_url=query.image_url,
                author_name=query.author_name,
            )

        if result:
            return JSONResponse({})

        else:
            return JSONResponse({}, status.HTTP_500_INTERNAL_SERVER_ERROR)

    else:
        return JSONResponse({}, status.HTTP_403_FORBIDDEN)


@router.get("/meme")
async def read_meme(query: schemes.ReadMeme) -> JSONResponse:
    async with session_factory() as session:
        meme = await Memes.read(session, query.id)

    if meme:
        return JSONResponse(
            {
                "id": meme.id,
                "title": meme.title,
                "image_url": meme.image_url,
                "author_name": meme.author_name,
                "created_at": meme.created_at.strftime("%Y-%m-%d %H:%M:%S.%f"),
                "updated_at": meme.updated_at.strftime("%Y-%m-%d %H:%M:%S.%f"),
            }
        )

    else:
        return JSONResponse({}, status.HTTP_404_NOT_FOUND)


@router.put("/update")
async def update_meme(query: schemes.UpdateMeme) -> JSONResponse:
    if query.app_token == settings.app_token:
        async with session_factory() as session:
            meme = await Memes.update(
                session,
                id=query.id,
                title=query.title,
                image_url=query.image_url,
                author_name=query.author_name,
            )

        if meme:
            return JSONResponse({})

        else:
            return JSONResponse({}, status.HTTP_404_NOT_FOUND)

    else:
        return JSONResponse({}, status.HTTP_403_FORBIDDEN)


@router.delete("/delete")
async def delete_meme(query: schemes.DeleteMeme) -> JSONResponse:
    if query.app_token == settings.app_token:
        async with session_factory() as session:
            meme = await Memes.delete(session, query.id)

        if meme:
            return JSONResponse({})

        else:
            return JSONResponse({}, status.HTTP_404_NOT_FOUND)

    else:
        return JSONResponse({}, status.HTTP_403_FORBIDDEN)
