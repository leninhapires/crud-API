
# API-db com python  🐍
 
### Estrutura 


## Este projeto requer a instalação dos seguintes pacotes:

- **uvicorn** (para executar o servidor FastAPI)
- **FastAPI** (framework para criação da API)
- **psycopg2**(postgresql)

- ##    Para instalar, execute o comando abaixo:

    ```bash
    pip install fastapi uvicorn psycopg2

    ```

- **Python** (linguagem de programação)

    Verifique se o Python está instalado com o comando:

    ```bash
    python --version
    ```

- **PostgreSQL** (banco de dados)

    Instale pelo site oficial: [https://www.postgresql.org/download/](https://www.postgresql.org/download/)

    Dependências necessárias para conectar com PostgreSQL no projeto:

    ```bash
    pip install psycopg2
    ```

---

## Verificar se o Uvicorn está ativo:

Use o comando abaixo para verificar se o Python e o Uvicorn estão configurados corretamente:


- CONFIGURANDO AMBIENTE 
  
    crie ambiente virtual  

        .venv\Script\Activate.ps1

    Verificar se o ambiente está ativo  

            get-command Python
    atualizar pip    

            python -m  pip install --upgrade pip

# OBSERVAÇÃO:  
E IMPORTANTE TER EXTENÇÃO DE BANCO DE DADOS ATIVADA NO SEU COMPUTADOR /VSCode 

    - SQLTools MySQL/MariaDB/TiDB 
    - Driver SQLTools PostgreSQL/Cockroach 
---
---

# DOCKERIZAR

- Tenha instalado docker desktop ou  Racher desktop

    - pastas nescessarias   

            dockerfile
            docker-compose.yml
            dockerignore
    -comandos

        docker build -t nome_imagem .
        docker-compose up --build
        docker run -it nome_imagem

