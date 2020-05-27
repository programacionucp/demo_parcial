import json


with open('covid19.json', encoding = 'utf-8') as file:
    listaDatosCovid19 = json.load(file)


def getListaDatos():
    return listaDatosCovid19
