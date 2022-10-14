"""Sections."""

import fastapi

router = fastapi.APIRouter(
    prefix="/sections",
    tags=["Sections"],
)


@router.get("/{id}")
async def read_section():  # NOQA
    return {"courses": []}


@router.get("/{id}/content-blocks")
async def read_section_content_blocks():  # NOQA
    return {"courses": []}


@router.get("/content-blocks/{id}")
async def read_content_block():  # NOQA
    return {"courses": []}
