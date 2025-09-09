import uuid  # id = str(uuid.uuid4())

from tmp.quotes import last_id

# Имитация хранилища данных с использованием словарей в памяти.
quotes_db: dict[int, dict] = {
    1: {"id": 1,
        "text": "Программирование — это искусство заставлять ...",
        "author_id": 3,
        },
    2: {
        "id": 2,
        "text": "Код — это стихи, написанные на языке логики.",
        "author_id": 3,
    }
}
last_quote_id = 2

authors_db: dict[int, dict] = {
    3: {
        "id": 3,
        "first_name": "Petr",
        "last_name": "Ivanov",
        "birth_year": 1910
    }
}

last_author_id = 3


# Функции для работы с цитатами
def create_quote(quote: dict) -> dict:
    """Создает новую цитату."""
    global last_quote_id
    new_quote = {"id": last_quote_id + 1, "text": quote["text"]}
    quotes_db[last_quote_id + 1] = new_quote
    last_quote_id += 1
    return new_quote


def get_quote_by_id(quote_id: str) -> dict | None:
    """Получает цитату по ID."""
    return ...


def get_all_quotes() -> list[dict]:
    """Возвращает список всех цитат."""
    quotes = list(quotes_db.values())
    for quote in quotes:
        author = get_author_by_id(quote["author_id"])
        quote["author"] = author
    return quotes


def get_quotes_by_author(author_id: str) -> list[dict]:
    """Возвращает все цитаты указанного автора."""
    return ...


def update_quote(quote_id: str, new_data: dict) -> dict | list:
    """Обновляет данные цитаты."""
    ...
    return ...


def delete_quote(quote_id: str) -> bool:
    """Удаляет цитату."""
    if quote_id in quotes_db:
        ...
        return True
    return False


# Функции для работы с авторами
def create_author(author: dict) -> dict:
    """Создает нового автора."""
    global last_author_id
    new_author = author.copy()
    new_author["id"] = last_author_id + 1
    authors_db[last_author_id + 1] = new_author
    last_author_id += 1
    return new_author


def get_author_by_id(author_id: int) -> dict | None:
    """Получает автора по ID."""
    return authors_db.get(author_id)


def get_all_authors() -> list[dict]:
    """Возвращает список всех авторов."""
    return list(authors_db.values())


def update_author(author_id: str, new_data: dict) -> dict | None:
    """Обновляет данные автора."""
    ...
    return ...


def delete_author(author_id: str) -> bool:
    """Удаляет автора и связанные с ним цитаты."""
    if author_id in authors_db:
        # Удаляем автора и все цитаты этого автора
        ...
        return True
    return False
