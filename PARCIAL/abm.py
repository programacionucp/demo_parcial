import json

with open('diputados.json', encoding = 'utf-8') as file:
    listaDiputados = json.load(file)


with open('viajes.json', encoding = 'utf-8') as fileViaje:
    listaViajes = json.load(fileViaje)



def diputadosPorProv(provincia): #Realizar por combobox
    listAux = list()
    i = 1
    for elemento in listaDiputados:
        i= str(i)
        if elemento[i]['diputado_distrito'] == provincia:
            if elemento[i]['diputado_nombre'] not in listAux:
                listAux.append(elemento[i]['diputado_nombre'])
        i = int(i)
        i+=1
    return len(listAux)

def diputadosBloqueGenero(bloque,genero):
    listAux = list()
    i = 1
    for elemento in listaDiputados:
        i= str(i)
        if elemento[i]['diputado_bloque'] == bloque:
             if elemento[i]['diputado_genero'] == genero:
                 if elemento[i]['diputado_nombre'] not in listAux:
                    listAux.append(elemento[i]['diputado_nombre'])
        i = int(i)
        i+=1
    return len(listAux)

#Visualizar la cantidad de viajes  por origen (“Origen_ciudad“) y por destino (“Destino_ciudad“), para lo cual se
# pide que desarrolle  una función que recibiendo como valores de parámetros un origen de viaje  (Ej. “Buenos Aires”)
# y un destino (Ej. "Misiones") retorne dicha cantidad.

def viajesPorOrigenYDestino(origen,destino):
    varAux = 0
    i = 1
    for elemento in listaViajes:
        i = str(i)
        if elemento[i]["Origen_ciudad"] == origen:
            if elemento[i]["Destino_ciudad"] == destino:
                varAux+=1
        i = int (i)
        i+=1
    return varAux

def viajesDiputados(diputado):
    varAux = 0
    i = 1
    for elemento in listaViajes:
        i = str(i)
        if diputado in elemento[i]["Persona_apellido_y_nombre"]:
            varAux+=1
        i = int (i)
        i+=1
    return varAux

def buscadorDiputados(id):
    listAux = list()
    i = 1
    año = ""
    for elemento in listaDiputados:
        i= str(i)
        if elemento[i]['﻿diputado_id'] == id:
            apellido = elemento[i]['diputado_apellido']
            nombre = elemento[i]['diputado_nombre']
            completo = apellido +" "+nombre
            listAux.append(completo)
            listAux.append(elemento[i]['diputado_distrito'])
            listAux.append(elemento[i]['diputado_bloque'])
            inicioFecha = elemento[i]['mandato_inicio']
            for e in range (4):
                año += inicioFecha[e]
            listAux.append(año)
            listAux.append(viajesDiputados(nombre.upper()))
            return listAux
        i = int (i)
        i+=1
    return None

print(buscadorDiputados("HCDN1136"))

