import sqlite3

conexao = sqlite3.connect("pessoas.db")

cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS pessoas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    idade INTEGER
)
""")

conexao.commit()
conexao.close()

print("Banco criado com sucesso")
