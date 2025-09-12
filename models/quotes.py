from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from database import Base

import typing

if typing.TYPE_CHECKING:
    from models.authors import Author


# child
class Quote(Base):
    __tablename__ = 'quotes'
    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str]
    author_id: Mapped[int] = mapped_column(ForeignKey('authors.id'))
    author: Mapped["Author"] = relationship(back_populates="quotes")
