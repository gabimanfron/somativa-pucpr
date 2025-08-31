from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"mensagem": "🚀 FastAPI rodando certinho!"}

#http://127.0.0.1:8000/hello/Gabrielly
@app.get("/hello/{nome}")
def hello(nome: str):
    return {"mensagem": f"Olá, {nome}!"}
