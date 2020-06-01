from tkinter import*
from tkinter import ttk

ventana = Tk()
ventana.title('Parcial programacion')
ventana.geometry('700x300')
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


#Labels Cambiantes
lbl_cantidad = Label(ventana, text="--", font="Arial", borderwidth=2, width=10, relief="ridge").place(x=500, y=50)
lbl_hombres = Label(ventana, text="--", font="Arial", borderwidth=2, width=10, relief="ridge").place(x=500, y=125)
lbl_mujeres = Label(ventana, text="--", font="Arial", borderwidth=2, width=10, relief="ridge").place(x=500, y=155)

ventana.mainloop()