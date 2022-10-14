"""Pydantic schemas for Course request body."""

import typing as tp

from pydantic import BaseModel


class CourseBase(BaseModel):  # NOQA
    title: str
    description: tp.Optional[str] = None
    user_id: int


class CourseCreate(CourseBase):  # NOQA
    pass


class Course(CourseBase):  # NOQA
    id: int

    class Config:  # NOQA
        orm_mode = True
