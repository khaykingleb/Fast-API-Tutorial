"""SQLAlchemy model for Users."""

import enum

from sqlalchemy import Boolean, Column, Enum, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from .mixins import Timestamp
from .. import Base


class Role(enum.Enum):  # NOQA
    teacher = 1
    student = 2


class User(Timestamp, Base):  # NOQA
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, index=True, nullable=False)
    role = Column(Enum(Role))

    profile = relationship("Profile", back_populates="owner", uselist=False)


class Profile(Timestamp, Base):  # NOQA
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    bio = Column(Text, nullable=True)
    is_active = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    owner = relationship("User", back_populates="profile")
