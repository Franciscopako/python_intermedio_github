with open("text2.txt") as archivo:
    print(archivo.read())

with open("texto.txt") as archivo:
    print(archivo.readline())
    print(archivo.readline())

print("="*50)

with open("carpertas.txt") as archivo:
    for linea in archivo.readlines():
        print(linea)