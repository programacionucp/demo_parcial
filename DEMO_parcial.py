#!/usr/bin/env python
# coding: utf-8

# In[32]:


from tkinter import *
from tkinter import ttk
import json

with open ('covid19.json', encoding = 'utf-8') as file:
    Lista_covid = json.load(file)

#Creación Tk
ventana = Tk()
ventana.geometry('1280x800+300+95')
ventana.title('Datos Covid19')
ventana.configure(bg='light gray')

#Funciones

#Frame: Visualización de información por paises 
frame_vis_arg = Frame(ventana, width=300, height=120, relief=SUNKEN, bg='light gray', bd=3)
frame_vis_arg.place(x=0, y=0, width=300, height=120)
frame_vis_py = Frame(ventana, width=300, height=120, relief=SUNKEN, bg='light gray', bd=3)
frame_vis_py.place(x=320, y=0, width=300, height=120)
frame_vis_uy = Frame(ventana, width=300, height=120, relief=SUNKEN, bg='light gray', bd=3)
frame_vis_uy.place(x=640, y=0, width=300, height=120)
frame_vis_br = Frame(ventana, width=300, height=120, relief=SUNKEN, bg='light gray', bd=3)
frame_vis_br.place(x=960, y=0, width=300, height=120)
    #Labels Arg:
lbl_arg = Label(frame_vis_arg, text='Argentina', width=20, height=1, bg='light gray').place(x=70, y=0)
lbl_conf_arg = Label(frame_vis_arg, text='Confirmados:', width=20, height=1, bg='light gray').place(x=0, y=20)    
lbl_fallec_arg = Label(frame_vis_arg, text='Fallecidos:', width=20, height=1, bg='light gray').place(x=5, y=50)
lbl_recup_arg = Label(frame_vis_arg, text='Recuperados:', width=20, height=1, bg='light gray').place(x=10, y=80)
    #Entrys Arg:
entry_conf_arg_var = IntVar(frame_vis_arg)
entry_conf_arg = Entry(frame_vis_arg, relief=SUNKEN, bg= 'light gray', state=DISABLED, bd=3,textvariable=entry_conf_arg_var)
entry_conf_arg.place(x=130, y=20,width=130,height=25)
entry_fallec_arg_var = IntVar(frame_vis_arg)
entry_fallec_arg = Entry(frame_vis_arg, relief=SUNKEN, bg= 'light gray', state=DISABLED, bd=3, textvariable=entry_fallec_arg_var)
entry_fallec_arg.place(x=130, y=50,width=130,height=25)
entry_recup_arg_var = IntVar(frame_vis_arg)
entry_recup_arg = Entry(frame_vis_arg, relief=SUNKEN, bg= 'light gray', state=DISABLED, bd=3, textvariable=entry_recup_arg_var)
entry_recup_arg.place(x=130, y=80,width=130,height=25)
    
    #Labels Paraguay:
lbl_py = Label(frame_vis_py, text='Paraguay', width=20, height=1, bg='light gray').place(x=70, y=0)
lbl_conf_py = Label(frame_vis_py, text='Confirmados:', width=20, height=1, bg='light gray').place(x=0, y=20)    
lbl_fallec_py = Label(frame_vis_py, text='Fallecidos:', width=20, height=1, bg='light gray').place(x=5, y=50)
lbl_recup_py = Label(frame_vis_py, text='Recuperados:', width=20, height=1, bg='light gray').place(x=10, y=80)
    #Entrys Paraguay:
entry_conf_py = IntVar(frame_vis_py)
entry_conf_py = Entry(frame_vis_py, relief=SUNKEN, bg= 'light gray', state=DISABLED, bd=3,textvariable=entry_conf_py)
entry_conf_py.place(x=130, y=20,width=130,height=25)
entry_fallec_py_var = IntVar(frame_vis_py)
entry_fallec_py = Entry(frame_vis_py, relief=SUNKEN, bg= 'light gray', bd=3,state=DISABLED, textvariable=entry_fallec_py_var)
entry_fallec_py.place(x=130, y=50,width=130,height=25)
entry_recup_py_var = IntVar(frame_vis_py)
entry_recup_py = Entry(frame_vis_py, relief=SUNKEN, bg= 'light gray', bd=3,state=DISABLED, textvariable=entry_recup_py_var)
entry_recup_py.place(x=130, y=80,width=130,height=25)    
    #Labels Uruguay:
lbl_uy = Label(frame_vis_uy, text='Uruguay', width=20, height=1, bg='light gray').place(x=70, y=0)
lbl_conf_uy = Label(frame_vis_uy, text='Confirmados', width=20, height=1, bg='light gray').place(x=0, y=20)    
lbl_fallec_uy = Label(frame_vis_uy, text='Fallecidos:', width=20, height=1, bg='light gray').place(x=5, y=50)
lbl_recup_uy = Label(frame_vis_uy, text='Recuperados:', width=20, height=1, bg='light gray').place(x=10, y=80)
    #Entrys Uruguay:
entry_conf_uy_var = IntVar(frame_vis_uy)
entry_conf_uy = Entry(frame_vis_uy, relief=SUNKEN, bg= 'light gray', state=DISABLED, bd=3,textvariable=entry_conf_uy_var)
entry_conf_uy.place(x=130, y=20,width=130,height=25)
entry_fallec_uy_var = IntVar(frame_vis_uy)
entry_fallec_uy = Entry(frame_vis_uy, relief=SUNKEN, bg= 'light gray', bd=3,state=DISABLED, textvariable=entry_fallec_uy_var)
entry_fallec_uy.place(x=130, y=50,width=130,height=25)
entry_recup_uy_var = IntVar(frame_vis_uy)
entry_recup_uy = Entry(frame_vis_uy, relief=SUNKEN, bg= 'light gray', bd=3,state=DISABLED, textvariable=entry_recup_uy_var)
entry_recup_uy.place(x=130, y=80,width=130,height=25)   
    #Labels Brasil:
