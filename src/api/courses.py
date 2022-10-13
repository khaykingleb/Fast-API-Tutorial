"""Courses."""

import fastapi

router = fastapi.APIRouter(
    prefix="/courses",
    tags=["courses"],
)


@router.get("/")
async def read_courses():  # NOQA
    return {"courses": []}


@router.post("/")
async def create_course_api():  # NOQA
    return {"courses": []}


@router.get("/{id}")
async def read_course():  # NOQA
    return {"courses": []}


@router.patch("/{id}")
async def update_course():  # NOQA
    return {"courses": []}


@router.delete("/{id}")
async def delete_course():  # NOQA
    return {"courses": []}


@router.get("/{id}/sections")
async def read_course_sections():  # NOQA
    return {"courses": []}
