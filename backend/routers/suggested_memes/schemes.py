from pydantic import BaseModel


class SuggestMeme(BaseModel):
    title: str
    image_url: str
    author_name: str


class ApproveSuggestedMeme(BaseModel):
    id: int
    app_token: str


class RejectSuggestedMeme(BaseModel):
    id: int
    app_token: str


class GetSuggestedMemes(BaseModel):
    app_token: str
