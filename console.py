from database import SessionLocal
from models.authors import Author
from sqlalchemy import select

print("from database import SessionLocal")
print("from models.authors import Author")
print("from sqlalchemy import select")

session = SessionLocal()
