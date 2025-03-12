from data.config import settings
from fastapi import APIRouter


router = APIRouter(prefix=settings.prefixes.memes)
