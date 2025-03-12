import memes.schemes as schemes
from crud import (
    Objects,
    SuggestedObjects,
)
from data.config import settings
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from models.engine import session_factory


router = APIRouter(prefix=settings.prefixes.memes)


@router.post("/create")
async def create_meme(query: schemes.CreateMeme) -> JSONResponse:
    if query.app_token == settings.app_token:
        async with session_factory() as session:
            result = await Objects.create(
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


@router.get("/read")
async def read_meme(query: schemes.ReadMeme) -> JSONResponse:
    async with session_factory() as session:
        meme = await Objects.read(session, query.id)

    if meme:
        return JSONResponse(
            {
                "id": meme.id,
                "title": meme.title,
                "image_url": meme.image_url,
                "author_name": meme.author_name,
                "created_at": meme.created_at,
                "updated_at": meme.updated_at,
            },
        )

    else:
        return JSONResponse({}, status.HTTP_404_NOT_FOUND)


@router.put("/update")
async def update_meme(query: schemes.UpdateMeme) -> JSONResponse:
    if query.app_token == settings.app_token:
        async with session_factory() as session:
            meme = await Objects.update(
                session,
                id=query.id,
                title=query.id,
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
            meme = await Objects.delete(session, query.id)

        if meme:
            return JSONResponse({})

        else:
            return JSONResponse({}, status.HTTP_404_NOT_FOUND)

    else:
        return JSONResponse({}, status.HTTP_403_FORBIDDEN)


@router.post("/suggest")
async def suggest_meme(query: schemes.SuggestMeme) -> JSONResponse:
    async with session_factory() as session:
        suggested_meme = await SuggestedObjects.create(
            session,
            title=query.title,
            image_url=query.image_url,
            author_name=query.author_name,
        )

    if suggested_meme:
        return JSONResponse({})

    else:
        return JSONResponse({}, status.HTTP_500_INTERNAL_SERVER_ERROR)


@router.post("/approve")
async def approve_suggested_meme(query: schemes.ApproveSuggestedMeme) -> JSONResponse:
    if query.app_token == settings.app_token:
        async with session_factory() as session:
            suggested_meme = await SuggestedObjects.approve(session, query.id)

        if suggested_meme:
            return JSONResponse({})

        else:
            return JSONResponse({}, status.HTTP_500_INTERNAL_SERVER_ERROR)

    else:
        return JSONResponse({}, status.HTTP_403_FORBIDDEN)


@router.post("/reject")
async def reject_suggested_meme(query: schemes.RejectSuggestedMeme) -> JSONResponse:
    if query.app_token == settings.app_token:
        async with session_factory() as session:
            suggested_meme = await SuggestedObjects.reject(session, query.id)

        if suggested_meme:
            return JSONResponse({})

        else:
            return JSONResponse({}, status.HTTP_500_INTERNAL_SERVER_ERROR)

    else:
        return JSONResponse({}, status.HTTP_403_FORBIDDEN)
