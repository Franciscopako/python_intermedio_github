
grado_actual= float(input("Cual es la Temperatura actual: "))


if grado_actual in range(25,30):
    print( "se antoja un pozol")


elif grado_actual > 35:
    print("ta juerte la calor")

elif grado_actual < 25:
    print("es hora de sacar el sueter cucarachiento")

else :
    print("Este Grado no se encuentra")