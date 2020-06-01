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

print(diputadosBloqueGenero("UCR","M"))
