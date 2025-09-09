from fastapi import APIRouter, HTTPException, status
from schemas.authors import AuthorSchema
from schemas.quotes import QuoteSchema, QuoteCreateSchema

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
    return fake_quotes


@router.get("/{quote_id}")
def get_quote(quote_id: int):
    """
    Возвращает цитату по ее уникальному идентификатору.
    """
    for quote in fake_quotes:
        if quote["id"] == quote_id:
            return quote
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Цитата не найдена."
    )


@router.post("/", response_model=QuoteSchema, status_code=status.HTTP_201_CREATED)  # сериализация
# @app.post("/quotes", status_code=status.HTTP_201_CREATED)  # сериализация
def create_quote(quote: QuoteCreateSchema):  # десериализация
    """
    Добавляет новую цитату.
    """
    global last_id
    last_id += 1
    new_quote = {"id": last_id, "text": quote.text.strip()}
    fake_quotes.append(new_quote)
    return new_quote


@router.put("/{quote_id}")
def update_quote(quote_id: int, updated_quote: QuoteSchema):
    """
    Обновляет существующую цитату.
    """
    for quote in fake_quotes:
        if quote["id"] == quote_id:
            quote.update(updated_quote)
            return quote

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Цитата не найдена."
    )


@router.delete("/{quote_id}")
def delete_quote(quote_id: int):
    """
    Удаляет цитату по ее идентификатору.
    """
    for index, quote in enumerate(fake_quotes):
        if quote["id"] == quote_id:
            del fake_quotes[index]
            return {"message": "Цитата успешно удалена"}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Цитата не найдена."
    )
