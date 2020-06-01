import json #importa una libreria que tenga guardada
with open('diputados.json',encoding = 'utf-8') as archivo: #abre el archivo "su direccion" y lo inserta en la variable archivo "as archivo". "encoding utf-8" tipo de codificacion
    lstDiputados = json.load(archivo)

with open('viajes.json',encoding = 'utf-8') as archivo: #abre el archivo "su direccion" y lo inserta en la variable archivo "as archivo". "encoding utf-8" tipo de codificacion
    lstViajes = json.load(archivo)

def archivoDiputados ():
    return lstDiputados

def archivoViajes ():
    return lstViajes
