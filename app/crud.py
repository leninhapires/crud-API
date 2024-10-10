from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import Session
from typing import List, Optional
from .database import Base, engine, SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Aluno(Base):
    __tablename__ = "alunos"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    email = Column(String)

Base.metadata.create_all(bind=engine)

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
