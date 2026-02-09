import json

ARQUIVO = "pessoas.json"


def carregar():
    try:
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    except:
        return []


def salvar(pessoas):
    with open(ARQUIVO, "w") as f:
        json.dump(pessoas, f, indent=4)


def listar(pessoas):
    print("\nPESSOAS:")
    for i, p in enumerate(pessoas):
        print(f"{i} - {p['nome']} ({p['idade']} anos)")


def cadastrar(pessoas):
    nome = input("Nome: ")
    idade = int(input("Idade: "))

    pessoas.append({"nome": nome, "idade": idade})
    salvar(pessoas)


def editar(pessoas):
    listar(pessoas)
    i = int(input("Qual número editar: "))

    novo_nome = input("Novo nome: ")
    nova_idade = int(input("Nova idade: "))

    pessoas[i]["nome"] = novo_nome
    pessoas[i]["idade"] = nova_idade

    salvar(pessoas)


def deletar(pessoas):
    listar(pessoas)
    i = int(input("Qual número deletar: "))

    pessoas.pop(i)
    salvar(pessoas)


pessoas = carregar()

while True:
    print("\n1 - Listar")
    print("2 - Cadastrar")
    print("3 - Editar")
    print("4 - Deletar")
    print("5 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        listar(pessoas)

    elif opcao == "2":
        cadastrar(pessoas)

    elif opcao == "3":
        editar(pessoas)

    elif opcao == "4":
        deletar(pessoas)

    elif opcao == "5":
        break

