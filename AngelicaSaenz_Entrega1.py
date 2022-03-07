#Nombre: Angelica Saenz Lacayo
#
# Objetivo: Programa que reciba un numero tipo float y muestre el nombre de la division que pertenece
#
# Variables:
#   jugador = recibe cualquier numero float
#
jugador = float(input("Ingrese el numero del jugador: "))
print(jugador)

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
