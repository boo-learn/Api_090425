from fastapi import APIRouter, HTTPException, status
from schemas.authors import AuthorSchema, AuthorCreateSchema
from services import storage

router = APIRouter()

@router.get("/", response_model=list[AuthorSchema])
def get_all_authors():
    """
    Возвращает список всех авторов.
    """
    return storage.get_all_authors()


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
def create_quote(author: AuthorCreateSchema):
    new_author = storage.create_author(author.model_dump())
    return new_author
