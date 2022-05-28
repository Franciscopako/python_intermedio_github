import psycopg2
import os

os.system('cls')

conn = psycopg2.connect("dbname = python_intermedio_db user = postgres password =123456")
cur = conn.cursor()

cur.execute("SELECT * FROM usuarios ;")

usuarios_lista =cur.fetchall()
for usuario in usuarios_lista:
    print(usuario)

cur.close()
conn.close()