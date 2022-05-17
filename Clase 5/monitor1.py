#ejemplo de uso de paquete de python
#psutil
#https://psutil.reagthedics.io/en/latest/

import psutil

# nucles del cpu

cpu_nucleos = psutil.cpu_count()

cpu_frecuencia = psutil.cpu_freq()

print("información del sistema")
print("Nucleos del CPU =>", cpu_nucleos)
print("Frecuencia del CPU => ", cpu_frecuencia)
