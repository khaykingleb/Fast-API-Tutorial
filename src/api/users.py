"""Sections."""

import typing as tp

import fastapi
from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from .utils import users as users_utils
from ..db import async_get_db, get_db
from ..schemas.user import User, UserCreate

router = fastapi.APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post("/", response_model=User, status_code=201)
async def create_user(  # NOQA
    *,
    db: Session = Depends(get_db),
    user: UserCreate,
) -> User:
    db_user = users_utils.get_user_by_email(db, user.email)
    if db_user is not None:
        raise HTTPException(status_code=400, detail="Such email is already registered.")
    return users_utils.create_user(db, user)


@router.get("/", response_model=tp.List[User])
async def get_users(  # NOQA
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
) -> tp.List[User]:
    users = users_utils.get_users(db, skip, limit)
    return users


@router.get("/{id}", response_model=User)
async def get_user(*, db: AsyncSession = Depends(async_get_db), id: int) -> User:  # NOQA
    db_user = await users_utils.get_user(db, id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found.")
    return db_user
