from typing import Any, Generator, AsyncGenerator

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker, AsyncAttrs
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Session
from contextlib import asynccontextmanager

DATABASE_URL = "postgresql+asyncpg://postgres:postgres_password@localhost:5432/postgres_db"
engine = create_async_engine(DATABASE_URL)
AsyncSessionLocal = async_sessionmaker(bind=engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


@asynccontextmanager
async def get_session() -> AsyncGenerator[AsyncSession, Any]:
    async with AsyncSessionLocal() as session:
        yield session