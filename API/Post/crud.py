from .schemas import PostBase
from core.models import Post
from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession


async def CreatePost(create_post: PostBase, session: AsyncSession) -> Post:
    post = Post(**create_post.model_dump())
    session.add(post)
    await session.commit()
    return post


async def GetPostsByUser(session: AsyncSession, username: str) -> list[Post]:
    query = select(Post).where(Post.author == username)
    result: Result = await session.execute(query)
    posts = result.scalars().all()
    return list(posts)


