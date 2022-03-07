# Nombre: Angelica Saenz Lacayo
#
# Objetivos:
# 1. Hacer una rutina que genere aleatoriamente una lista de diez numeros flotantes que representen diez jugadores.
# 2. Hacer una rutina que reciba el numero del jugadores, y muestre la division a la cual pertence

import random

lista = 10

lista_de_jugadores = random.sample(range(5, 100), lista)
float_list = [x/10 for x in lista_de_jugadores]
print(float_list)
print("Tamano de la lista: ", len(float_list))

for jugador in float_list:
    if 0 <= jugador <= 0.99:
        print("Division Hierro")
        print("-" * 40)
    elif 1 <= jugador <= 1.99:
        print("Division Bronce")
        print("-" * 40)
    elif 2 <= jugador <= 2.99:
        print("Division Plata")
        print("-" * 40)
    elif 3 <= jugador <= 3.99:
        print("Division Oro")
        print("-" * 40)
    elif 4 <= jugador <= 4.99:
        print("Division Platino")
        print("-" * 40)
    elif 5 <= jugador <= 5.99:
        print("Division Diamante")
        print("-" * 40)
    elif 6 <= jugador <= 6.99:
        print("Division Maestro")
        print("-" * 40)
    elif 7 <= jugador <= 7.99:
        print("Division Gran Maestro")
        print("-" * 40)
    elif 8 <= jugador <= 8.99:
        print("Division Retador")
        print("-" * 40)
    else:
        print("No pertenece a ninguna division")

print("Estos son las divisiones")