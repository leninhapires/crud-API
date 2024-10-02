# crud.py

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base  # Importação atual
from sqlalchemy.orm import sessionmaker, Session
from typing import List, Dict, Optional

# Alterar esta linha
from sqlalchemy.orm import declarative_base  # Nova importação

# Configuração do banco de dados
DATABASE_URL = "postgresql://postgres:123456@:5432/postgres"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()  # Agora está importando corretamente

# Definição do modelo de Aluno
class Aluno(Base):
    __tablename__ = "alunos"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    email = Column(String)

# Criação das tabelas
Base.metadata.create_all(bind=engine)

# Funções CRUD
def listar_alunos(db: Session) -> List[Aluno]:
    return db.query(Aluno).all()

def adicionar_aluno(db: Session, nome: str, email: str) -> Aluno:
    novo_aluno = Aluno(nome=nome, email=email)
    db.add(novo_aluno)
    db.commit()
    db.refresh(novo_aluno)
    return novo_aluno

def pesquisar_aluno(db: Session, nome: str) -> Optional[Aluno]:
    return db.query(Aluno).filter(Aluno.nome.ilike(nome)).first()

def deletar_aluno(db: Session, nome: str) -> bool:
    aluno = db.query(Aluno).filter(Aluno.nome.ilike(nome)).first()
    if aluno:
        db.delete(aluno)
        db.commit()
        return True
    return False

def atualizar_aluno(db: Session, nome: str, novo_nome: str = None, novo_email: str = None) -> Optional[Aluno]:
    aluno = db.query(Aluno).filter(Aluno.nome.ilike(nome)).first()
    if aluno:
        if novo_nome:
            aluno.nome = novo_nome
        if novo_email:
            aluno.email = novo_email
        db.commit()
        db.refresh(aluno)
        return aluno
    return None
