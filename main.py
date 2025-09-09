from fastapi import FastAPI
from routers import quotes, authors

app = FastAPI()

app.include_router(
    quotes.router,
    prefix='/quotes',
    tags=['quotes']
)

app.include_router(
    authors.router,
    prefix='/authors',
    tags=['authors']
)