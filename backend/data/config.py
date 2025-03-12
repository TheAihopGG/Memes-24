from pathlib import Path
from pydantic import BaseModel


BASE_DIR = Path(__file__).parent.parent


class DBSettings(BaseModel):
    path: str = BASE_DIR / "data" / "database.db"
    url: str = f"sqlite+aiosqlite:///{path}"
    echo: bool = True


class Prefixes(BaseModel):
    api: str = "/api"
    memes: str = "/memes"


class Settings(BaseModel):
    db: DBSettings = DBSettings()
    prefixes: Prefixes = Prefixes()
    app_token: str = "12345"


settings = Settings()

__all__ = (settings,)
