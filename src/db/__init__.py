"""SQLAlchemy setup."""

import typing as tp

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .. import cfg

engine = create_engine(cfg.POSTGRES_URI, future=True)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)

Base = declarative_base()
DBTable = tp.Type[Base]


def get_db():  # NOQA
    db = session()
    try:
        yield db
    finally:
        db.close()
