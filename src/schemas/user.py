"""Pydantic schemas for User."""

import datetime as dt

from pydantic import BaseModel


class UserBase(BaseModel):  # NOQA
    email: str
    role: int


class UserCreate(UserBase):  # NOQA
    pass


class User(UserBase):  # NOQA
    id: int
    is_active: bool
    created_at: dt.datetime
    updated_at: dt.datetime

    class Config:  # NOQA
        orm_mode = True
