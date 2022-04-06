import random

#tamano de la lista
lista = 10

#Generando lista de floats
lista_de_jugadores = random.sample(range(4, 90), lista)
float_list = [x/10 for x in lista_de_jugadores]

valores = {'Hierro': [],
           'Bronce': [],
           'Plata': [],
           'Oro': [],
           'Platino': [],
           'Diamante': [],
           'Maestro': [],
           'Gran Maestro': [],
           "Retador": []
           }

#Asignacion de jugadores con respecto a la lista
for jugador in float_list:
    if 0 <= jugador <= 0.99:
        valores['Hierro'].append(jugador)
    elif 1 <= jugador <= 1.99:
        valores['Bronce'].append(jugador)
    elif 2 <= jugador <= 2.99:
        valores['Plata'].append(jugador)
    elif 3 <= jugador <= 3.99:
        valores['Oro'].append(jugador)
    elif 4 <= jugador <= 4.99:
        valores['Platino'].append(jugador)
    elif 5 <= jugador <= 5.99:
        valores['Diamante'].append(jugador)
    elif 6 <= jugador <= 6.99:
        valores['Maestro'].append(jugador)
    elif 7 <= jugador <= 7.99:
        valores['Gran Maestro'].append(jugador)
    elif 8 <= jugador <= 8.99:
        valores['Retador'].append(jugador)





for k, v in valores.items():
    print(k)
    print(v)
    print("-------------")

