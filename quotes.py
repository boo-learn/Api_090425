from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

# Инициализация приложения FastAPI
app = FastAPI()

# Глобальное хранилище цитат в виде списка словарей
fake_quotes = [
    {"id": 1, "text": "Программирование — это искусство заставлять компьютер делать то, что вы хотите."},
    {"id": 2, "text": "Код — это стихи, написанные на языке логики."}
]

last_id = 2

class Quote(BaseModel):
    text: str


@app.get("/", status_code=status.HTTP_200_OK)
def read_root():
    """
    Корневой путь, возвращающий приветственное сообщение.
    """
    return {"message": "Добро пожаловать в API цитат!"}


@app.get("/quotes")
def get_all_quotes():
    """
    Возвращает список всех цитат.
    """
    return fake_quotes


@app.get("/quotes/{quote_id}")
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


@app.post("/quotes", status_code=status.HTTP_201_CREATED)
def create_quote(quote: Quote):
    """
    Добавляет новую цитату.
    """
    global last_id
    last_id += 1
    new_quote = {"id": last_id, "text": quote["text"].strip()}
    fake_quotes.append(new_quote)
    return new_quote


@app.put("/quotes/{quote_id}")
def update_quote(quote_id: int, updated_quote: Quote):
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


@app.delete("/quotes/{quote_id}")
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