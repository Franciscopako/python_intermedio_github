#ejemplo de uso de paquete de python
#psutil
#https://psutil.reagthedics.io/en/latest/

import psutil
import os

# nucles del cpu

cpu_nucleos = psutil.cpu_count()
cpu_frecuencia = psutil.cpu_freq()

# Memoria
memoria_virtual = psutil.virtual_memory()

# disco
disco_uso = psutil.disk_usage('/')

os.system('cls')

print("="*50)

print("información del sistema")
print("Nucleos del CPU =>", cpu_nucleos)
print("Frecuencia del CPU => ", cpu_frecuencia)

print("Memoria virutal => ", memoria_virtual)

print("Uso de disco => ", disco_uso)

print("=" * 50)
