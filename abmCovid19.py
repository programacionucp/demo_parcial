import json

with open('covid19.json', encoding="utf-8") as archivocovid:
    listaPaises = json.load(archivocovid)


def getPaises():
    return listaPaises

def Paises(pais):
    for unPais in listaPaises:
        if unPais['pais']==pais:
            return unPais

