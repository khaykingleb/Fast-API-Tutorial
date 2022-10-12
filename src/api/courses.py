"""Courses."""

import fastapi

router = fastapi.APIRouter()


@router.get("/courses")
async def read_courses():  # NOQA
    return {"courses": []}


@router.post("/courses")
async def create_course_api():  # NOQA
    return {"courses": []}


@router.get("/courses/{id}")
async def read_course():  # NOQA
    return {"courses": []}


@router.patch("/courses/{id}")
async def update_course():  # NOQA
    return {"courses": []}


@router.delete("/courses/{id}")
async def delete_course():  # NOQA
    return {"courses": []}


@router.get("/courses/{id}/sections")
async def read_course_sections():  # NOQA
    return {"courses": []}
