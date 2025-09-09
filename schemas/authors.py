from pydantic import BaseModel


class BaseAuthorSchema(BaseModel):
    first_name: str
    last_name: str
    birth_year: int

class AuthorSchema(BaseAuthorSchema):
    id: int

class AuthorCreateSchema(BaseAuthorSchema):
    pass
