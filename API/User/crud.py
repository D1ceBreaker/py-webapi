from typing import Optional

from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import UserBase
from core.models import User


async def get_users(session: AsyncSession) -> list[User]:
    stmt = select(User).order_by(User.username)
    result: Result = await session.execute(stmt)
    users = result.scalars().all()
    return list(users)


async def get_user_by_name(session: AsyncSession, name: str) -> Optional[User]:
    query = select(User).where(User.username == name)
    result: Result = await session.execute(query)
    return result.scalar_one_or_none()



async def create_user(session: AsyncSession, user_create: UserBase) -> User:
    user = User(**user_create.model_dump())
    try:
        session.add(user)
        await session.commit()
    except Exception:
        raise Exception("The username is not unique")
    return user
