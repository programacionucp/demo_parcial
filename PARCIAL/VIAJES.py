import json


with open('viajes.json', encoding = 'utf-8') as file:
    listaViajes = json.load(file)


def getListaDatos():
    return listaViajes
