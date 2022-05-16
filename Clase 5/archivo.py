# practica de manipulacion de archivo con python
#open

archivo= open("texto.txt","w")

archivo.write("Hola \n")
archivo.write("mundo")

archivo.close()
print("Termino la manipulación de archivos")