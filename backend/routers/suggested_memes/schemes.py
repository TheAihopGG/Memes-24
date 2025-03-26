from pydantic import BaseModel


class SuggestMeme(BaseModel):
    title: str
    image_url: str
    author_name: str
    app_token: str


class ApproveSuggestedMeme(BaseModel):
    id: int
    remove_invalid_images_urls: bool
    app_token: str


class RejectSuggestedMeme(BaseModel):
    id: int
    app_token: str


class GetSuggestedMemes(BaseModel):
    app_token: str
