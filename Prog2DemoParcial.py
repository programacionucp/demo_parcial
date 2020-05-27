from tkinter import *
import abmCovid19

def MostrarDatosdePaises():
    entrada = e13.get()
    info = abmCovid19.Paises(entrada)
    if entrada == "Argentina":
        e1.insert(END, info["confirmados"])
        e2.insert(END, info["muertos"])
        e3.insert(END, info["recuperados"])
    if entrada=="Paraguay":
        e4.insert(END, info["confirmados"])
        e5.insert(END, info["muertos"])
        e6.insert(END, info["recuperados"])
    if entrada=="Uruguay":
        e7.insert(END, info["confirmados"])
        e8.insert(END, info["muertos"])
        e9.insert(END, info["recuperados"])
    if entrada=="Brazil":
        e10.insert(END, info["confirmados"])
        e11.insert(END, info["muertos"])
        e12.insert(END, info["recuperados"])





vp = Tk()
vp.geometry("1200x600")
vp.title("Datos del Covid-19")

#vuzualizacion de los paises
l1 = Label(vp, text="Visulizar informacion por paises", font=("arial",11)).place(x=10, y=0)

l2 = Label(vp, text="Argentina", font=("arial",12)).place(x=50,y=50)
l3 = Label(vp, text="Confirmados:", font=("arial",11)).place(x=10,y=90)
e1 = Entry(vp, width=20)
e1.place(x=120,y=90)
l4 = Label(vp, text="Fallecidos:", font=("arial",11)).place(x=10,y=130)
e2 = Entry(vp, width=20)
e2.place(x=120,y=130)
l5 = Label(vp, text="Recuperdos:", font=("arial",11)).place(x=10,y=170)
e3 = Entry(vp, width=20)
e3.place(x=120,y=170)

l6 = Label(vp, text="Paraguay", font=("arial",12)).place(x=350,y=50)
l7 = Label(vp, text="Confirmados:", font=("arial",11)).place(x=290,y=90)
e4 = Entry(vp, width=20)
e4.place(x=400,y=90)
l8 = Label(vp, text="Fallecidos:", font=("arial",11)).place(x=290,y=130)
e5 = Entry(vp, width=20)
e5.place(x=400,y=130)
l9 = Label(vp, text="Recuperdos:", font=("arial",11)).place(x=290,y=170)
e6 = Entry(vp, width=20)
e6.place(x=400,y=170)

l10 = Label(vp, text="Uruguay", font=("arial",12)).place(x=650,y=50)
l11 = Label(vp, text="Confirmados:", font=("arial",11)).place(x=570,y=90)
e7 = Entry(vp, width=20)
e7.place(x=680,y=90)
l12 = Label(vp, text="Fallecidos:", font=("arial",11)).place(x=570,y=130)
e8 = Entry(vp, width=20)
e8.place(x=680,y=130)
l13 = Label(vp, text="Recuperdos:", font=("arial",11)).place(x=570,y=170)
e9 = Entry(vp, width=20)
e9.place(x=680,y=170)

l14 = Label(vp, text="Brasil", font=("arial",12)).place(x=930,y=50)
l15 = Label(vp, text="Confirmados:", font=("arial",11)).place(x=840,y=90)
e10 = Entry(vp, width=20)
e10.place(x=950,y=90)
l16 = Label(vp, text="Fallecidos:", font=("arial",11)).place(x=840,y=130)
e11 = Entry(vp, width=20)
e11.place(x=950,y=130)
l17 = Label(vp, text="Recuperdos:", font=("arial",11)).place(x=840,y=170)
e12 = Entry(vp, width=20)
e12.place(x=950,y=170)

#btn1 = Button(vp, text="Mostrar", font=("arial",12)).place(x=1100, y=120)

#mostrar pais con mas recuperado
l18 = Label(vp, text="Pais con mas Recuperdos:", font=("arial",11)).place(x=10,y=270)
btn2 = Button(vp, text="Buscar", font=("arial",12),command=MostrarDatosdePaises).place(x=260, y=265)
l19 = Label(vp, text="Pais:", font=("arial",11)).place(x=410,y=250)
e13 = Entry(vp, width=20)
e13.place(x=500, y=250)
l20 = Label(vp, text="Cantidad:", font=("arial",11)).place(x=410,y=290)
e14 = Entry(vp, width=20)
e14.place(x=500, y=290)

#buscador
l21 = Label(vp, text="Buscador", font=("arial",11)).place(x=10,y=380)
l22 = Label(vp, text="Pais:", font=("arial",11)).place(x=10,y=430)
e15 = Entry(vp, width=20)
e15.place(x=100, y=430)
l23 = Label(vp, text="Dia:", font=("arial",11)).place(x=10,y=480)
e16 = Entry(vp, width=20)
e16.place(x=100, y=480)
btn3 = Button(vp, text="Buscar", font=("arial",12)).place(x=260, y=430)

l24 = Label(vp, text="Comfirmados:", font=("arial",11)).place(x=400,y=420)
e17 = Entry(vp, width=20)
e17.place(x=530, y=420)
l25 = Label(vp, text="Fallecidos", font=("arial",11)).place(x=400,y=460)
e18 = Entry(vp, width=20)
e18.place(x=530, y=460)
l26 = Label(vp, text="Recuperdos", font=("arial",11)).place(x=400,y=500)
e19 = Entry(vp, width=20)
e19.place(x=530, y=500)

vp.mainloop()
