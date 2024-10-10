from typing import List
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app.crud import listar_alunos, adicionar_aluno, pesquisar_aluno, deletar_aluno, atualizar_aluno, Aluno, get_db
from app.models import Aluno
from app.database import SessionLocal
# importei as coisas das bibliotecas certas e apaguei o que nao precisava
from fastapi import FastAPI

app = FastAPI()


@app.get('/alunos', response_model=List[Aluno])
def listar(db: Session = Depends(get_db)):
    return listar_alunos(db)

@app.post('/alunos', response_model=Aluno)
def adicionar(nome: str, email: str, db: Session = Depends(get_db)):
    
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
