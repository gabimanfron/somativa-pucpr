from fastapi import FastAPI;
import random;

app = FastAPI()

@app.get("/")
async def root():
    return {"mensagem": "🚀 FastAPI rodando certinho!"}

#http://127.0.0.1:8000/teste1
@app.get("/teste1")
async def funcaoteste():
    return {"teste": True, "num_aleatorio": random.randint(0,10)}


#http://127.0.0.1:8000/hello/Gabrielly
@app.get("/hello/{nome}")
async def hello(nome: str):
    return {"mensagem": f"Olá, {nome}!"}
