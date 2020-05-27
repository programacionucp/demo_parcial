import tkinter as tk
import tkinter.messagebox
import json
window = tk.Tk() #creo una instansia y lo asignamos a una variable
window.title("Programa Rompe")#creo el titulo de mi ventana
window.geometry('550x500')#le doy dimanciones a la ven
with open('covid19.json', encoding='utf-8') as archivoRompe:
    lst_Rompe= json.load(archivoRompe)
def Buscar_confirmados():
    confirmados=0
    pais=""
    muertos=0
    recuperados=""
    for datos in lst_Rompe:
        if datos['pais']=="Argentina":
            if int(datos['confirmados'])>=int(confirmados):

                confirmados=datos['confirmados']
                pais=datos['pais']
                muertos=datos['muertos']
                recuperados=datos['recuperados']


        if datos['pais']=="Paraguay":
            if int(datos['confirmados'])>=int(confirmados):
                confirmados=datos['confirmados']
                pais = datos['pais']
        if datos['pais']=="Brazil":
            if int(datos['confirmados'])>=int(confirmados):
                confirmados=datos['confirmados']
                pais=datos['pais']
        if datos['pais']=="Uruguay":
            if int(datos['confirmados'])>=int(confirmados):
                confirmados=datos['confirmados']
                pais = datos['pais']
    ent1_5.insert(0,pais)
    ent1_6.insert(0,confirmados)
et1_1=tk.Label(window,text= "Visualizacion de informacion por paises:")#etiqueta del
et1_1.place(x=0, y=0)

################################################################################
for elementos in lst_Rompe:
    if elementos['pais']=="Argentina":
        tk.Label(window,text=elementos['pais']+"\n Confirmados: "+elementos['confirmados']+"\n Muertos: "+elementos['muertos']+"\n Recuperados: "+elementos['recuperados']).place(x=0,y=20)
    if elementos['pais']=="Brazil":
        tk.Label(window,text=elementos['pais']+"\n Confirmados: "+elementos['confirmados']+"\n Muertos: "+elementos['muertos']+"\n Recuperados: "+elementos['recuperados']).place(x=120,y=20)
    if elementos['pais']=="Paraguay":
        tk.Label(window,text=elementos['pais']+"\n Confirmados: "+elementos['confirmados']+"\n Muertos: "+elementos['muertos']+"\n Recuperados: "+elementos['recuperados']).place(x=250,y=20)
    if elementos['pais']=="Uruguay":
        tk.Label(window,text=elementos['pais']+"\n Confirmados: "+elementos['confirmados']+"\n Muertos: "+elementos['muertos']+"\n Recuperados: "+elementos['recuperados']).place(x=360,y=20)

#################################################################################
et1_6=tk.Label(window,text= "Persona Confirmadas")#etiqueta del
et1_6.place(x=0, y=100)
et1_7=tk.Label(window,text= "Pais")#etiqueta del
et1_7.place(x=0, y=170)
et1_8=tk.Label(window,text= "Dia")#etiqueta del
et1_8.place(x=0, y=190)
ent1_7= tk.Entry(window,width=13)  # boton "sigueinte", al darle click llama a la funcion(operacion_inicio)para los demas datos
ent1_7.place(x=30, y=170)
ent1_8= tk.Entry(window,width=13)  # boton "sigueinte", al darle click llama a la funcion(operacion_inicio)para los demas datos
ent1_8.place(x=30, y=190)

#################################################################################
def Buscar_datos():
    pais=str(ent1_7.get())
    Dia=int(ent1_8.get())
    confirmado=0
    muertos=0
    recuperados=0
    for datos in lst_Rompe:
        if pais==datos['pais']:
            if Dia==int(datos['dia']):
                tk.Label(window, text= "Confirmados: " + datos['confirmados'] + "\n Muertos: " +
                                     datos['muertos'] + "\n Recuperados: " + datos['recuperados']).place(x=250,y=170)

buscar1= tk.Button(window, text="Buscar",command=Buscar_confirmados)  # boton "sigueinte", al darle click llama a la funcion(operacion_inicio)para los demas datos
buscar1.place(x=150, y=100)
buscar2= tk.Button(window, text="Buscar",command=Buscar_datos)  # boton "sigueinte", al darle click llama a la funcion(operacion_inicio)para los demas datos
buscar2.place(x=150, y=170)
ent1_5= tk.Entry(window,width=13)  # boton "sigueinte", al darle click llama a la funcion(operacion_inicio)para los demas datos
ent1_5.place(x=260, y=100)
ent1_6= tk.Entry(window,width=13)  # boton "sigueinte", al darle click llama a la funcion(operacion_inicio)para los demas datos
ent1_6.place(x=260, y=120)
window.mainloop()