from pydantic import BaseModel


class CreateTag(BaseModel):
    name: str
    app_token: str


class GetTag(BaseModel):
    id: int


class UpdateTag(BaseModel):
    name: str
    app_token: str


class DeleteTag(BaseModel):
    id: int
    app_token: str
