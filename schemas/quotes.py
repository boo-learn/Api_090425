from pydantic import BaseModel
from schemas.authors import AuthorSchema


class BaseQuoteSchema(BaseModel):
    text: str
    author: AuthorSchema


class QuoteSchema(BaseQuoteSchema):
    id: int


class QuoteCreateSchema(BaseQuoteSchema):
    pass
