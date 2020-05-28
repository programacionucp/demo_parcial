#!/usr/bin/env python
# coding: utf-8

# In[8]:


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

lista_auxiliar=[[],[]]

#Funciones
def Visual_Info():
    global lista_auxiliar
    confirmados = [0,0,0,0]
    fallecidos = [0,0,0,0]
    recuperados = [0,0,0,0]
    for n in Lista_covid:
        if n['pais'] == 'Argentina':
            confirmados[0]+=int(n['confirmados'])
            fallecidos[0]+=int(n['muertos'])
            recuperados[0]+=int(n['recuperados'])
        elif n['pais'] == 'Paraguay':
            confirmados[1]+=int(n['confirmados'])
            fallecidos[1]+=int(n['muertos'])
            recuperados[1]+=int(n['recuperados'])
        elif n['pais'] == 'Uruguay':
            confirmados[2]+=int(n['confirmados'])
            fallecidos[2]+=int(n['muertos'])
            recuperados[2]+=int(n['recuperados'])
        elif n['pais'] == 'Brazil':
            confirmados[3]+=int(n['confirmados'])
            fallecidos[3]+=int(n['muertos'])
            recuperados[3]+=int(n['recuperados'])
    #Argentina:  
    entry_conf_arg_var.set(confirmados[0])
    entry_fallec_arg_var.set(fallecidos[0])
    entry_recup_arg_var.set(recuperados[0])
    #Py
    entry_conf_py.set(confirmados[1])
    entry_fallec_py_var.set(fallecidos[1])
    entry_recup_py_var.set(recuperados[1])
    #Uy
    entry_conf_py.set(confirmados[2])
    entry_fallec_py_var.set(fallecidos[2])
    entry_recup_py_var.set(recuperados[2])
    #Br              
    entry_conf_br.set(confirmados[3])
    entry_fallec_br_var.set(fallecidos[3])
    entry_recup_br_var.set(recuperados[3])
    
    puesto = confirmados.index(max(confirmados))
    cantidad = max(confirmados)
    lista_auxiliar[1] = cantidad
    if puesto == 0:
        lista_auxiliar[0] = 'Argentina'
    elif puesto == 1:
        lista_auxiliar[0] = 'Paraguay'
    elif puesto == 2:
        lista_auxiliar[0] = 'Uruguay'
    elif puesto == 3:
        lista_auxiliar[0] = 'Brazil'
        
def Max_Casos():
    global lista_auxiliar
    entry_pais_var.set(lista_auxiliar[0])
    entry_cant_var.set(lista_auxiliar[1])

def Pais_Buscado():
    for i in Lista_covid:
        if i['pais']==cmb_pais_var.get() and i['dia']==entry_dia_var.get():
            entry_confir_var.set(i['confirmados'])
            entry_fallecidos_var.set(i['muertos'])
            entry_recup_var.set(i['recuperados'])
            
            
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
entry_conf_arg_var = StringVar(frame_vis_arg)
entry_conf_arg = Entry(frame_vis_arg, relief=SUNKEN, bg= 'light gray', state=DISABLED, bd=3,textvariable=entry_conf_arg_var)
entry_conf_arg.place(x=130, y=20,width=130,height=25)
entry_fallec_arg_var = StringVar(frame_vis_arg)
entry_fallec_arg = Entry(frame_vis_arg, relief=SUNKEN, bg= 'light gray', state=DISABLED, bd=3, textvariable=entry_fallec_arg_var)
entry_fallec_arg.place(x=130, y=50,width=130,height=25)
entry_recup_arg_var = StringVar(frame_vis_arg)
entry_recup_arg = Entry(frame_vis_arg, relief=SUNKEN, bg= 'light gray', state=DISABLED, bd=3, textvariable=entry_recup_arg_var)
entry_recup_arg.place(x=130, y=80,width=130,height=25)
    #Labels Paraguay:
lbl_py = Label(frame_vis_py, text='Paraguay', width=20, height=1, bg='light gray').place(x=70, y=0)
lbl_conf_py = Label(frame_vis_py, text='Confirmados:', width=20, height=1, bg='light gray').place(x=0, y=20)    
lbl_fallec_py = Label(frame_vis_py, text='Fallecidos:', width=20, height=1, bg='light gray').place(x=5, y=50)
lbl_recup_py = Label(frame_vis_py, text='Recuperados:', width=20, height=1, bg='light gray').place(x=10, y=80)
    #Entrys Paraguay:
entry_conf_py = StringVar(frame_vis_py)
entry_conf_py = Entry(frame_vis_py, relief=SUNKEN, bg= 'light gray', state=DISABLED, bd=3,textvariable=entry_conf_py)
entry_conf_py.place(x=130, y=20,width=130,height=25)
entry_fallec_py_var = StringVar(frame_vis_py)
entry_fallec_py = Entry(frame_vis_py, relief=SUNKEN, bg= 'light gray', bd=3,state=DISABLED, textvariable=entry_fallec_py_var)
entry_fallec_py.place(x=130, y=50,width=130,height=25)
entry_recup_py_var = StringVar(frame_vis_py)
entry_recup_py = Entry(frame_vis_py, relief=SUNKEN, bg= 'light gray', bd=3,state=DISABLED, textvariable=entry_recup_py_var)
entry_recup_py.place(x=130, y=80,width=130,height=25)    
    #Labels Uruguay:
lbl_uy = Label(frame_vis_uy, text='Uruguay', width=20, height=1, bg='light gray').place(x=70, y=0)
lbl_conf_uy = Label(frame_vis_uy, text='Confirmados', width=20, height=1, bg='light gray').place(x=0, y=20)    
lbl_fallec_uy = Label(frame_vis_uy, text='Fallecidos:', width=20, height=1, bg='light gray').place(x=5, y=50)
lbl_recup_uy = Label(frame_vis_uy, text='Recuperados:', width=20, height=1, bg='light gray').place(x=10, y=80)
    #Entrys Uruguay:
