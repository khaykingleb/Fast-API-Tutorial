"""Courses."""

import typing as tp

import fastapi
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from .utils import courses as courses_utils
from ..db import get_db
from ..schemas.course import Course, CourseCreate

router = fastapi.APIRouter(
    prefix="/courses",
    tags=["Courses"],
)


@router.get("/", response_model=tp.List[Course])
async def get_courses(db: Session = Depends(get_db)):  # NOQA
    courses = courses_utils.get_courses(db)
    return courses


@router.post("/", response_model=Course)
async def create_course(*, db: Session = Depends(get_db), course: CourseCreate):  # NOQA
    return courses_utils.create_course(db, course)


@router.get("/{course_id}")
async def read_course(*, db: Session = Depends(get_db), id: int):  # NOQA
    db_course = courses_utils.get_course(db, id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found.")
    return db_course


@router.patch("/{course_id}")
async def update_course():  # NOQA
    return {"courses": []}


@router.delete("/{course_id}")
async def delete_course():  # NOQA
    return {"courses": []}


@router.get("/{course_id}/sections")
async def read_course_sections():  # NOQA
    return {"courses": []}
