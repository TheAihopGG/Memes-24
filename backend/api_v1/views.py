import memes.views
from data.config import settings
from fastapi import APIRouter


router = APIRouter(prefix=settings.prefixes.api)

router.include_router(memes.views.router)
