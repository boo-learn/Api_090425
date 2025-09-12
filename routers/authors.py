from fastapi import APIRouter, HTTPException, Depends, status
from schemas.authors import AuthorSchema, AuthorCreateSchema
from schemas.quotes import QuoteSchema
from database import get_session
from models.authors import Author
from models.quotes import Quote
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
def get_author(author_id: int, session: Session = Depends(get_session)):
    """
    Возвращает автора по его уникальному идентификатору.
    """
    author = session.get(Author, author_id)
    if author is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Author with id={author_id} not found"
        )
    return author


@router.post("/", response_model=AuthorSchema, status_code=status.HTTP_201_CREATED)  # сериализация
def create_author(author: AuthorCreateSchema, session: Session = Depends(get_session)):
    """
    Создает нового автора.
    """
    db_author = Author(**author.model_dump())
    session.add(db_author)
    session.commit()
    session.refresh(db_author)
    return db_author


@router.put("/{author_id}", response_model=AuthorSchema)
def update_author(author_id: int, author_update: AuthorCreateSchema, session: Session = Depends(get_session)):
    """
    Обновляет существующего автора.
    """
    author = session.get(Author, author_id)
    if author is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Author with id={author_id} not found"
        )
    
    for field, value in author_update.model_dump().items():
        setattr(author, field, value)
    
    session.commit()
    session.refresh(author)
    return author


@router.delete("/{author_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_author(author_id: int, session: Session = Depends(get_session)):
    """
    Удаляет автора по его идентификатору.
    """
    author = session.get(Author, author_id)
    if author is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Author with id={author_id} not found"
        )
    
    session.delete(author)
    session.commit()
    return None


@router.get("/{author_id}/quotes", response_model=list[QuoteSchema])
def get_author_quotes(author_id: int, session: Session = Depends(get_session)):
    """
    Возвращает все цитаты конкретного автора.
    """
    author = session.get(Author, author_id)
    if author is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Author with id={author_id} not found"
        )
    stmt = select(Quote).where(Quote.author_id == author_id)
    quotes = session.scalars(stmt).all()
    return quotes
