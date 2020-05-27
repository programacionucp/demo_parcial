from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image,ImageTk
import json

root = Tk()
root.geometry('1000x650')
root.configure(bg='black')

    Listacovid19 = json.load(file)
    
list_aux = [0,0]

#Funciones
def Visualizar_Info_por_pais():
    global list_aux
    confirmados_l = [0,0,0,0]
    fallecidos_l = [0,0,0,0]
    recuperados_l = [0,0,0,0]
    for i in Listacovid19:
        if i['pais'] == "Argentina":
            confirmados_l[0]+=int(i['confirmados'])
            fallecidos_l[0]+=int(i['muertos'])
            recuperados_l[0]+=int(i['recuperados'])
        elif i['pais'] == "Paraguay":
            confirmados_l[1]+=int(i['confirmados'])
            fallecidos_l[1]+=int(i['muertos'])
            recuperados_l[1]+=int(i['recuperados'])
        elif i['pais'] == "Uruguay":
            confirmados_l[2]+=int(i['confirmados'])
            fallecidos_l[2]+=int(i['muertos'])
            recuperados_l[2]+=int(i['recuperados'])
        elif i['pais'] == "Brazil":
            confirmados_l[3]+=int(i['confirmados'])
            fallecidos_l[3]+=int(i['muertos'])
            recuperados_l[3]+=int(i['recuperados'])
            
    #Argentina
    f_arg_entr_var_c.set(confirmados_l[0])
    f_arg_entr_var_f.set(fallecidos_l[0])
    f_arg_entr_var_r.set(recuperados_l[0])

    #Paraguay
    
    f_par_entr_var_c.set(confirmados_l[1])
    f_par_entr_var_f.set(fallecidos_l[1])
    f_par_entr_var_r.set(recuperados_l[1])
    
    #Uruguay
    f_uru_entr_var_c.set(confirmados_l[2])
    f_uru_entr_var_f.set(fallecidos_l[2])
    f_uru_entr_var_r.set(recuperados_l[2])
    
    #Brasil
    f_br_entr_var_c.set(confirmados_l[3])
    f_br_entr_var_f.set(fallecidos_l[3])
    f_br_entr_var_r.set(recuperados_l[3])
    
    indice = recuperados_l.index(max(recuperados_l))
    cantidad = max(recuperados_l)
    list_aux[1]=cantidad
    if indice == 0:
        list_aux[0]='Argentina'
    elif indice == 1:
        list_aux[0]='Paraguay'
    elif indice == 2:
        list_aux[0]='Uruguay'
    elif indice == 3:
        list_aux[0]='Brasil'
        
def set_pais_recuperados():
    global list_aux
    entr_pais_var.set(list_aux[0])
    entr_cant_var.set(list_aux[1])
    
def set_pais_buscado():
    for i in Listacovid19:
        if i['pais']==cmb_pais_var.get() and i['dia']==entr_dia_var.get():
            f_dia_entr_var_c.set(i['confirmados'])
            f_dia_entr_var_f.set(i['muertos'])
            f_dia_entr_var_r.set(i['recuperados'])
            break
       
    
#GUI
    #Frame_Paises
F_Paises = Frame(root, width=1000, height=250, bd=2, relief=SUNKEN, bg='black')
F_Paises.pack()
        #Frame_Argentina
F_Argentina = Frame(F_Paises, width=250, height=250, bd=2, relief=SUNKEN, bg='black')
F_Argentina.pack(side=LEFT)
lbl_Argentina = Label(F_Argentina, text='Argentina').place(x=60, y=0)
f_arg_lbl = Label(F_Argentina, text='Confirmados').place(x=0, y=20)
f_arg_lbl = Label(F_Argentina, text='Fallecidos').place(x=0, y=60)
f_arg_lbl = Label(F_Argentina, text='Recuperados').place(x=0, y=100)
f_arg_entr_var_c = StringVar(F_Argentina)
f_arg_entr_c = Entry(F_Argentina, textvariable=f_arg_entr_var_c)
f_arg_entr_c.place(x=80, y=20)
f_arg_entr_var_f = StringVar(F_Argentina)
f_arg_entr_f = Entry(F_Argentina, textvariable=f_arg_entr_var_f)
f_arg_entr_f.place(x=80, y=60)
f_arg_entr_var_r = StringVar(F_Argentina)
f_arg_entr_r = Entry(F_Argentina, textvariable=f_arg_entr_var_r)
f_arg_entr_r.place(x=80, y=100)
        #Frame_Paraguay
F_Paraguay = Frame(F_Paises, width=250, height=250, bd=2, relief=SUNKEN, bg='black')
F_Paraguay.pack(side=LEFT)
lbl_Paraguay = Label(F_Paraguay, text='Paraguay').place(x=60, y=0)
f_par_lbl = Label(F_Paraguay, text='Confirmados').place(x=0, y=20)
f_par_lbl = Label(F_Paraguay, text='Fallecidos').place(x=0, y=60)
f_par_lbl = Label(F_Paraguay, text='Recuperados').place(x=0, y=100)
f_par_entr_var_c = StringVar(F_Paraguay)
f_par_entr_c = Entry(F_Paraguay, textvariable=f_par_entr_var_c)
f_par_entr_c.place(x=80, y=20)
f_par_entr_var_f = StringVar(F_Paraguay)
f_par_entr_f = Entry(F_Paraguay, textvariable=f_par_entr_var_f)
f_par_entr_f.place(x=80, y=60)
f_par_entr_var_r = StringVar(F_Paraguay)
f_par_entr_r = Entry(F_Paraguay, textvariable=f_par_entr_var_r)
f_par_entr_r.place(x=80, y=100)
        #Frame_Uruguay
