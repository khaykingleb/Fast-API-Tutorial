"""Sections."""

import typing as tp

import fastapi
from pydantic import BaseModel

router = fastapi.APIRouter()

users = []


class User(BaseModel):  # NOQA
    email: str
    is_active: bool
    bio: tp.Optional[str]


@router.post("/users")
async def create_user(user: User):  # NOQA
    users.append(user)
    return "Success"


@router.get("/users", response_model=tp.List[User])
async def get_users():  # NOQA
    return users


@router.get("/users/{id}")
async def get_user(id: int):  # NOQA
    return {"user": users[id]}
