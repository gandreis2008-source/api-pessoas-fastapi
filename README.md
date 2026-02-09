# API de Pessoas — FastAPI

API REST para cadastro, listagem, edição e exclusão de pessoas, desenvolvida em **Python + FastAPI** com persistência em **SQLite** e deploy em nuvem.

## 🔗 Acesse online

* Documentação (Swagger):
  `https://SEU-LINK-ONRENDER.onrender.com/docs`

## 🚀 Funcionalidades

* Criar pessoa (POST /pessoas)
* Listar pessoas (GET /pessoas)
* Atualizar pessoa (PUT /pessoas/{id})
* Deletar pessoa (DELETE /pessoas/{id})

## 🧱 Tecnologias

* Python
* FastAPI
* SQLite
* Pydantic
* Uvicorn
* Render (deploy)

## ▶️ Como rodar localmente

```bash
git clone https://github.com/SEU-USUARIO/api-pessoas-fastapi.git
cd api-pessoas-fastapi
pip install -r requirements.txt
uvicorn api:app --reload
```

Abra: `http://127.0.0.1:8000/docs`

## 📚 O que aprendi neste projeto

* Construção de API REST
* Operações CRUD
* Integração com banco de dados
* Validação de dados com Pydantic
* Deploy em nuvem