entry_conf_uy_var = StringVar(frame_vis_uy)
entry_conf_uy = Entry(frame_vis_uy, relief=SUNKEN, bg= 'light gray', state=DISABLED, bd=3,textvariable=entry_conf_uy_var)
entry_conf_uy.place(x=130, y=20,width=130,height=25)
entry_fallec_uy_var = StringVar(frame_vis_uy)
entry_fallec_uy = Entry(frame_vis_uy, relief=SUNKEN, bg= 'light gray', bd=3,state=DISABLED, textvariable=entry_fallec_uy_var)
entry_fallec_uy.place(x=130, y=50,width=130,height=25)
entry_recup_uy_var = StringVar(frame_vis_uy)
entry_recup_uy = Entry(frame_vis_uy, relief=SUNKEN, bg= 'light gray', bd=3,state=DISABLED, textvariable=entry_recup_uy_var)
entry_recup_uy.place(x=130, y=80,width=130,height=25)   
    #Labels Brasil:
lbl_br = Label(frame_vis_br, text='Brasil', width=20, height=1, bg='light gray').place(x=70, y=0)
lbl_conf_br = Label(frame_vis_br, text='Confirmados', width=20, height=1, bg='light gray').place(x=0, y=20)    
lbl_fallec_br = Label(frame_vis_br, text='Fallecidos:', width=20, height=1, bg='light gray').place(x=5, y=50)
lbl_recup_br = Label(frame_vis_br, text='Recuperados:', width=20, height=1, bg='light gray').place(x=10, y=80)
    #Entrys Brasil:
entry_conf_br_var = StringVar(frame_vis_br)
entry_conf_br = Entry(frame_vis_br, relief=SUNKEN, bg= 'light gray', state=DISABLED, bd=3,textvariable=entry_conf_br_var)
entry_conf_br.place(x=130, y=20,width=130,height=25)
entry_fallec_br_var = StringVar(frame_vis_br)
entry_fallec_br = Entry(frame_vis_br, relief=SUNKEN, bg= 'light gray', bd=3,state=DISABLED, textvariable=entry_fallec_br_var)
entry_fallec_br.place(x=130, y=50,width=130,height=25)
entry_recup_br_var = StringVar(frame_vis_br)
entry_recup_br = Entry(frame_vis_br, relief=SUNKEN, bg= 'light gray', bd=3,state=DISABLED, textvariable=entry_recup_br_var)
entry_recup_br.place(x=130, y=80,width=130,height=25)
Visual_Info()
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
entry_cant_var = StringVar(frame_max_confir)
entry_cant = Entry(frame_max_confir, relief=SUNKEN, bg= 'light gray', bd=3,state=DISABLED, textvariable=entry_cant_var)
entry_cant.place(x=930, y=65,width=130,height=25)
    #Boton:
btn_busc_pais = Button(frame_max_confir, text='Buscar', width=8, height=2, bg='light grey').place(x=550, y=35)
#Frame Buscador:
frame_busc = Frame(ventana, width=1280, height=120, relief=SUNKEN, bg='light gray', bd=3)
frame_busc.place(x=0, y=240, width=1280, height=180)
    #Labels
lbl_pais = Label(frame_busc, text='País:', width=20, height=1, bg='light gray').place(x=70, y=55)
lbl_dias= Label(frame_busc, text='Día:', width=20, height=1, bg='light gray').place(x=70, y=95)
lbl_confir = Label(frame_busc, text='Confirmados:', width=20, height=1, bg='light gray').place(x=800, y=35)
lbl_fallecidos = Label(frame_busc, text='Fallecidos:', width=20, height=1, bg='light gray').place(x=800, y=65)
lbl_recup = Label(frame_busc, text='Recuperados:', width=20, height=1, bg='light gray').place(x=800, y=95)
    #Entrys
entry_dia_var = StringVar(frame_busc)
entry_dia = Entry(frame_busc, relief=SUNKEN, bg= 'light gray', bd=3, textvariable=entry_dia_var)
entry_dia.place(x=180, y=95,width=130,height=25)
entry_confir_var =  StringVar(frame_busc)
entry_confir = Entry(frame_busc, relief=SUNKEN, bg= 'light gray', state=DISABLED, bd=3,textvariable=entry_confir_var)
entry_confir.place(x=930, y=35,width=130,height=25)
entry_fallecidos_var = StringVar(frame_busc)
entry_fallecidos = Entry(frame_busc, relief=SUNKEN, bg= 'light gray', state=DISABLED, bd=3,textvariable=entry_fallecidos_var)
entry_fallecidos.place(x=930, y=65,width=130,height=25)
entry_recup_var =  StringVar(frame_busc)
entry_recup = Entry(frame_busc, relief=SUNKEN, bg= 'light gray', state=DISABLED, bd=3,textvariable=entry_recup_var)
entry_recup.place(x=930, y=95,width=130,height=25)
     #Boton
btn_busc_pais = Button(frame_busc, text='Buscar', width=8, height=2, bg='light grey',command=Pais_Buscado).place(x=550, y=55)
    #Combobox
cmb_pais_var = StringVar(frame_busc)
cmb_pais = ttk.Combobox(frame_busc, values=['Argentina','Bolivia','Brazil','Chile','Colombia','Ecuador','Paraguay','Peru','Uruguay','Venezuela'], textvariable=cmb_pais_var)
cmb_pais.place(x=180, y=55)

ventana.mainloop()


# In[ ]:




