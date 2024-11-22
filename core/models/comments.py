from datetime import datetime
from typing import TYPE_CHECKING

from .base import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, ForeignKey, func

if TYPE_CHECKING:
    from .user import User
    from .post import Post


class Comment(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(String(256))
    time: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        default=datetime.now(),
    )

    # relationship to connect Post -> Comment
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"))
    post: Mapped["Post"] = relationship(back_populates="post_comments")

    # relationship to connect User -> Comment
    user_id: Mapped[str] = mapped_column(ForeignKey("users.username"))
    author: Mapped["User"] = relationship(back_populates="user_comments")


