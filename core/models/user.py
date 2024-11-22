from typing import TYPE_CHECKING

from .base import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String

if TYPE_CHECKING:
    from .post import Post
    from .comments import Comment


class User(Base):
    username: Mapped[str] = mapped_column(String(32), unique=True, primary_key=True)

    # relationship to connect Post -> User
    posts: Mapped[list["Post"]] = relationship("Post", back_populates="user")

    # relationship to connect Comment -> User
    user_comments: Mapped[list["Comment"]] = relationship("Comment", back_populates="author")

