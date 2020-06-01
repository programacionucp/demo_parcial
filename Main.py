from tkinter import*
from tkinter import ttk
import json


root = Tk()
root.geometry('500x800')
root.resizable(0,0)

#GUI
    #Frame_Diputados_por_provincia
Dip_x_provincia = Frame(root, width=500, height=200, relief=SUNKEN, bd=20)
Dip_x_provincia.pack()
Provinc_ = Label(Dip_x_provincia, text='Provincia: ').place(x=20, y=30)
Provinc_entr_var = StringVar(Dip_x_provincia)
Provinc_entr = Entry(Dip_x_provincia, textvariable=Provinc_entr_var)
Provinc_entr.place(x=80, y=30)
Calc_btn_1 = Button(Dip_x_provincia, text='Calcular').place(x=180, y=60)
Cantidad_1_lbl = Label(Dip_x_provincia, text='Cantidad: ').place(x=400, y=60)
cantidad_1_var = StringVar(Dip_x_provincia)
Cantidad_1_entr = Entry(Dip_x_provincia, textvariable=cantidad_1_var)
Cantidad_1_entr.place(x=240, y= 60)
    #Frame_Diputados_por_Bloque_Político
Dip_x_bloque = Frame(root, width=500, height=200, relief=SUNKEN, bd=20)
Dip_x_bloque.pack()
bloque_ = Label(Dip_x_bloque, text='Bloque: ').place(x=40, y=60)
bloque_entr_var = StringVar(Dip_x_bloque)
bloque_entr = Entry(Dip_x_bloque, textvariable=bloque_entr_var)
bloque_entr.place(x=70, y=60)
Calc_btn_1 = Button(Dip_x_bloque, text='Calcular').place(x=110, y=60)
Hombres_lbl = Label(Dip_x_bloque, text='Hombres: ').place(x=180, y=60)
Mujeres_lbl = Label(Dip_x_bloque, text='Mujeres: ').place(x=180, y=80)
hombres_var = StringVar(Dip_x_bloque)
mujeres_var = StringVar(Dip_x_bloque)
hombres_entr = Entry(Dip_x_provincia, textvariable=hombres_var)
hombres_entr.place(x=240, y= 60)
mujeres_entr = Entry(Dip_x_provincia, textvariable=mujeres_var)
hombres_entr.place(x=240, y= 80)
    #Frame_Cantidad_Viajes
Cantidad_Viajes_F = Frame(root, width=500, height=200, relief=SUNKEN, bd=20)
Cantidad_Viajes_F.pack()
Origen_ = Label(Cantidad_Viajes_F, text='Origen: ').place(x=40, y=60)
Destino_ = Label(Cantidad_Viajes_F, text='Destino: ').place(x=40, y=80)
origen_var = StringVar(Cantidad_Viajes_F)
origen_entr = Entry(Cantidad_Viajes_F, textvariable=origen_var)
origen_entr.place(x=70, y=60)
destino_var = StringVar(Cantidad_Viajes_F)
destino_entr = Entry(Cantidad_Viajes_F, textvariable=destino_var)
destino_entr.place(x=70, y=80)
Calc_btn_1 = Button(Cantidad_Viajes_F, text='Calcular').place(x=110, y=60)
Cantidad_2_lbl = Label(Cantidad_Viajes_F, text='Cantidad: ').place(x=180, y=60)
cantidad_2_var = StringVar(Cantidad_Viajes_F)
Cantidad_2_entr = Entry(Cantidad_Viajes_F, textvariable=cantidad_2_var)
Cantidad_2_entr.place(x=240, y= 60)
    #Frame_Buscador_Diputados
Buscador_diputados = Frame(root, width=500, height=200, relief=SUNKEN, bd=20)
Buscador_diputados.pack()
Diputado_id = Label(Buscador_diputados, text='Diputado ID').place(x=40, y=60)
diputado_entr_var = StringVar(Buscador_diputados)
diputado_entr = Entry(Buscador_diputados, textvariable=Buscador_diputados)
diputado_entr.place(x=70, y=60)

Nombre_completo_entr_var = StringVar(Buscador_diputados)
Nombre_completo_entr = Entry(Buscador_diputados, textvariable=Buscador_diputados)
Nombre_completo_entr.place(x=70, y=60)

Provincia_buscador_entr_var = StringVar(Buscador_diputados)
Provincia_buscador_entr = Entry(Buscador_diputados, textvariable=Buscador_diputados)
Provincia_buscador_entr.place(x=70, y=60)

cantidad_viajes_2_entr_var = StringVar(Buscador_diputados)
cantidad_viajes_2_entr = Entry(Buscador_diputados, textvariable=cantidad_viajes_2_entr_var)
cantidad_viajes_2_entr.place(x=70, y=60)

bloque_2_entr_var = StringVar(Buscador_diputados)
bloque_2_entr = Entry(Buscador_diputados, textvariable=bloque_2_entr_var)
bloque_2_entr.place(x=70, y=60)

año_inicio_entr_var = StringVar(Buscador_diputados)
año_inicio_entr = Entry(Buscador_diputados, textvariable=año_inicio_entr_var)
año_inicio_entr.place(x=70, y=60)




root.mainloop()


