"""Main application."""

from fastapi import FastAPI

from .api import courses, sections, users

app = FastAPI(
    title="Fast API LMS",
    description="LMS for managing students and courses.",
    version="0.1.0",
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
