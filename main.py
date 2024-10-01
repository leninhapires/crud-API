from fastapi import FastAPI, HTTPException
import psycopg2
from typing import List

app = FastAPI()

def get_connection():
    return psycopg2.connect(
        dbname="AlunoDB",
        user="postgres",
        password="181216",
        host="localhost",
        port="5432"
    )

Alunos : List[dict] = []

@app.get('/Alunos')
def liste():
    return Alunos

@app.post('/Alunos')
def adicionar(nome: str, email: str):
    for aluno in Alunos:
        if aluno['nome'].lower() == nome.lower():
            print(f'Adicionando aluno: {nome}, {email}')
            raise HTTPException(status_code=400, detail='Aluno já existe')
    novo_aluno = {'nome': nome, 'email': email}
    Alunos.append(novo_aluno)
    return novo_aluno

@app.get('/Alunos/{nome}')
def pesquisar(nome: str):
    for aluno in Alunos:
        if aluno['nome'].lower() == nome.lower():
            return aluno
    raise HTTPException(status_code=404, detail="Aluno não encontrado!")

@app.delete('/alunos/{nome}')
def deletar(nome: str):
    for aluno in Alunos:
        if aluno['nome'].lower() == nome.lower():
            Alunos.remove(aluno)
            return {"mensagem": "Aluno removido!"}
    raise HTTPException(status_code=404, detail="Aluno não encontrado!")

@app.put('/alunos/{nome}')
def atualizar(nome: str, novo_nome: str = None, novo_email: str = None):
    for aluno in Alunos:
        if aluno['nome'].lower() == nome.lower():
            if novo_nome:
                aluno['nome'] = novo_nome
            
            if novo_email:
                aluno['email'] = novo_email
            return {"mensagem": "Aluno atualizado com sucesso!", "aluno": aluno}
    raise HTTPException(status_code=404, detail="Aluno não encontrado!")