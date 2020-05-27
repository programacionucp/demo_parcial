from tkinter import *
from tkinter import ttk
import json

with open('covid19.json', encoding = 'utf-8') as file:
    lst_covid = json.load(file)

#funciones
def paises():
    global lst_paises
    lst_paises = list()
    for un_pais in lst_covid:
        if un_pais['pais'] not in lst_paises:
            lst_paises.append(un_pais['pais'])
    return lst_paises

def dias():
    global lst_dias
    lst_dias = list()
    for un_dia in lst_covid:
        if un_dia['dia'] not in lst_dias:
            lst_dias.append(un_dia['dia'])
    return lst_dias

def buscador():
    selec_pais = combo2.get()
    selec_dia = combo3.get()
    for una_farm in lst_covid:
        if una_farm['pais'] == selec_pais and una_farm['dia'] == selec_dia:
            confir.config(text=una_farm['confirmados'])
            fall.config(text=una_farm['muertos'])
            recu.config(text=una_farm['recuperados'])


def infoArg():
    for una_info in lst_covid:
        if una_info['pais'] == "Argentina":
            confir_arg.config(text=una_info['confirmados'])
            fall_arg.config(text=una_info['muertos'])
            recu_arg.config(text=una_info['recuperados'])

def infoBra():
    for una_info in lst_covid:
        if una_info['pais'] == "Brazil":
            confir_bra.config(text=una_info['confirmados'])
            fall_bra.config(text=una_info['muertos'])
            recu_bra.config(text=una_info['recuperados'])

def infoPar():
    for una_info in lst_covid:
        if una_info['pais'] == "Paraguay":
            confir_par.config(text=una_info['confirmados'])
            fall_par.config(text=una_info['muertos'])
            recu_par.config(text=una_info['recuperados'])

def infoUru():
    for una_info in lst_covid:
        if una_info['pais'] == "Paraguay":
            confir_uru.config(text=una_info['confirmados'])
            fall_uru.config(text=una_info['muertos'])
            recu_uru.config(text=una_info['recuperados'])

def mas():
    canti = 0
    pais = ""
    for un_recu in lst_covid:
        if int(un_recu['recuperados']) > canti:
            canti = int(un_recu['recuperados'])
            cantidad.config(text=canti)
            pais = un_recu["pais"]
            combo1.config(text=pais)

covid = Tk()
covid.title('Covid-19')
covid.geometry('778x400')
covid.resizable(0,0)
Canvas(covid, width=180, height=140, borderwidth=2, relief="groove").place(x=10, y=33)
Canvas(covid, width=180, height=140, borderwidth=2, relief="groove").place(x=200, y=33)
Canvas(covid, width=180, height=140, borderwidth=2, relief="groove").place(x=390, y=33)
Canvas(covid, width=180, height=140, borderwidth=2, relief="groove").place(x=580, y=33)
Label(covid, text="Visualizacion De Informacion Por Paises", font=("Arial", 11)).place(x=10, y=10)
Label(covid, text="Argentina", font=("Arial", 16)).place(x=50, y=37)
Label(covid, text="Paraguay", font=("Arial", 16)).place(x=243, y=37)
Label(covid, text="Uruguay", font=("Arial", 16)).place(x=440, y=37)
Label(covid, text="Brasil", font=("Arial", 16)).place(x=640, y=37)
Label(covid, text="Confirmados:", font=("Arial", 11)).place(x=15, y=67)
Label(covid, text="Fallecidos:", font=("Arial", 11)).place(x=15, y=97)
Label(covid, text="Recuperados:", font=("Arial", 11)).place(x=15, y=127)
Label(covid, text="Confirmados:", font=("Arial", 11)).place(x=210, y=67)
Label(covid, text="Fallecidos:", font=("Arial", 11)).place(x=210, y=97)
Label(covid, text="Recuperados:", font=("Arial", 11)).place(x=210, y=127)
Label(covid, text="Confirmados:", font=("Arial", 11)).place(x=400, y=67)
Label(covid, text="Fallecidos:", font=("Arial", 11)).place(x=400, y=97)
Label(covid, text="Recuperados:", font=("Arial", 11)).place(x=400, y=127)
Label(covid, text="Confirmados:", font=("Arial", 11)).place(x=600, y=67)
Label(covid, text="Fallecidos:", font=("Arial", 11)).place(x=600, y=97)
Label(covid, text="Recuperados:", font=("Arial", 11)).place(x=600, y=127)
Label(covid, text="Pais Mas Recuperados", font=("Arial", 11)).place(x=10, y=210)
Label(covid, text="Pais:", font=("Arial", 11)).place(x=300, y=190)
Label(covid, text="Cantidad:", font=("Arial", 11)).place(x=300, y=230)
Label(covid, text="Buscador", font=("Arial", 11)).place(x=10, y=300)
Label(covid, text="Pais:", font=("Arial", 11)).place(x=10, y=340)
Label(covid, text="Dia:", font=("Arial", 11)).place(x=10, y=370)
Label(covid, text="Confirmados:", font=("Arial", 11)).place(x=400, y=320)
Label(covid, text="Fallecidos:", font=("Arial", 11)).place(x=400, y=350)
Label(covid, text="Recuperados:", font=("Arial", 11)).place(x=400, y=380)

