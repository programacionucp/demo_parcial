import tkinter as tk
import tkinter.messagebox
import json
window = tk.Tk() #creo una instansia y lo asignamos a una variable
window.title("Programa Rompe")#creo el titulo de mi ventana
window.geometry('550x500')#le doy dimanciones a la ven
with open('diputados.json', encoding='utf-8') as archivoRompe:
    lst_diputados= json.load(archivoRompe)
with open('viajes.json', encoding='utf-8') as archivoRompe:
    lst_viajes= json.load(archivoRompe)
def calcular_algo():
    id=0
    PROVINCIA = str(ent1_1.get())
    for datos in lst_diputados:
        if datos[str(lst_diputados.index(datos) + 1)]["diputado_distrito"] == PROVINCIA:
            id += 1
    ent1_2.insert(0,id)
def calcular_algo_2():
    id = 0
    bloque = str(ent1_3.get())
    for datos in lst_diputados:
        if datos[str(lst_diputados.index(datos) + 1)]["diputado_bloque"] == bloque:
            if  datos[str(lst_diputados.index(datos) + 1)]["diputado_genero"]=="F":
                id +=1
                ent1_5.insert(0, id)
            else:
                id += 1
                ent1_4.insert(0, id)
def calcular_algo_3():
    id = 0
    Origen = str(ent1_6.get())
    destino= str(ent1_7.get())
    for datos in lst_viajes:
        if datos[str(lst_viajes.index(datos) + 1)]["Origen_ciudad"] == Origen and datos[str(lst_viajes.index(datos) + 1)]["Destino_ciudad"]==destino:
            id +=1
    ent1_8.insert(0, id)
def calcular_algo_4():
    id = 0
    ID = str(ent1_9.get())
    for datos in lst_diputados:
        if datos[str(lst_diputados.index(datos) + 1)]["\ufeffdiputado_id"]==ID:
            ent1_13.insert(0,datos[str(lst_diputados.index(datos) + 1)]["diputado_bloque"])
            ent1_11.insert(0,datos[str(lst_diputados.index(datos) + 1)]["diputado_distrito"])
            ent1_14.insert(0,datos[str(lst_diputados.index(datos) + 1)]["mandato_inicio"])
            ent1_10.insert(0, datos[str(lst_diputados.index(datos) + 1)]["diputado_nombre"]+datos[str(lst_diputados.index(datos) + 1)]["diputado_apellido"])
    for datos in lst_viajes:
        if datos[str(lst_viajes.index(datos) + 1)]["\ufeffPersona_id"] == ID:
            id+=1
    ent1_12.insert(0,id)
et1_1=tk.Label(window,text= "Cantidad de diputados por provincia")#etiqueta del
et1_1.place(x=0, y=10)
et1_2=tk.Label(window,text= "Provincia")#etiqueta del
et1_2.place(x=0, y=30)
et1_3=tk.Label(window,text= "Cantidad")#etiqueta del
et1_3.place(x=200, y=30)
et1_4=tk.Label(window,text= "Cantidad de diputados por bloque politico")#etiqueta del
et1_4.place(x=0, y=60)
et1_5=tk.Label(window,text= "Bloque")#etiqueta del
et1_5.place(x=0, y=80)
et1_6=tk.Label(window,text= "Hombre")#etiqueta del
et1_6.place(x=200, y=80)
et1_7=tk.Label(window,text= "Mujer")#etiqueta del
et1_7.place(x=200, y=100)
et1_8=tk.Label(window,text= "Cantidad de viajes")#etiqueta del
et1_8.place(x=0, y=130)
et1_9=tk.Label(window,text= "Origen")#etiqueta del
et1_9.place(x=0, y=150)
et1_10=tk.Label(window,text= "Destino")#etiqueta del
et1_10.place(x=0, y=170)
et1_11=tk.Label(window,text= "Cantidad")#etiqueta del
et1_11.place(x=200, y=150)
et1_12=tk.Label(window,text= "Buscador de diputados")#etiqueta del
et1_12.place(x=0, y=190)
et1_13=tk.Label(window,text= "diputado id")#etiqueta del
et1_13.place(x=0, y=210)
et1_14=tk.Label(window,text= "Nombre completo")#etiqueta del
et1_14.place(x=0, y=230)
et1_15=tk.Label(window,text= "Provincia")#etiqueta del
et1_15.place(x=0, y=250)
et1_16=tk.Label(window,text= "Cantidad de viajes")#etiqueta del
et1_16.place(x=0, y=270)
et1_17=tk.Label(window,text= "BLOQUE")#etiqueta del
et1_17.place(x=260, y=210)
et1_18=tk.Label(window,text= "AÑO DE INICIO")#etiqueta del
et1_18.place(x=260, y=230)
###############################
ent1_1= tk.Entry(window,width=13) #provincia
ent1_1.place(x=60, y=30)
ent1_1.insert(0,"provincia")
ent1_2= tk.Entry(window,width=13) #cantidad
ent1_2.place(x=260, y=30)
ent1_3= tk.Entry(window,width=13) #bloque
ent1_3.place(x=60, y=80)
ent1_4= tk.Entry(window,width=13) #hombre
ent1_4.place(x=260, y=80)
ent1_5= tk.Entry(window,width=13) #mujer
ent1_5.place(x=260, y=100)
ent1_6= tk.Entry(window,width=13) #origen
ent1_6.place(x=60, y=150)
ent1_7= tk.Entry(window,width=13) #destino
ent1_7.place(x=60, y=170)
ent1_8= tk.Entry(window,width=13) #cantidad
ent1_8.place(x=260, y=150)
ent1_9= tk.Entry(window,width=13) #DIPURTADOID
ent1_9.place(x=110, y=210)
ent1_10= tk.Entry(window,width=13) #NOMBRE
ent1_10.place(x=110, y=230)
ent1_11= tk.Entry(window,width=13) #PROV
ent1_11.place(x=110, y=250)
ent1_12= tk.Entry(window,width=13) #CANTIDAD
ent1_12.place(x=110, y=270)
ent1_13= tk.Entry(window,width=13) #BLOQUE
ent1_13.place(x=350, y=210)
ent1_14= tk.Entry(window,width=13) #AÑO INICIO
ent1_14.place(x=350, y=230)
##################################
calcular1= tk.Button(window, text="Cargar",command=calcular_algo)  # boton "sigueinte", al darle click llama a la funcion(operacion_inicio)para los demas datos
calcular1.place(x=150, y=30)
calcular2= tk.Button(window, text="Cargar",command=calcular_algo_2)  # boton "sigueinte", al darle click llama a la funcion(operacion_inicio)para los demas datos
calcular2.place(x=150, y=80)
calcular3= tk.Button(window, text="Cargar",command=calcular_algo_3)  # boton "sigueinte", al darle click llama a la funcion(operacion_inicio)para los demas datos
calcular3.place(x=150, y=150)
calcular3= tk.Button(window, text="Cargar",command=calcular_algo_4)  # boton "sigueinte", al darle click llama a la funcion(operacion_inicio)para los demas datos
calcular3.place(x=200, y=210)
window.mainloop()