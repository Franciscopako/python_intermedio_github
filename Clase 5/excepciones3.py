# Actividad excepciones
# Replicar el comportamiento de creacion de carpetas con Windows
# al crear un directorio si ya existe agregarle entre parentesis el consecutivo
# carpeta
# carpeta(1)
# carpeta(2)

import os

os.system('cls')

Path="C:\\python_intermedio_github\\"
NomDir="Nueva_Carpeta"
Lista=os.listdir(Path)
Lista2=[]
for Contador in range(len(Lista)):
    if str(Lista[Contador]).find(NomDir)==0:
        ParteNumero=str(Lista[Contador])[len(NomDir):len(str(Lista[Contador]))]
        if (ParteNumero.isnumeric()): Lista2.append(ParteNumero) # Determina el ultimo               
if Lista2==[]:
   os.makedirs(Path+NomDir+"1") # Crea el primero si no existe
else:
   os.makedirs(Path+NomDir+str(int(max(Lista2))+1)) # Crea el siguiente