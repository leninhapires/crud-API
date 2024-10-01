from typing import List
from fastapi import FastAPI, HTTPException

app = FastAPI()


alunos = []

@app.get('/alunos')
def listar():
    return alunos

@app.post('/alunos')
def adicionar(nome: str, email: str):
    # Verifica se o aluno já existe
    for aluno in alunos:
        if aluno['nome'].lower() == nome.lower():
            raise HTTPException(status_code=400, detail='Aluno já existe')
    
    novo_aluno = {'nome': nome, 'email': email}
    alunos.append(novo_aluno)
    return novo_aluno

@app.get('/alunos/{nome}')
def pesquisar(nome: str):
    # Pesquisa o aluno pelo nome
    for aluno in alunos:
        if aluno['nome'].lower() == nome.lower():
            return aluno
    raise HTTPException(status_code=404, detail="Aluno não encontrado!")

@app.delete('/alunos/{nome}')
def deletar(nome: str):
    # Encontra e remove o aluno
    for aluno in alunos:
        if aluno['nome'].lower() == nome.lower():
            alunos.remove(aluno)
            return {"mensagem": "Aluno removido!"}
    raise HTTPException(status_code=404, detail="Aluno não encontrado!")

@app.put('/alunos/{nome}')
def atualizar(nome: str, novo_nome: str = None, novo_email: str = None):
    # Atualiza as informações do aluno
    for aluno in alunos:
        if aluno['nome'].lower() == nome.lower():
            if novo_nome:
                aluno['nome'] = novo_nome
            
            if novo_email:
                aluno['email'] = novo_email
            return {"mensagem": "Aluno atualizado com sucesso!", "aluno": aluno}
    
    raise HTTPException(status_code=404, detail="Aluno não encontrado!")
