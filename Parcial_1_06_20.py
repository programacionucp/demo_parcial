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
    variable_contador=0
    PROVINCIA=str(ent1_1.get())
    for datos in lst_diputados:
        if datos["diputado_distrito"]==PROVINCIA.upper:
            variable_contador+=1
            ent1_2.insert(0,variable_contador)
et1_1=tk.Label(window,text= "Cantidad de diputados por provincia")#etiqueta del
et1_1.place(x=0, y=10)
et1_2=tk.Label(window,text= "Provincia")#etiqueta del
et1_2.place(x=0, y=30)
et1_3=tk.Label(window,text= "Cantidad")#etiqueta del
et1_3.place(x=200, y=30)
###############################
ent1_1= tk.Entry(window,width=13) #provincia
ent1_1.place(x=60, y=30)
ent1_1.insert(0,"provincia")
ent1_2= tk.Entry(window,width=13) #cantidad
ent1_2.place(x=260, y=30)
##################################
calcular1= tk.Button(window, text="Cargar",command=calcular_algo)  # boton "sigueinte", al darle click llama a la funcion(operacion_inicio)para los demas datos
calcular1.place(x=150, y=30)
window.mainloop()