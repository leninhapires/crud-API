from sqlalchemy import Column, Integer, String
from .database import Base

class Aluno(Base):
    __tablename__ = "alunos"

   
    nome = Column(String, index=True)
    email = Column(String, unique=True, index=True)