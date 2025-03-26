from typing import Annotated
import routers.suggested_memes.schemes as schemes  # type: ignore
from crud import SuggestedMemes  # type: ignore
from core import settings  # type: ignore
from fastapi import APIRouter, Depends, Request, status
from fastapi.responses import JSONResponse
from core import session_factory


router = APIRouter(prefix=settings.prefixes.suggested_memes)


@router.post("/suggest")
async def suggest_meme(query: schemes.SuggestMeme) -> JSONResponse:
    if query.app_token == settings.app_token:
        async with session_factory() as session:
            suggested_meme = await SuggestedMemes.create(
                session,
                title=query.title,
                image=bytes(query.image, "utf-8"),
                author_name=query.author_name,
            )

        if suggested_meme:
            return JSONResponse({})

        else:
            return JSONResponse({}, status.HTTP_500_INTERNAL_SERVER_ERROR)

    else:
        return JSONResponse({}, status.HTTP_403_FORBIDDEN)


@router.post("/approve")
async def approve_suggested_meme(query: schemes.ApproveSuggestedMeme) -> JSONResponse:
    if query.app_token == settings.app_token:
        async with session_factory() as session:
            suggested_meme = await SuggestedMemes.approve(session, query.id)

            if suggested_meme:
                return JSONResponse({})

            else:
                return JSONResponse({}, status.HTTP_404_NOT_FOUND)

    else:
        return JSONResponse({}, status.HTTP_403_FORBIDDEN)


@router.post("/reject")
async def reject_suggested_meme(query: schemes.RejectSuggestedMeme) -> JSONResponse:
    if query.app_token == settings.app_token:
        async with session_factory() as session:
            suggested_meme = await SuggestedMemes.reject(session, query.id)

        if suggested_meme:
            return JSONResponse({})

        else:
            return JSONResponse({}, status.HTTP_500_INTERNAL_SERVER_ERROR)

    else:
        return JSONResponse({}, status.HTTP_403_FORBIDDEN)


@router.get("/all")
async def get_suggested_memes(query: schemes.GetSuggestedMemes) -> JSONResponse:
    if query.app_token == settings.app_token:
        async with session_factory() as session:
            suggested_memes = [
                {
                    "id": suggested_meme.id,
                    "title": suggested_meme.title,
                    "image": suggested_meme.image,
                    "author_name": suggested_meme.author_name,
                    "created_at": suggested_meme.created_at.strftime(
                        "%Y-%m-%d %H:%M:%S.%f"
                    ),
                }
                for suggested_meme in (
                    column[0] for column in await SuggestedMemes.get_all(session)
                )
            ]

        return JSONResponse({"suggested_memes": suggested_memes})

    else:
        return JSONResponse({}, status.HTTP_403_FORBIDDEN)
