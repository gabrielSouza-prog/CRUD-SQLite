import sqlite3
conn = sqlite3.connect('lanchonete.db')
cursor = conn.cursor()

#criando a tabela
cursor.execute("""
	CREATE TABLE IF NOT EXISTS lanches(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, valor REAL)
	""")

#inserindo os dados na tabela
cursor.execute(""" INSERT INTO lanches (nome, valor) VALUES ('hamburguer', 8) """)
cursor.execute(""" INSERT INTO lanches (nome, valor) VALUES ('pastel', 4) """)
cursor.execute(""" INSERT INTO lanches (nome, valor) VALUES ('coxinha', 4) """)
cursor.execute(""" INSERT INTO lanches (nome, valor) VALUES ('suco', 3) """)
cursor.execute(""" INSERT INTO lanches (nome, valor) VALUES ('refrigerante', 3) """)

#ATUALIZANDO OS DADOS DA TABELA 
def update(id, nome, valor):
	cursor.execute(""" UPDATE lanches SET nome = ?, valor = ? WHERE id = ? """, (nome, valor, id))
update(1, 'açai', 6)

#ADICIONANDO UMA NOVA COLUNA A TABELA 
def add_column():
	cursor.execute(""" ALTER TABLE lanches ADD COLUMN quantidade INTEGER """)
add_column()

id = 1
quantidade = 10
cursor.execute(""" UPDATE lanches SET quantidade = ? WHERE id = ? """, (quantidade, id))

id = 2
quantidade = 10
cursor.execute(""" UPDATE lanches SET quantidade = ? WHERE id = ? """, (quantidade, id))

id = 3
quantidade = 10
cursor.execute(""" UPDATE lanches SET quantidade = ? WHERE id = ? """, (quantidade, id))

id = 4
quantidade = 10
cursor.execute(""" UPDATE lanches SET quantidade = ? WHERE id = ? """, (quantidade, id))

id = 5
quantidade = 10
cursor.execute(""" UPDATE lanches SET quantidade = ? WHERE id = ? """, (quantidade, id))

#DELETANDO DADOS DA TABELA
def delete(id):
	cursor.execute(""" DELETE FROM lanches WHERE id = ? """, (id, ))
delete(3)

#LENDO OS DADOS DA TABELA
def select():
	cursor.execute(""" SELECT * FROM lanches """)
select()
for linha in cursor.fetchall():
    print(linha)

conn.commit()
print("Sucesso!")

conn.close()