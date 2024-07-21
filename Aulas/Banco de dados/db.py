import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent
FILE_PATH = ROOT_PATH / "meu_banco.db"

con = sqlite3.connect(FILE_PATH)
cursor = con.cursor()
cursor.row_factory = sqlite3.Row

def criar_tabela(cursor):
    cursor.execute("CREATE TABLE clientes(id INTEGER primary key AUTOINCREMENT, nome VARCHAR(100) NOT NULL, email VARCHAR(100) UNIQUE)")


def inserir_cliente(con, cursor, data):
    cursor.execute("INSERT INTO clientes(nome, email) VALUES(?,?)", data)
    con.commit()


def inserir_clientes(con, cursor, data):
    cursor.executemany("INSERT INTO clientes(nome, email) VALUES(?, ?)", data)
    con.commit()

def listar_clientes(cursor):
    return cursor.execute('SELECT * FROM clientes')
    

clientes = listar_clientes(cursor)

for c in clientes:
    print(c['nome'])