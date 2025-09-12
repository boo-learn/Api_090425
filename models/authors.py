from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base

import typing

if typing.TYPE_CHECKING:
    from models.quotes import Quote


# parent
class Author(Base):
    __tablename__ = "authors"
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    birth_year: Mapped[int]
    quotes: Mapped[list["Quote"]] = relationship(back_populates="author", cascade="all, delete-orphan")
