import json

with open('diputados.json', encoding="utf-8") as archivodipu:
    listadiputados = json.load(archivodipu)

with open('viajes.json', encoding="utf-8") as archivoviaje:
    listaviajes = json.load(archivoviaje)

def getDiputados():
    return listadiputados

def getViajes():
    return listaviajes

def CantidadDiputados(nombre):
    cantidadDiputados = 0
    for unDiputado in listadiputados:
        infoDiputado = unDiputado["1"]
        while infoDiputado==nombre:
            cantidadDiputados += 1
    return cantidadDiputados
