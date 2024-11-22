from typing import TYPE_CHECKING

from .base import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, ForeignKey, Text
from sqlalchemy import func
from datetime import datetime

if TYPE_CHECKING:
    from .comments import Comment


class Post(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str] = mapped_column(Text, default="", server_default="")
    title: Mapped[str] = mapped_column(nullable=False)
    time: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        default=datetime.now(),
    )

    # relationship to connect Post -> User
    author: Mapped[str] = mapped_column(ForeignKey("users.username"))
    user: Mapped[list["Post"]] = relationship("User", back_populates="posts")

    # relationship to connect Comment -> Post
    post_comments: Mapped[list["Comment"]] = relationship("Comment", back_populates="post")
