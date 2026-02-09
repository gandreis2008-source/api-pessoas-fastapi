from fastapi import FastAPI, HTTPException
from db import listar_pessoas, adicionar_pessoa, atualizar_pessoa, deletar_pessoa
from models import Pessoa

app = FastAPI()


@app.get("/")
def home():
    return {"mensagem": "API CRUD completa"}


@app.get("/pessoas")
def get_pessoas():
    pessoas = listar_pessoas()

    return [
        {"id": p[0], "nome": p[1], "idade": p[2]}
        for p in pessoas
    ]


@app.post("/pessoas")
def post_pessoa(pessoa: Pessoa):
    adicionar_pessoa(pessoa.nome, pessoa.idade)
    return {"status": "Pessoa adicionada"}


@app.put("/pessoas/{id}")
def put_pessoa(id: int, pessoa: Pessoa):
    atualizar_pessoa(id, pessoa.nome, pessoa.idade)
    return {"status": "Pessoa atualizada"}


@app.delete("/pessoas/{id}")
def delete_pessoa(id: int):
    deletar_pessoa(id)
    return {"status": "Pessoa deletada"}
