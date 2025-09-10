from sqlalchemy.orm import Mapped, mapped_column
from database import Base


class Author(Base):
    __tablename__ = "authors"
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    birth_year: Mapped[int]