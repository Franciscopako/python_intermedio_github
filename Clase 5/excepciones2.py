# manejo de excepcion cuando creamos un directorio
import os


try:
    os.mkdir("carpeta_prueba")
    print("se creo la carpeta")
except FileExistsError as ex:
    os.mkdir("carpeta_prueba1")
    print("Ya existe ese directorio intenta con otro nombre")
except FileNotFoundError as ex:
    print("No se encontro el directorio proporcionado")
except Exception as ex:
    print("oops ocurrio un error")

print("Fin del script")