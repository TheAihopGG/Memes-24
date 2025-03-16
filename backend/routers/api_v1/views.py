from routers import (
    memes,
    suggested_memes,
    tags,
)
from core import settings
from fastapi import APIRouter


router = APIRouter(prefix=settings.prefixes.api)

router.include_router(memes.router)
router.include_router(suggested_memes.router)
router.include_router(tags.router)
