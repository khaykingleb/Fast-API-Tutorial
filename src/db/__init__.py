"""SQLAlchemy setup."""

import typing as tp

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .. import cfg

engine = create_engine(cfg.POSTGRES_URI, future=True)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)

async_engine = create_async_engine(cfg.ASYNC_POSTGRES_URI)
async_session = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()
DBTable = tp.Type[Base]


def get_db():  # NOQA
    db = session()
    try:
        yield db
    finally:
        db.close()


async def async_get_db():  # NOQA
    async with async_session() as db:
        yield db
        await db.commit()
