"""Utilities for users."""

from sqlalchemy.orm import Session

from ...db.models.user import User
from ...schemas.user import UserCreate


def get_user(db: Session, user_id: int):  # NOQA
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):  # NOQA
    return db.query(User).filter(User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):  # NOQA
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate):  # NOQA
    db_user = User(email=user.email, role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
