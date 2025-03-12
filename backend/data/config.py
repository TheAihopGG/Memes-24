from pathlib import Path
from pydantic import BaseModel


BASE_DIR = Path(__file__).parent.parent


class DBSettings(BaseModel):
    path = BASE_DIR / "data" / "database.db"
    url = f"sqlite+aiosqlite:///{path}"
    echo = True


class Prefixes(BaseModel):
    api = "/api"
    memes = "/memes"


class Settings(BaseModel):
    db = DBSettings()
    prefixes = Prefixes()


settings = Settings()

__all__ = (settings,)
