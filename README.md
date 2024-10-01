
# API-db com python  🐍
--

## CRIAÇÃO DA PASTA
    mkdir api 
    cd api 
-- 
### estrutura

- **API-BD**
- **venv/**                     # Ambiente virtual
- **.vscode/**                  # Configurações do VSCode
- **api/**                      # Diretório da API
  - **__pycache__/**            # Arquivos de cache do Python
  - **__init__.py**             # Arquivo de inicialização do pacote
  - **config.py**               # Configurações gerais
  - **crud.py**                 # Operações CRUD com o banco de dados
  - **main.py**                 # Arquivo principal da API
- **AlunoBD.session.sql**       # Sessão de banco de dados SQL
- **README.md**                 # Documentação do projeto


## Este projeto requer a instalação dos seguintes pacotes:

- **uvicorn** (para executar o servidor FastAPI)
- **FastAPI** (framework para criação da API)

    Para instalar, execute o comando abaixo:

    ```bash
    pip install fastapi uvicorn
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

```bash
get-command python
```

# OBSERVAÇÃO:  
E IMPORTANTE TER EXTENÇÃO DE BANCO DE DADOS ATIVADA NO SEU COMPUTADOR /VSCode 

    **SQLTools MySQL/MariaDB/TiDB**
    **Driver SQLTools PostgreSQL/Cockroach**
