import json


with open('diputados.json', encoding = 'utf-8') as file:
    listaDiputados = json.load(file)


def getListaDatos():
    return listaDiputados
