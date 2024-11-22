from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models.db import db_helper
from . import crud
from .schemas import User, UserBase
from ..Post.schemas import PostBase, Post
from ..Post import crud as pcrud

router = APIRouter(tags=["Users"])


@router.get("/", response_model=list[User])
async def get_users(
        session: AsyncSession = Depends(db_helper.get_scoped_session)
):
    return await crud.get_users(session)


@router.get("/{username}/", response_model=User)
async def get_user_by_name(
        username: str,
        session: AsyncSession = Depends(db_helper.get_scoped_session)
):
    return await crud.get_user_by_name(session, username)


@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(
        user_create: UserBase,
        session: AsyncSession = Depends(db_helper.get_scoped_session)
) -> User:
    return await crud.create_user(session, user_create)


@router.post("/post")
async def create_post_by_user(
        post: PostBase,
        session: AsyncSession = Depends(db_helper.get_scoped_session)
) -> Post:
    return await pcrud.CreatePost(post, session)