F_Uruguay = Frame(F_Paises, width=250, height=250, bd=2, relief=SUNKEN, bg='black')
F_Uruguay.pack(side=LEFT)
lbl_Uruguay = Label(F_Uruguay, text='Uruguay').place(x=60, y=0)
f_uru_lbl = Label(F_Uruguay, text='Confirmados').place(x=0, y=20)
f_uru_lbl = Label(F_Uruguay, text='Fallecidos').place(x=0, y=60)
f_uru_lbl = Label(F_Uruguay, text='Recuperados').place(x=0, y=100)
f_uru_entr_var_c = StringVar(F_Uruguay)
f_uru_entr_c = Entry(F_Uruguay, textvariable=f_uru_entr_var_c)
f_uru_entr_c.place(x=80, y=20)
f_uru_entr_var_f = StringVar(F_Uruguay)
f_uru_entr_f = Entry(F_Uruguay, textvariable=f_uru_entr_var_f)
f_uru_entr_f.place(x=80, y=60)
f_uru_entr_var_r = StringVar(F_Uruguay)
f_uru_entr_r = Entry(F_Uruguay, textvariable=f_uru_entr_var_r)
f_uru_entr_r.place(x=80, y=100)
        #Frame_Brasil
F_Brasil = Frame(F_Paises, width=250, height=250, bd=2, relief=SUNKEN, bg='black')
F_Brasil.pack(side=LEFT)
lbl_Brasil = Label(F_Brasil, text='Brasil').place(x=60, y=0)
f_br_lbl = Label(F_Brasil, text='Confirmados').place(x=0, y=20)
f_br_lbl = Label(F_Brasil, text='Fallecidos').place(x=0, y=60)
f_br_lbl = Label(F_Brasil, text='Recuperados').place(x=0, y=100)
f_br_entr_var_c = StringVar(F_Brasil)
f_br_entr_c = Entry(F_Brasil, textvariable=f_br_entr_var_c)
f_br_entr_c.place(x=80, y=20)
f_br_entr_var_f = StringVar(F_Brasil)
f_br_entr_f = Entry(F_Brasil, textvariable=f_br_entr_var_f)
f_br_entr_f.place(x=80, y=60)
f_br_entr_var_r = StringVar(F_Brasil)
f_br_entr_r = Entry(F_Brasil, textvariable=f_br_entr_var_r)
f_br_entr_r.place(x=80, y=100)
Visualizar_Info_por_pais()
    #Frame_recuperados
F_Recuperados = Frame(root, width=1000, height=200, bd=2, relief=SUNKEN, bg='black')
F_Recuperados.pack()
lbl_mas_recup = Label(F_Recuperados, text='País con más Confirimados').place(x=300, y=60)
btn_busc = Button(F_Recuperados, text='Buscar', command=set_pais_recuperados).place(x=600, y=60)
lbl_pais = Label(F_Recuperados, text='País').place(x=760, y=30)
entr_pais_var = StringVar(F_Recuperados)
entr_pais = Entry(F_Recuperados, textvariable=entr_pais_var)
entr_pais.place(x=830, y=30)
lbl_Cantidad = Label(F_Recuperados, text='Cantidad').place(x=760, y=60)
entr_cant_var = StringVar(F_Recuperados)
entr_cant = Entry(F_Recuperados, textvariable=entr_cant_var)
entr_cant.place(x=830, y=60)
    #Frame_buscador
F_Dia = Frame(root, width=1000, height=200, bd=2, relief=SUNKEN, bg='black')
F_Dia.pack()
lbl_pais_cmb= Label(F_Dia, text='País').place(x=200,y=30)
cmb_pais_var = StringVar(F_Dia)
cmb_pais = ttk.Combobox(F_Dia, values=["Argentina","Paraguay","Uruguay","Brazil"], textvariable=cmb_pais_var)
cmb_pais.place(x=270, y=30)
lbl_Cantidad = Label(F_Dia, text='Día').place(x=200, y=60)
entr_dia_var = StringVar(F_Dia)
entr_dia = Entry(F_Dia, textvariable=entr_dia_var)
entr_dia.place(x=270, y=60)
btn_busc_d = Button(F_Dia, text='Buscar', command=set_pais_buscado).place(x=450, y=60)
f_dia_lbl = Label(F_Dia, text='Confirmados').place(x=600, y=20)
f_dia_lbl = Label(F_Dia, text='Fallecidos').place(x=600, y=60)
f_dia_lbl = Label(F_Dia, text='Recuperados').place(x=600, y=100)
f_dia_entr_var_c = StringVar(F_Dia)
f_dia_entr_c = Entry(F_Dia, textvariable=f_dia_entr_var_c)
f_dia_entr_c.place(x=700, y=20)
f_dia_entr_var_f = StringVar(F_Dia)
f_dia_entr_f = Entry(F_Dia, textvariable=f_dia_entr_var_f)
f_dia_entr_f.place(x=700, y=60)
f_dia_entr_var_r = StringVar(F_Dia)
f_dia_entr_r = Entry(F_Dia, textvariable=f_dia_entr_var_r)
f_dia_entr_r.place(x=700, y=100)

root.mainloop()
