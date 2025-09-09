from pydantic import BaseModel


class AuthorSchema(BaseModel):
    first_name: str
    last_name: str
    birth_year: int
