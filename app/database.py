import os #importei essa biblioteca

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv #importei essa biblioteca

load_dotenv() #chamei esse metodo pra obter as variaveis do arquivo .env

# Obter as variáveis de ambiente
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}" #mudei a URL pra guardar teus dados

engine = create_engine(DATABASE_URL, pool_pre_ping=True, echo=True) #aqui adicionei o echo e o pre ping

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()