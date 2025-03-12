import memes.views
from backend.data.config import settings
from fastapi import APIRouter


router = APIRouter(prefix=settings.prefixes.api)

router.include_router(memes.views.router)
