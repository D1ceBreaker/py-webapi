from pydantic import BaseModel, ConfigDict


class PostBase(BaseModel):
    author: str
    content: str | None = None
    title: str


class Post(PostBase):
    model_config = ConfigDict(from_attributes=True)
