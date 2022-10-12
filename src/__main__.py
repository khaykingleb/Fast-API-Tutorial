"""Main application."""

import typing as tp

from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

app = FastAPI(
    title="Fast API LMS",
    description="LMS for managing students and courses.",
    version="0.0.0",
    contact={
        "name": "Gleb Khaykin",
        "email": "khaykingleb@gmail.com",
    },
    license_info={
        "name": "MIT License",
    },
)

users = []


class User(BaseModel):  # NOQA
    email: str
    is_active: bool
    bio: tp.Optional[str]


@app.post("/users")
async def create_user(user: User):  # NOQA
    users.append(user)
    return "Success"


@app.get("/users", response_model=tp.List[User])
async def get_users():  # NOQA
    return users


@app.get("/users/{id}")
async def get_user(  # NOQA
    id: int = Path(description="The ID of the user you want to retrieve.", gt=2),
    q: str = Query(default=None, max_length=5),
) -> tp.Dict[str, tp.Any]:
    return {
        "user": users[id],
        "query": q,
    }
