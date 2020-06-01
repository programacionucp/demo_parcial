from tkinter import*
from tkinter import ttk
import json

with open('diputados.json', encoding = 'utf-8') as file:
    lst_diputados = json.load(file)

with open('viajes.json', encoding = 'utf-8') as file:
    lst_viajes = json.load(file)

#funciones
def provincias():
    global lst_prov
    global lst_dip
    lst_prov = list()
    lst_dip = list()
    for un_dipu in lst_diputados:
        print(un_dipu)

ventana = Tk()
ventana.title('Parcial programacion')
ventana.geometry('900x500')
ventana.resizable(0,0)

#Label Fijo(NO TOCAR)
Label(ventana, text="Cantidad de diputados por provincia", font="Arial").place(x=10, y=10)
Label(ventana, text="Provincia:", font="Arial").place(x=10, y=50)
Label(ventana, text="Cantidad:", font="Arial").place(x=400, y=50)
Label(ventana, text="Cantidad de diputados por bloque politico", font="Arial").place(x=10, y=100)
Label(ventana, text="Bloque:", font="Arial").place(x=10, y=140)
Label(ventana, text="Hombres:", font="Arial").place(x=400, y=125)
Label(ventana, text="Mujeres:", font="Arial").place(x=400, y=155)
Label(ventana, text="Cantidad de viajes", font="Arial").place(x=10, y=180)
Label(ventana, text="Origen:", font="Arial").place(x=10, y=210)
Label(ventana, text="Destino:", font="Arial").place(x=10, y=240)
Label(ventana, text="Cantidad:", font="Arial").place(x=400, y=220)
Label(ventana, text="Buscador de diputados", font="Arial").place(x=10, y=280)
Label(ventana, text="Diputado ID:", font="Arial").place(x=10, y=310)
Label(ventana, text="Nombre Completo:", font="Arial").place(x=10, y=340)
Label(ventana, text="Provincia:", font="Arial").place(x=10, y=370)
Label(ventana, text="Cantidad de viajes", font="Arial").place(x=10, y=400)
Label(ventana, text="Bloque:", font="Arial").place(x=500, y=310)
Label(ventana, text="Año de inicio:", font="Arial").place(x=500, y=340)



#Labels Cambiantes
global lbl_cantidad
global lbl_hombres
global lbl_mujeres
global lbl_cantidad2
global lbl_nombre
global lbl_provincia
global lbl_viajes
global lbl_bloque
global lbl_año
lbl_cantidad = Label(ventana, text="--", font="Arial", borderwidth=2, width=10, relief="ridge").place(x=500, y=50)
lbl_hombres = Label(ventana, text="--", font="Arial", borderwidth=2, width=10, relief="ridge").place(x=500, y=125)
lbl_mujeres = Label(ventana, text="--", font="Arial", borderwidth=2, width=10, relief="ridge").place(x=500, y=155)
lbl_cantidad2 = Label(ventana, text="--", font="Arial", borderwidth=2, width=10, relief="ridge").place(x=500, y=220)
lbl_nombre = Label(ventana, text="--", font="Arial", borderwidth=2, width=33, relief="ridge").place(x=180, y=340)
lbl_provincia = Label(ventana, text="--", font="Arial", borderwidth=2, width=33, relief="ridge").place(x=180, y=370)
lbl_viajes = Label(ventana, text="--", font="Arial", borderwidth=2, width=33, relief="ridge").place(x=180, y=400)
lbl_bloque = Label(ventana, text="--", font="Arial", borderwidth=2, width=25, relief="ridge").place(x=620, y=310)
lbl_año = Label(ventana, text="--", font="Arial", borderwidth=2, width=25, relief="ridge").place(x=620, y=340)

#Interactivo
    #Combo
combo1 = ttk.Combobox(ventana, width=25)
combo1.configure(value=provincias())
combo1.place(x=100, y=50)
combo2 = ttk.Combobox(ventana, width=25)
combo2.place(x=100, y=140)
combo3 = ttk.Combobox(ventana, width=25)
combo3.place(x=100, y=210)
combo3 = ttk.Combobox(ventana, width=25)
combo3.place(x=100, y=240)
    #Entry
ent_nombre = Entry(ventana, width=30)
ent_nombre.place(x=115, y=313)
    #Botones
btn_calcular = Button(ventana, text="Calcular", font="Arial", cursor="hand2").place(x=300, y=45)
btn_calcular2 = Button(ventana, text="Calcular", font="Arial", cursor="hand2").place(x=300, y=135)
btn_calcular3 = Button(ventana, text="Calcular", font="Arial", cursor="hand2").place(x=300, y=220)
btn_buscar = Button(ventana, text="Buscar", font="Arial", cursor="hand2").place(x=340, y=305)

provincias()

ventana.mainloop()