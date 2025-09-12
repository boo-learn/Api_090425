from fastapi import APIRouter, HTTPException, status, Depends, Query
from schemas.quotes import QuoteSchema, QuoteCreateSchema
from database import get_session
from sqlalchemy.orm import Session
from sqlalchemy.orm import selectinload, noload
from sqlalchemy import select
from models.authors import Author
from models.quotes import Quote

router = APIRouter()
# Глобальное хранилище цитат в виде списка словарей


@router.get("/", response_model=list[QuoteSchema])
def get_all_quotes(
    expand: str | None = Query(default=None, description="Например: author"),
    session: Session = Depends(get_session),
):
    """
    Возвращает список всех цитат.
    """
    if expand == "author":
        stmt = select(Quote).options(selectinload(Quote.author))
    else:
        stmt = select(Quote).options(noload(Quote.author))
    quotes = session.scalars(stmt).all()
    return quotes


@router.get("/{quote_id}", response_model=QuoteSchema)
def get_quote(
    quote_id: int,
    expand: str | None = Query(default=None, description="Например: author"),
    session: Session = Depends(get_session),
):
    """
    Возвращает цитату по ее уникальному идентификатору.
    """
    if expand == "author":
        quote = session.get(Quote, quote_id, options=(selectinload(Quote.author),))
    else:
        quote = session.get(Quote, quote_id, options=(noload(Quote.author),))
    if quote is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Quote with id={quote_id} not found"
        )
    return quote


@router.post("/", response_model=QuoteSchema, status_code=status.HTTP_201_CREATED)  # сериализация
# @app.post("/quotes", status_code=status.HTTP_201_CREATED)  # сериализация
def create_quote(
        quote: QuoteCreateSchema,
        session: Session = Depends(get_session)
):  # десериализация
    """
    Добавляет новую цитату.
    """
    author = session.get(Author, quote.author_id)
    if author is not None:
        new_quote = Quote(text=quote.text, author=author)
        session.add(new_quote)
        session.commit()
        session.refresh(new_quote)
        return new_quote
        # new_quote = storage.create_quote(quote.model_dump())



@router.put("/{quote_id}", response_model=QuoteSchema)
def update_quote(quote_id: int, updated_quote: QuoteCreateSchema, session: Session = Depends(get_session)):
    """
    Обновляет существующую цитату.
    """
    quote = session.get(Quote, quote_id)
    if quote is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Quote with id={quote_id} not found"
        )
    
    # Проверяем, что автор существует
    author = session.get(Author, updated_quote.author_id)
    if author is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Author with id={updated_quote.author_id} not found"
        )
    
    quote.text = updated_quote.text
    quote.author_id = updated_quote.author_id
    
    session.commit()
    session.refresh(quote)
    return quote


@router.delete("/{quote_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_quote(quote_id: int, session: Session = Depends(get_session)):
    """
    Удаляет цитату по ее идентификатору.
    """
    quote = session.get(Quote, quote_id)
    if quote is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Quote with id={quote_id} not found"
        )
    
    session.delete(quote)
    session.commit()
    return None
