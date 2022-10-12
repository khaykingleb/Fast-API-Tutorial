"""Main application."""

from fastapi import FastAPI

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
