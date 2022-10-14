"""Main application."""

from fastapi import FastAPI

from .api import courses, sections, users
from .db import engine
from .db.models import course, user

user.Base.metadata.create_all(bind=engine)
course.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Fast API LMS",
    description="LMS for managing students and courses.",
    version="0.6.1",
    contact={
        "name": "Gleb Khaykin",
        "email": "khaykingleb@gmail.com",
    },
    license_info={
        "name": "MIT License",
    },
)

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)
