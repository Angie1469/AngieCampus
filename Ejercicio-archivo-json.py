import json
import os



data = {}
data['jugadores'] = []


while True:
    nombre = input("Ingrese el nombre del jugador:")
    edad = int(input("Ingrese la edad del jugador"))
    peso = float(input("ingrese el peso del jugador"))

    data['jugadores'].append({
        'nombre':nombre,
        'edad': edad,
        'peso':peso,
        })
    op = input("desea continuar?")
    if op.lower()== "no":
        break


with open('jugadores.json','w') as file:
    json.dump(data, file, indent=4)