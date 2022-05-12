import os


def crear_carpetas(sufijo, cantidad):
    """
    Crear N numero de carpetas
    """
    for i in range(cantidad):
        os.mkdir(f"{sufijo}{i}")
        print(f"Creando carpeta {sufijo}{i}")