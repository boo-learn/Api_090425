from fastapi import APIRouter, HTTPException, status
from schemas.authors import AuthorSchema
from schemas.quotes import QuoteSchema, QuoteCreateSchema
from services import storage

router = APIRouter()
# Глобальное хранилище цитат в виде списка словарей
fake_quotes = [
    {
        "id": 1,
        "text": "Программирование — это искусство заставлять компьютер делать то, что вы хотите.",
        "author": {
            "first_name": "Иван",
            "last_name": "Петров",
            "birth_year": 1900,
        }
    },
    {
        "id": 2,
        "text": "Код — это стихи, написанные на языке логики.",
        "author": {
            "first_name": "Иван",
            "last_name": "Петров",
            "birth_year": 1900,
        }
    }
]

last_id = 2


@router.get("/", response_model=list[QuoteSchema])
def get_all_quotes():
    """
    Возвращает список всех цитат.
    """
    return storage.get_all_quotes()


@router.get("/{quote_id}")
def get_quote(quote_id: int):
    """
    Возвращает цитату по ее уникальному идентификатору.
    """
    ...


@router.post("/", response_model=QuoteSchema, status_code=status.HTTP_201_CREATED)  # сериализация
# @app.post("/quotes", status_code=status.HTTP_201_CREATED)  # сериализация
def create_quote(quote: QuoteCreateSchema):  # десериализация
    """
    Добавляет новую цитату.
    """
    new_quote = storage.create_quote(quote.model_dump())
    return new_quote


@router.put("/{quote_id}")
def update_quote(quote_id: int, updated_quote: QuoteSchema):
    """
    Обновляет существующую цитату.
    """
    ...


@router.delete("/{quote_id}")
def delete_quote(quote_id: int):
    """
    Удаляет цитату по ее идентификатору.
    """
    ...
