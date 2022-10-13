"""Sections."""

import typing as tp

import fastapi
from pydantic import BaseModel

router = fastapi.APIRouter(
    prefix="/users",
    tags=["users"],
)

users = []


class User(BaseModel):  # NOQA
    email: str
    is_active: bool
    bio: tp.Optional[str]


@router.post("/")
async def create_user(user: User):  # NOQA
    users.append(user)
    return "Success"


@router.get("/", response_model=tp.List[User])
async def get_users():  # NOQA
    return users


@router.get("/{id}")
async def get_user(id: int):  # NOQA
    return {"user": users[id]}
