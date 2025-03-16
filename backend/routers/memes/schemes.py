from pydantic import BaseModel


class CreateMeme(BaseModel):
    title: str
    image_url: str
    author_name: str
    app_token: str


class ReadMeme(BaseModel):
    id: int


class UpdateMeme(BaseModel):
    id: int
    title: str | None = None
    image_url: str | None = None
    author_name: str | None = None
    app_token: str


class DeleteMeme(BaseModel):
    id: int
    app_token: str
