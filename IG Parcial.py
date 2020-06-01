from tkinter import *
import abmDiputados

def CantidadDeDiputados():
    provincia = e1.get()
    info = abmDiputados.CantidadDiputados(provincia)
    print(info)



vp = Tk()
vp.geometry("900x650")
vp.title("Sistema Diputados")

#primera opcion
l1 = Label(vp, text="Cantidad de diputados por provincia ",font=("Arial",12)).place(x=10,y=10)
l2 = Label(vp, text="Provincia:",font=("Arial",12)).place(x=10,y=60)
e1 = Entry(vp, width=25)
e1.place(x=90,y=60)
btn1 = Button(vp, text="Calcular", font=("Arial",12),command=CantidadDeDiputados).place(x=250,y=55)
l3 = Label(vp, text="Cantidad:",font=("Arial",12)).place(x=350,y=60)
e2 = Entry(vp, width=15)
e2.place(x=440,y=60)

#segunda opcion
l4 = Label(vp, text="Cantidad de diputados por bloque politico ",font=("Arial",12)).place(x=10,y=110)
l5 = Label(vp, text="Bloque:",font=("Arial",12)).place(x=10,y=150)
e3 = Entry(vp, width=15)
e3.place(x=80,y=150)
btn2 = Button(vp, text="Calcular", font=("Arial",12)).place(x=250,y=140)
l6 = Label(vp, text="Hombres:",font=("Arial",12)).place(x=350,y=140)
e4 = Entry(vp, width=15)
e4.place(x=440,y=140)
l7 = Label(vp, text="Mujeres:",font=("Arial",12)).place(x=350,y=180)
e5 = Entry(vp, width=15)
e5.place(x=440,y=180)

#tercera opcion
l8 = Label(vp, text="Cantidad de viajes",font=("Arial",12)).place(x=10,y=240)
l9 = Label(vp, text="Origen:",font=("Arial",12)).place(x=10,y=280)
e6 = Entry(vp, width=15)
e6.place(x=90,y=280)
l10 = Label(vp, text="Destino:",font=("Arial",12)).place(x=10,y=310)
e7 = Entry(vp, width=15)
e7.place(x=90,y=310)
btn3 = Button(vp, text="Calcular", font=("Arial",12)).place(x=250,y=290)
l11 = Label(vp, text="Cantidad:",font=("Arial",12)).place(x=350,y=290)
e8 = Entry(vp, width=15)
e8.place(x=440,y=290)

#cuarta opcion
l12 = Label(vp, text="Buscador de diputados",font=("Arial",12)).place(x=10,y=390)
l13 = Label(vp, text="Diputado ID:",font=("Arial",12)).place(x=10,y=430)
e9 = Entry(vp, width=15)
e9.place(x=150,y=430)
l14 = Label(vp, text="Nombre completo:",font=("Arial",12)).place(x=10,y=480)
e10 = Entry(vp, width=15)
e10.place(x=150,y=480)
l15 = Label(vp, text="Provincia:",font=("Arial",12)).place(x=10,y=530)
e11 = Entry(vp, width=15)
e11.place(x=150,y=530)
btn4 = Button(vp, text="Buscar", font=("Arial",12)).place(x=280,y=420)

l16 = Label(vp, text="Bloque:",font=("Arial",12)).place(x=380,y=480)
e12 = Entry(vp, width=15)
e12.place(x=520,y=480)
l17 = Label(vp, text="Año Inicio:",font=("Arial",12)).place(x=380,y=520)
e13 = Entry(vp, width=15)
e13.place(x=520,y=520)
l18 = Label(vp, text="Cantidad de viajes:",font=("Arial",12)).place(x=380,y=560)
e14 = Entry(vp, width=15)
e14.place(x=520,y=560)

vp,mainloop()
