import random;
from fastapi import FastAPI;
from pydantic import BaseModel;

app = FastAPI()


class Estudante(BaseModel):
    name: str
    curso: str
    ativo: bool


@app.get("/")
async def root():
    return {"mensagem": "🚀 FastAPI rodando certinho!"}

#http://127.0.0.1:8000/teste
@app.get("/teste")
async def funcaoteste():
    return {"teste": True, "num_aleatorio": random.randint(0,5000)}

#http://127.0.0.1:8000/hello/Gabrielly
@app.get("/hello/{nome}")
async def hello(nome: str):
    return {"mensagem": f"Olá, {nome}!"}

#cadastro
@app.post("/estudantes/cadastro")
async def create_estudante(estudante: Estudante):
    return estudante

#update
@app.put("/estudantes/update/{id_estudante}")
async def update_item(id_estudante: int):
    return id_estudante > 0

#delete
@app.delete("/estudantes/delete/{id_estudante}")
async def delete_estudante(id_estudante: int):
    return id_estudante > 0
