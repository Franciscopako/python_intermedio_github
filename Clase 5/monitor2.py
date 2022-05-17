# pasar todo lo del monitor 1 a un archivo de texto
# crear una carpeta donde se almacenaran los logs 
# crear un archivo con X nombre 
# insertar la informacion recabada en el archivo
import psutil
import os


cpu_nucleos = psutil.cpu_count()
cpu_frecuencia = psutil.cpu_freq()
memoria_virtual = psutil.virtual_memory()
disco_uso = psutil.disk_usage('/')

os.system('cls')
print("="*50)

os.mkdir("Almacena_log")

with open("Almacena_log\system.txt","w") as archivo:
    archivo.write(f"nucleo de CPU :{cpu_nucleos}\n")
    archivo.write(f"Frecuencia de CPU :{cpu_frecuencia}\n")
    archivo.write(f"Memorias del CPU :{memoria_virtual}\n")
    archivo.write(f"Disco del CPU :{disco_uso}")

