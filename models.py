from sqlalchemy import Column, Integer, String
from database import Base
from pydantic import BaseModel

class Aluno(BaseModel):
    id: int
    nome: str
    email: str

    class Config:
        from_attributes = True   # Permite que o modelo Pydantic trabalhe com modelos ORM como SQLAlchemy
