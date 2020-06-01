#!/usr/bin/env python
# coding: utf-8

# In[102]:


from tkinter import *
from tkinter import ttk
import json

with open ('viajes.json', encoding = 'utf-8') as file:
    Lista_viajes = json.load(file)
    
with open ('diputados.json', encoding = 'utf-8') as archivo:
    Lista_diput = json.load(archivo)
                                           
#Creación Tk
ventana = Tk()
ventana.geometry('900x800+300+95')
ventana.title('Parcial')
ventana.configure(bg='light gray')

#Funciones:
def Cant_dip_x_prov():
    contador = 0
    for diputado in Lista_diput:
        if diputado[str(Lista_diput.index(diputado)+1)]['diputado_distrito']==entry_ingr_prov_var.get():
            contador+=1
    entry_cant_farm_var.set(contador)
        

#Interfaz
    #Frames:
frame_cant_dip_x_prov = Frame(ventana, width=900, height=180, relief=SUNKEN, bg='light gray', bd=3)
frame_cant_dip_x_prov.pack()
frame_cant_dip_x_bp = Frame(ventana, width=900, height=180, relief=SUNKEN, bg='light gray', bd=3)
frame_cant_dip_x_bp.pack()
frame_cant_viaj = Frame(ventana, width=900, height=180, relief=SUNKEN, bg='light gray', bd=3)
frame_cant_viaj.pack()
frame_busc_dip = Frame(ventana, width=900, height=260, relief=SUNKEN, bg='light gray', bd=3)
frame_busc_dip.pack()

    #Lbls frame1:
lbl_cant_dip_x_prov = Label(frame_cant_dip_x_prov, text='Cantidad de Diputados por Provincia', width=30, height=1, bg='light gray').place(x=1, y=0)
lbl_ingr_prov = Label(frame_cant_dip_x_prov, text='Provincia:', width=10, height=1, bg='light gray').place(x=90, y=90)
lbl_cant_dip = Label(frame_cant_dip_x_prov, text='Cantidad:', width=10, height=1, bg='light gray').place(x=590, y=90)
    #Entrys frame1:
entry_ingr_prov_var = StringVar(frame_cant_dip_x_prov)
entry_ingr_prov = Entry(frame_cant_dip_x_prov, relief=SUNKEN, bg= 'light gray', bd=3, textvariable=entry_ingr_prov_var)
entry_ingr_prov.place(x=190, y=90,width=100,height=25)
entry_cant_farm_var = StringVar(frame_cant_dip_x_prov)
entry_cant_farm = Entry(frame_cant_dip_x_prov, relief=SUNKEN, bg= 'light gray', bd=3,state=DISABLED, textvariable=entry_cant_farm_var)
entry_cant_farm.place(x=700, y=90,width=100,height=25)
    #Button frame1:
btn_calc_dip_x_prov = Button(frame_cant_dip_x_prov, text='Calcular', width=8, height=2, bg='light gray', command=Cant_dip_x_prov).place(x=390,y=90)


    #Lbls frame2:
lbl_cant_dip_x_bp = Label(frame_cant_dip_x_bp, text='Cantidad de Diputados por Bloque Político', width=35, height=1, bg='light gray').place(x=1, y=0)
lbl_bloq = Label(frame_cant_dip_x_bp, text='Bloque:', width=10, height=1, bg='light gray').place(x=90, y=90)
lbl_h = Label(frame_cant_dip_x_bp, text='Hombres:', width=10, height=1, bg='light gray').place(x=590, y=50)
lbl_m = Label(frame_cant_dip_x_bp, text='Mujeres:', width=10, height=1, bg='light gray').place(x=590, y=100)
    #Entry frame2:
entry_ingr_bloq_var = StringVar(frame_cant_dip_x_bp)
entry_ingr_bloq = Entry(frame_cant_dip_x_bp, relief=SUNKEN, bg= 'light gray', bd=3, textvariable=entry_ingr_bloq_var)
entry_ingr_bloq.place(x=190, y=90,width=100,height=25)
entry_cant_h_var = StringVar(frame_cant_dip_x_bp)
entry_cant_h = Entry(frame_cant_dip_x_bp, relief=SUNKEN, bg= 'light gray', bd=3,state=DISABLED, textvariable=entry_cant_h_var)
entry_cant_h.place(x=700, y=50,width=100,height=25)
entry_cant_m_var = StringVar(frame_cant_dip_x_bp)
entry_cant_m = Entry(frame_cant_dip_x_bp, relief=SUNKEN, bg= 'light gray', bd=3,state=DISABLED, textvariable=entry_cant_m_var)
entry_cant_m.place(x=700, y=100,width=100,height=25)
    #Button frame2:
btn_calc_dip_x_bp = Button(frame_cant_dip_x_bp, text='Calcular', width=8, height=2, bg='light gray').place(x=390,y=90)


    #Lbls frame3:
