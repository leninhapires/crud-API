from sqlalchemy import Column, Integer, String
from .database import Base

class Aluno(Base):
    __tablename__ = "aluno"

   
    nome = Column(String, index=True)
    email = Column(String, unique=True, index=True)