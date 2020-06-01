from tkinter import *

vp = Tk()
vp.geometry("900x650")
vp.title("Sistema Diputados")

#primera opcion
l1 = Label(vp, text="Cantidad de diputados por provincia ",font=("Arial",12)).place(x=10,y=10)
l2 = Label(vp, text="Provincia:",font=("Arial",12)).place(x=10,y=60)
e1 = Entry(vp, width=15)
e1.place(x=100,y=60)
btn1 = Button(vp, text="Calcular", font=("Arial",12)).place(x=250,y=55)
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



vp,mainloop()
