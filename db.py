import sqlite3

DB = "pessoas.db"


def conectar():
    return sqlite3.connect(DB)


def listar_pessoas():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT id, nome, idade FROM pessoas")
    pessoas = cursor.fetchall()

    conn.close()

    return pessoas


def adicionar_pessoa(nome, idade):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO pessoas (nome, idade) VALUES (?, ?)",
        (nome, idade)
    )

    conn.commit()
    conn.close()

def atualizar_pessoa(id, nome, idade):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE pessoas SET nome = ?, idade = ? WHERE id = ?",
        (nome, idade, id)
    )

    conn.commit()
    conn.close()


def deletar_pessoa(id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM pessoas WHERE id = ?", (id,))

    conn.commit()
    conn.close()
