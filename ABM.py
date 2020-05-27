import json #importa una libreria que tenga guardada
with open('covid19.json',encoding = 'utf-8') as archivo: #abre el archivo "su direccion" y lo inserta en la variable archivo "as archivo". "encoding utf-8" tipo de codificacion
    lstCovid19 = json.load(archivo)

def archivoJson ():
    return lstCovid19

def guardar ():
    with open ('Serie A.json',"w") as archivo :
        json.dump (lstCovid19, archivo)
