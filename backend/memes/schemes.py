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
    title: str
    image_url: str
    author_name: str
    app_token: str


class DeleteMeme(BaseModel):
    id: int


class SuggestMeme(BaseModel):
    title: str
    image_url: str
    author_name: str


class ApproveSuggestedMeme(BaseModel):
    id: int


class RejectSuggestedMeme(BaseModel):
    id: int
