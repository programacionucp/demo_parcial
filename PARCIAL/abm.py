import json

with open('diputados.json', encoding = 'utf-8') as file:
    listaDiputados = json.load(file)

def guardarDiputados():
    with open('diputados','w') as archivo:
        json.dump(listaDiputados,archivo)

with open('viajes.json', encoding = 'utf-8') as file:
    listaViajes = json.load(file)

def guardarViajes():
    with open('viajes','w') as archivo:
        json.dump(listaViajes,archivo)
