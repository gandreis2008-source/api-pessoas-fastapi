import sqlite3

conexao = sqlite3.connect("pessoas.db")
cursor = conexao.cursor()

cursor.execute("SELECT * FROM pessoas")
pessoas = cursor.fetchall()

conexao.close()

print("PESSOAS NO BANCO:")

for p in pessoas:
    print(p)
