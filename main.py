from typing import List
from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from crud import listar_alunos, adicionar_aluno, pesquisar_aluno, deletar_aluno, atualizar_aluno, SessionLocal, Aluno
from models import Aluno 
app = FastAPI()

# Dependência para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/alunos', response_model=List[Aluno])
def listar(db: Session = Depends(get_db)):
    return listar_alunos(db)

@app.post('/alunos', response_model=Aluno)
def adicionar(nome: str, email: str, db: Session = Depends(get_db)):
    # Verifica se o aluno já existe
    if pesquisar_aluno(db, nome):
        raise HTTPException(status_code=400, detail='Aluno já existe')
    
    novo_aluno = adicionar_aluno(db, nome, email)
    return novo_aluno

@app.get('/alunos/{nome}', response_model=Aluno)
def pesquisar(nome: str, db: Session = Depends(get_db)):
    aluno = pesquisar_aluno(db, nome)
    if aluno:
        return aluno
    raise HTTPException(status_code=404, detail="Aluno não encontrado!")

@app.delete('/alunos/{nome}', response_model=dict)
def deletar(nome: str, db: Session = Depends(get_db)):
    if deletar_aluno(db, nome):
        return {"mensagem": "Aluno removido!"}
    raise HTTPException(status_code=404, detail="Aluno não encontrado!")

@app.put('/alunos/{nome}', response_model=Aluno)
def atualizar(nome: str, novo_nome: str = None, novo_email: str = None, db: Session = Depends(get_db)):
    aluno = atualizar_aluno(db, nome, novo_nome, novo_email)
    if aluno:
        return {"mensagem": "Aluno atualizado com sucesso!", "aluno": aluno}
    
    raise HTTPException(status_code=404, detail="Aluno não encontrado!")