#Label cambiante
global confir_arg
global fall_arg
global recu_arg
global confir_par
global fall_par
global recu_par
global confir_uru
global fall_uru
global recu_uru
global confir_bra
global fall_bra
global recu_bra
confir_arg=Label(covid, text="---", font=("Arial", 11))
confir_arg.place(x=145, y=67)
fall_arg=Label(covid, text="---", font=("Arial", 11))
fall_arg.place(x=145, y=97)
recu_arg=Label(covid, text="---", font=("Arial", 11))
recu_arg.place(x=145, y=127)

confir_par=Label(covid, text="---", font=("Arial", 11))
confir_par.place(x=345, y=67)
fall_par=Label(covid, text="---", font=("Arial", 11))
fall_par.place(x=345, y=97)
recu_par=Label(covid, text="---", font=("Arial", 11))
recu_par.place(x=345, y=127)

confir_uru=Label(covid, text="---", font=("Arial", 11))
confir_uru.place(x=525, y=67)
fall_uru=Label(covid, text="---", font=("Arial", 11))
fall_uru.place(x=525, y=97)
recu_uru=Label(covid, text="---", font=("Arial", 11))
recu_uru.place(x=525, y=127)

confir_bra=Label(covid, text="---", font=("Arial", 11))
confir_bra.place(x=705, y=67)
fall_bra=Label(covid, text="---", font=("Arial", 11))
fall_bra.place(x=705, y=97)
recu_bra=Label(covid, text="---", font=("Arial", 11))
recu_bra.place(x=705, y=127)

global cantidad
cantidad=Label(covid, text="---", font=("Arial", 11))
cantidad.place(x=405, y=230)

confir = Label(covid, text="---", font=("Arial", 11))
confir.place(x=500, y=320)
fall = Label(covid, text="---", font=("Arial", 11))
fall.place(x=500, y=350)
recu = Label(covid, text="---", font=("Arial", 11))
recu.place(x=500, y=380)

#combo
combo1 = Label(covid, text="---", font=("Arial", 11))
combo1.place(x=400, y=190)
combo2 = ttk.Combobox(covid, width=12)
combo2.configure(values=paises())
combo2.place(x=50, y=340)
combo3 = ttk.Combobox(covid, width=12)
combo3.configure(values=dias())
combo3.place(x=50, y=370)

#Botones
infoArg()
infoBra()
infoPar()
infoUru()

Button(covid, text="Buscar", command=mas).place(x=200, y=210)
Button(covid, text="Buscar", command=buscador).place(x=200, y=360)


covid.mainloop()