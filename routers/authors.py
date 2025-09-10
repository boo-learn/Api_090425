from fastapi import APIRouter, HTTPException, Depends, status
from schemas.authors import AuthorSchema, AuthorCreateSchema
from services import storage
from database import get_session
from models.authors import Author
from sqlalchemy.orm import Session
from sqlalchemy import select

router = APIRouter()


@router.get("/", response_model=list[AuthorSchema])
def get_all_authors(session: Session = Depends(get_session)):
    """
    Возвращает список всех авторов.
    """
    stmt = select(Author)
    authors = session.scalars(stmt).all()
    return authors


@router.get("/{author_id}", response_model=AuthorSchema)
def get_quote(author_id: int):
    """
    Возвращает автора по его уникальному идентификатору.
    """
    author = storage.get_author_by_id(author_id)
    if author is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Author with id={author_id} not found"
        )
    return author


@router.post("/", response_model=AuthorSchema, status_code=status.HTTP_201_CREATED)  # сериализация
def create_quote(author: AuthorCreateSchema, session: Session = Depends(get_session)):
    # new_author = storage.create_author(author.model_dump())
    db_author = Author(**author.model_dump())
    session.add(db_author)
    session.commit()
    session.refresh(db_author)

    return db_author
