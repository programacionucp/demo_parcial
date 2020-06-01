#!/usr/bin/env python
# coding: utf-8

# In[61]:


from tkinter import *
from tkinter import ttk
import json

with open ('viajes.json', encoding = 'utf-8') as file:
    Lista_viajes = json.load(file)
    
with open ('diputados.json', encoding = 'utf-8') as file:
    Lista_diput = json.load(file)
                                           
#Creación Tk
ventana = Tk()
ventana.geometry('900x800+300+95')
ventana.title('Parcial')
ventana.configure(bg='light gray')

#Funciones

#Interfaz
    #Frame:
frame_cant_dip_x_prov = Frame(ventana, width=900, height=180, relief=SUNKEN, bg='black', bd=3)
frame_cant_dip_x_prov.pack()

frame_cant_dip_x_bp = Frame(ventana, width=900, height=180, relief=SUNKEN, bg='black', bd=3)
frame_cant_dip_x_bp.pack()

frame_cant_viaj = Frame(ventana, width=900, height=180, relief=SUNKEN, bg='black', bd=3)
frame_cant_viaj.pack()

frame_busc_dip = Frame(ventana, width=900, height=260, relief=SUNKEN, bg='black', bd=3)
frame_busc_dip.pack()

    #Lbls frame1:
lbl_cant_dip_x_prov = Label(frame_cant_dip_x_prov, text='Cantidad de Diputados por Provincia', width=30, height=1, bg='light gray').place(x=1, y=0)
lbl_ingr_prov = Label(frame_cant_dip_x_prov, text='Provincia:', width=10, height=1, bg='light gray').place(x=90, y=90)
lbl_cant_dip = Label(frame_cant_dip_x_prov, text='Cantidad:', width=10, height=1, bg='light gray').place(x=590, y=90)
    #Entrys frame1:
# entry_ingr_prov_var = StringVar(frame_cant_dip_x_prov)
entry_ingr_prov = Entry(frame_cant_dip_x_prov, relief=SUNKEN, bg= 'light gray', bd=3)
entry_ingr_prov.place(x=190, y=90,width=100,height=25)
# entry_cant_farm_var = StringVar(frame_cant_dip_x_prov)
entry_cant_farm = Entry(frame_cant_dip_x_prov, relief=SUNKEN, bg= 'light gray', bd=3,state=DISABLED)
entry_cant_farm.place(x=700, y=90,width=100,height=25)
    #Button frame1:
btn_calc_dip_x_prov = Button(frame_cant_dip_x_prov, text='Calcular', width=8, height=2, bg='light gray').place(x=390,y=90)


    #Lbls frame2:
lbl_cant_dip_x_bp = Label(frame_cant_dip_x_bp, text='Cantidad de Diputados por Bloque Político', width=35, height=1, bg='light gray').place(x=1, y=0)
lbl_bloq = Label(frame_cant_dip_x_bp, text='Bloque:', width=10, height=1, bg='light gray').place(x=90, y=90)
lbl_h = Label(frame_cant_dip_x_bp, text='Hombres:', width=10, height=1, bg='light gray').place(x=590, y=50)
lbl_m = Label(frame_cant_dip_x_bp, text='Mujeres:', width=10, height=1, bg='light gray').place(x=590, y=100)
    #Entry frame2:
# entry_ingr_bloq = StringVar(frame_cant_dip_x_bp)
entry_ingr_bloq = Entry(frame_cant_dip_x_bp, relief=SUNKEN, bg= 'light gray', bd=3)
entry_ingr_bloq.place(x=190, y=90,width=100,height=25)
# entry_cant_h = StringVar(frame_cant_dip_x_bp)
entry_cant_h = Entry(frame_cant_dip_x_bp, relief=SUNKEN, bg= 'light gray', bd=3,state=DISABLED)
entry_cant_h.place(x=700, y=50,width=100,height=25)
# entry_cant_mu = StringVar(frame_cant_dip_x_bp)
entry_cant_m = Entry(frame_cant_dip_x_bp, relief=SUNKEN, bg= 'light gray', bd=3,state=DISABLED)
entry_cant_m.place(x=700, y=100,width=100,height=25)
    #Button frame2:
btn_calc_dip_x_bp = Button(frame_cant_dip_x_bp, text='Calcular', width=8, height=2, bg='light gray').place(x=390,y=90)


    #Lbls frame3:
lbl_cant_viajes = Label(frame_cant_viaj, text='Cantidad de Viajes', width=35, height=1, bg='light gray').place(x=1, y=0)
lbl_orig = Label(frame_cant_viaj, text='Origen:', width=10, height=1, bg='light gray').place(x=90, y=70)
lbl_destin = Label(frame_cant_viaj, text='Destino:', width=10, height=1, bg='light gray').place(x=90, y=130)
lbl_cant_viaj = Label(frame_cant_viaj, text='Cantidad:', width=10, height=1, bg='light gray').place(x=590, y=100)
    #Entry frame3:
# entry_ingr_orig = StringVar(frame_cant_viaj)
entry_ingr_orig = Entry(frame_cant_viaj, relief=SUNKEN, bg= 'light gray', bd=3)
entry_ingr_orig.place(x=190, y=70,width=100,height=25)
entry_ingr_dest = StringVar(frame_cant_viaj)
entry_ingr_dest = Entry(frame_cant_viaj, relief=SUNKEN, bg= 'light gray', bd=3)
entry_ingr_dest.place(x=190, y=130,width=100,height=25)
# entry_cant_viaj = StringVar(frame_cant_viaj)
entry_cant_viaj = Entry(frame_cant_viaj, relief=SUNKEN, bg= 'light gray', bd=3,state=DISABLED)
entry_cant_viaj.place(x=700, y=100,width=100,height=25)
    #Button frame3
btn_calc_viaj = Button(frame_cant_viaj, text='Calcular', width=8, height=2, bg='light gray').place(x=390,y=90)


    #Lbls frame4:



ventana.mainloop()


# In[ ]:




