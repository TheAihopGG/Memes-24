from pathlib import Path
from pydantic import BaseModel


BASE_DIR = Path(__file__).parent.parent


class DBSettings(BaseModel):
    path: str = BASE_DIR / "data" / "database.db"
    url: str = f"sqlite+aiosqlite:///{path}"
    echo: bool = True


class Settings(BaseModel):
    db: DBSettings = DBSettings()


settings = Settings()

__all__ = (settings,)