lbl_br = Label(frame_vis_br, text='Brasil', width=20, height=1, bg='light gray').place(x=70, y=0)
lbl_conf_br = Label(frame_vis_br, text='Confirmados', width=20, height=1, bg='light gray').place(x=0, y=20)    
lbl_fallec_br = Label(frame_vis_br, text='Fallecidos:', width=20, height=1, bg='light gray').place(x=5, y=50)
lbl_recup_br = Label(frame_vis_br, text='Recuperados:', width=20, height=1, bg='light gray').place(x=10, y=80)
    #Entrys Brasil:
entry_conf_br_var = IntVar(frame_vis_br)
entry_conf_br = Entry(frame_vis_br, relief=SUNKEN, bg= 'light gray', state=DISABLED, bd=3,textvariable=entry_conf_br_var)
entry_conf_br.place(x=130, y=20,width=130,height=25)
entry_fallec_br_var = IntVar(frame_vis_br)
entry_fallec_br = Entry(frame_vis_br, relief=SUNKEN, bg= 'light gray', bd=3,state=DISABLED, textvariable=entry_fallec_br_var)
entry_fallec_br.place(x=130, y=50,width=130,height=25)
entry_recup_br_var = IntVar(frame_vis_br)
entry_recup_br = Entry(frame_vis_br, relief=SUNKEN, bg= 'light gray', bd=3,state=DISABLED, textvariable=entry_recup_br_var)
entry_recup_br.place(x=130, y=80,width=130,height=25)

#Frame País con más confirmados:
frame_max_confir = Frame(ventana, width=1280, height=120, relief=SUNKEN, bg='light gray', bd=3)
frame_max_confir.place(x=0, y=120, width=1280, height=120)

    #Labels
lbl_max_pais_confir = Label(frame_max_confir, text='País con más confirmados', width=20, height=1, bg='light gray').place(x=70, y=35)
lbl_pais= Label(frame_max_confir, text='País:', width=20, height=1, bg='light gray').place(x=800, y=7)
lbl_cant = Label(frame_max_confir, text='Cantidad:', width=20, height=1, bg='light gray').place(x=800, y=65)
    #Entrys
entry_pais_var = StringVar(frame_max_confir)
entry_pais = Entry(frame_max_confir, relief=SUNKEN, bg= 'light gray',state=DISABLED, bd=3,textvariable=entry_pais_var)
entry_pais.place(x=930, y=7,width=130,height=25)
entry_cant_var = IntVar(frame_max_confir)
entry_cant = Entry(frame_max_confir, relief=SUNKEN, bg= 'light gray', bd=3,state=DISABLED, textvariable=entry_cant_var)
entry_cant.place(x=930, y=65,width=130,height=25)
    #Boton:
btn_busc_pais = Button(frame_max_confir, text='Buscar', width=8, height=2, bg='light grey').place(x=550, y=35)

#Frame Buscador:
frame_busc = Frame(ventana, width=1280, height=120, relief=SUNKEN, bg='light gray', bd=3)
frame_busc.place(x=0, y=240, width=1280, height=180)
 #Labels
lbl_max_pais_confir = Label(frame_busc, text='País con más confirmados', width=20, height=1, bg='light gray').place(x=70, y=35)
lbl_pais= Label(frame_busc, text='País:', width=20, height=1, bg='light gray').place(x=800, y=7)
lbl_cant = Label(frame_busc, text='Cantidad:', width=20, height=1, bg='light gray').place(x=800, y=65)
lbl_cant = Label(frame_busc, text='Cantidad:', width=20, height=1, bg='light gray').place(x=800, y=65)
lbl_cant = Label(frame_busc, text='Cantidad:', width=20, height=1, bg='light gray').place(x=800, y=65)
    #Entrys
entry_pais_var = StringVar(frame_max_confir)
entry_pais = Entry(frame_max_confir, relief=SUNKEN, bg= 'light gray',state=DISABLED, bd=3,textvariable=entry_pais_var)
entry_pais.place(x=930, y=7,width=130,height=25)
entry_cant_var = IntVar(frame_max_confir)
entry_cant = Entry(frame_max_confir, relief=SUNKEN, bg= 'light gray', bd=3,state=DISABLED, textvariable=entry_cant_var)
entry_cant.place(x=930, y=65,width=130,height=25)
entry_pais_var = StringVar(frame_max_confir)
entry_pais = Entry(frame_max_confir, relief=SUNKEN, bg= 'light gray',state=DISABLED, bd=3,textvariable=entry_pais_var)
entry_pais.place(x=930, y=7,width=130,height=25)
entry_pais_var = StringVar(frame_max_confir)
entry_pais = Entry(frame_max_confir, relief=SUNKEN, bg= 'light gray',state=DISABLED, bd=3,textvariable=entry_pais_var)
entry_pais.place(x=930, y=7,width=130,height=25)
entry_pais_var = StringVar(frame_max_confir)
entry_pais = Entry(frame_max_confir, relief=SUNKEN, bg= 'light gray',state=DISABLED, bd=3,textvariable=entry_pais_var)
entry_pais.place(x=930, y=7,width=130,height=25)
    #Boton
frame_busc = Frame(ventana, width=1280, height=120, relief=SUNKEN, bg='light gray', bd=3)
frame_busc.place(x=0, y=240, width=1280, height=180)

ventana.mainloop()

