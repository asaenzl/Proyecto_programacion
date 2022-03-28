# Nombre: Angelica Saenz Lacayo
#
# Objetivos:
# 1.Hacer un menu.

#Menu: funcion para hacer menu
import random


def menu():
    print("[1] Lista de emparejamiento")
    print("[2] Ordenar jugadores")
    print("[3] Lista inicial de jugadores")
    print("[4] Lista de cada division")
    print("[5] Jugador con mayor division y puntuacion")
    print("[6] Jugador con menor division y puntuacion")
    print("[7] Promedio por division")
    print("[8] Promedio de puntuación dada una división")
    print("[9] Promedio de puntuación de todas las divisiones")
    print("[10] Cantidad de jugadores por división")
    print("[11] Cantidad de jugadores totales")
    print("[0] Salir del programa")

#tamano de la lista
lista = 10
def generarlist():
    # Generando lista de floats
    lista_de_jugadores = random.sample(range(4, 90), lista)
    float_list = [x / 10 for x in lista_de_jugadores]
    print(sorted(float_list, reverse=True))
    print("Tamano de la lista: ", len(float_list))




menu()
opcion = int(input("Digite alguna opcion: "))

while opcion != 0 :
    if opcion == 1:
        generarlist()
    elif opcion == 2:
        print("Eligion opcion 2")
    elif opcion == 3:
        print("Eligio opcion 3")
    elif opcion == 4:
        print("Eligio opcion 4")
    elif opcion == 5:
        print("Eligio opcion 5")
    elif opcion == 6:
        print("Eligio opcion 6")
    elif opcion == 7:
        print("Eligio opcion 7")
    elif opcion == 8:
        print("Eligio opcion 8")
    elif opcion == 9:
        print("Eligio opcion 9")
    elif opcion == 10:
        print("Eligio opcion 10")
    elif opcion == 11:
        print("Eligio opcion 11")
    else:
        print("Opcion invalida")

    print()
    menu()
    opcion = int(input("Digite alguna opcion: "))

print("Gracias por usar el programa")