lbl_cant_viajes = Label(frame_cant_viaj, text='Cantidad de Viajes', width=35, height=1, bg='light gray').place(x=1, y=0)
lbl_orig = Label(frame_cant_viaj, text='Origen:', width=10, height=1, bg='light gray').place(x=90, y=70)
lbl_destin = Label(frame_cant_viaj, text='Destino:', width=10, height=1, bg='light gray').place(x=90, y=130)
lbl_cant_viaj = Label(frame_cant_viaj, text='Cantidad:', width=10, height=1, bg='light gray').place(x=590, y=100)
    #Entry frame3:
entry_ingr_orig_var = StringVar(frame_cant_viaj)
entry_ingr_orig = Entry(frame_cant_viaj, relief=SUNKEN, bg= 'light gray', bd=3, textvariable=entry_ingr_orig_var)
entry_ingr_orig.place(x=190, y=70,width=100,height=25)
entry_ingr_dest_var = StringVar(frame_cant_viaj)
entry_ingr_dest = Entry(frame_cant_viaj, relief=SUNKEN, bg= 'light gray', bd=3, textvariable=entry_ingr_dest_var)
entry_ingr_dest.place(x=190, y=130,width=100,height=25)
entry_cant_viaj_var = StringVar(frame_cant_viaj)
entry_cant_viaj = Entry(frame_cant_viaj, relief=SUNKEN, bg= 'light gray', bd=3,state=DISABLED, textvariable=entry_cant_viaj_var)
entry_cant_viaj.place(x=700, y=100,width=100,height=25)
    #Button frame3
btn_calc_viaj = Button(frame_cant_viaj, text='Calcular', width=8, height=2, bg='light gray').place(x=390,y=90)


    #Lbls frame4:
lbl_busc_dip = Label(frame_busc_dip, text='Buscador de Diputados', width=35, height=1, bg='light gray').place(x=1, y=0)
lbl_dip_id = Label(frame_busc_dip, text='Diputado ID:', width=10, height=1, bg='light gray').place(x=90, y=70)
lbl_nom_com= Label(frame_busc_dip, text='Nombre Completo:', width=20, height=1, bg='light gray').place(x=90, y=130)
lbl_prov= Label(frame_busc_dip, text='Provincia:', width=10, height=1, bg='light gray').place(x=90, y=180)
lbl_cant_viaj_f4= Label(frame_busc_dip, text='Cantidad de Viajes', width=20, height=1, bg='light gray').place(x=90, y=230)
lbl_bloq_dip= Label(frame_busc_dip, text='Bloque:', width=10, height=1, bg='light gray').place(x=590, y=70)
lbl_añ_in = Label(frame_busc_dip, text='Año Inicio:', width=15, height=1, bg='light gray').place(x=590, y=130)

    #Entry frame4:
entry_ingr_dip_id_var = StringVar(frame_busc_dip)
entry_ingr_dip_id = Entry(frame_busc_dip, relief=SUNKEN, bg= 'light gray', bd=3, textvariable=entry_ingr_dip_id_var)
entry_ingr_dip_id.place(x=190, y=70,width=100,height=25)
entry_nom_com_var = StringVar(frame_busc_dip)
entry_nom_com = Entry(frame_busc_dip, relief=SUNKEN, bg= 'light gray', bd=3, state=DISABLED, textvariable=entry_nom_com_var)
entry_nom_com.place(x=250, y=130,width=100,height=25)
entry_prov_var = StringVar(frame_busc_dip)
entry_prov = Entry(frame_busc_dip, relief=SUNKEN, bg= 'light gray', bd=3,state=DISABLED, textvariable=entry_prov_var)
entry_prov.place(x=200, y=180,width=100,height=25)
entry_cant_viaj_f4_var = StringVar(frame_busc_dip)
entry_cant_viaj_f4 = Entry(frame_busc_dip, relief=SUNKEN, bg= 'light gray', bd=3, state=DISABLED, textvariable=entry_cant_viaj_f4_var)
entry_cant_viaj_f4.place(x=250, y=225,width=100,height=25)
entry_bloq_dip_var = StringVar(frame_busc_dip)
entry_bloq_dip = Entry(frame_busc_dip, relief=SUNKEN, bg= 'light gray', bd=3,state=DISABLED, textvariable=entry_bloq_dip_var)
entry_bloq_dip.place(x=700, y=70,width=100,height=25)
entry_añ_in_var = StringVar(frame_busc_dip)
entry_añ_in = Entry(frame_busc_dip, relief=SUNKEN, bg= 'light gray', bd=3,state=DISABLED, textvariable=entry_añ_in_var)
entry_añ_in.place(x=725, y=130,width=100,height=25)

    #Button frame4
btn_calc_viaj = Button(frame_busc_dip, text='Calcular', width=8, height=2, bg='light gray').place(x=435,y=70)

ventana.mainloop()

