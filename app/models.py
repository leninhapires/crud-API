from pydantic import BaseModel

class Aluno(BaseModel):
    id: int
    nome: str
    email: str

    class Config:
        from_attributes = True   
