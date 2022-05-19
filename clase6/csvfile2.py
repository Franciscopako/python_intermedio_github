import csv
import os
import time
from tracemalloc import start

"""
with open("console_games.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #print(row["Name"], row["Platform"])
        pass
"""
start = time.time()

os.system('cls')
ruta = "C:\\python_intermedio_github\\clase6\\practica\\"

with open('console_games.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(f"plataforma => {row['Platform']} año=> {row['Year']}")
        
        try:
            if row['Platform']:
                os.makedirs(f"{ruta}{row['Platform']}\\{row['Year']}")

        except FileExistsError as ex:
            pass

        if row['Platform']:
            ruta_archivo = f"{ruta}{row['Platform']}\\{row['Year']}\\archivo.txt"
            cadena = ''

            for key, value in row.items():
                cadena += value + ","

            cadena += "\n"

            with open(ruta_archivo, 'a') as archivo:
                archivo.write(cadena)

end = time.time()

print(end - start)



