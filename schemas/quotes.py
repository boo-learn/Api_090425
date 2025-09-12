from pydantic import BaseModel, ConfigDict
from schemas.authors import AuthorSchema


class BaseQuoteSchema(BaseModel):
    text: str
    # author: AuthorSchema


class QuoteSchema(BaseQuoteSchema):
    id: int
    author_id: int
    author: AuthorSchema | None = None

    model_config = ConfigDict(from_attributes=True)


class QuoteCreateSchema(BaseQuoteSchema):
    author_id: int
