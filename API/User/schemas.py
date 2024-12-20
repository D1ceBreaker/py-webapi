from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    username: str


class User(UserBase):
    model_config = ConfigDict(from_attributes=True)


