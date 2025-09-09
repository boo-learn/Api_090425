from pydantic import BaseModel
from schemas.authors import AuthorSchema


class BaseQuoteSchema(BaseModel):
    text: str
    # author: AuthorSchema


class QuoteSchema(BaseQuoteSchema):
    id: int
    author: AuthorSchema


class QuoteCreateSchema(BaseQuoteSchema):
    author_id: int
