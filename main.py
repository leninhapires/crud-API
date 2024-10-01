import psycopg2
from typing import List
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import engine
from . import crud, models, database

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get('/aluno')
def liste():
    return 

@app.post('/aluno')
def adicionar(nome: str, email: str):
    for aluno in aluno:
        if aluno['nome'].lower() == nome.lower():
            print(f'Adicionando aluno: {nome}, {email}')
            raise HTTPException(status_code=400, detail='Aluno já existe')
    novo_aluno = {'nome': nome, 'email': email}
    aluno.append(novo_aluno)
    return novo_aluno

@app.get('/aluno/{nome}')
def pesquisar(nome: str):
    for aluno in aluno:
        if aluno['nome'].lower() == nome.lower():
            return aluno
    raise HTTPException(status_code=404, detail="Aluno não encontrado!")

@app.delete('/aluno/{nome}')
def deletar(nome: str):
    for aluno in aluno:
        if aluno['nome'].lower() == nome.lower():
            aluno.remove(aluno)
            return {"mensagem": "Aluno removido!"}
    raise HTTPException(status_code=404, detail="Aluno não encontrado!")

@app.put('/aluno/{nome}')
def atualizar(nome: str, novo_nome: str = None, novo_email: str = None):
    for aluno in aluno:
        if aluno['nome'].lower() == nome.lower():
            if novo_nome:
                aluno['nome'] = novo_nome
            
            if novo_email:
                aluno['email'] = novo_email
            return {"mensagem": "Aluno atualizado com sucesso!", "aluno": aluno}
    raise HTTPException(status_code=404, detail="Aluno não encontrado!")