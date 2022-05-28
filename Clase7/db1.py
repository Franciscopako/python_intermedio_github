#ejemplo de conexion a base de datos postgres
#utilizando psycopg2

import psycopg2
import os 

os.system('cls')

conn = psycopg2.connect("dbname = python_intermedio_db user = postgres password =123456")
cur = conn.cursor()

cur.execute("SELECT * FROM usuarios;")
print(cur.fetchone())

cur.close()
conn.close()
 