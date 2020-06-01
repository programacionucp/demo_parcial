#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 5.2
#  in conjunction with Tcl version 8.6
#    Jun 01, 2020 03:23:26 PM -03  platform: Windows NT
#    Jun 01, 2020 04:26:40 PM -03  platform: Windows NT

import sys

import json

with open('diputados.json') as archivoDip:
    lstDip = json.load(archivoDip)

with open('viajes.json') as archivoVia:
    lstVia = json.load(archivoVia)

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def set_Tk_var():
    global cantidadVia
    cantidadVia = tk.StringVar()
    global nomProvincia
    nomProvincia = tk.StringVar()
    global proCantidad
    proCantidad = tk.StringVar()
    global bloque
    bloque = tk.StringVar()
    global hombres
    hombres = tk.StringVar()
    global mujeres
    mujeres = tk.StringVar()
    global origen
    origen = tk.StringVar()
    global destino
    destino = tk.StringVar()
    global dipuID
    dipuID = tk.StringVar()
    global name
    name = tk.StringVar()
    global proBusc
    proBusc = tk.StringVar()
    global cantViajes
    cantViajes = tk.StringVar()
    global bloqBusc
    bloqBusc = tk.StringVar()
    global añoInicio
    añoInicio = tk.StringVar()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def buscar():
    print('par_support.buscar')
    sys.stdout.flush()
    contador= 0
    dip=dipuID.get
    for datos in lstDip:
        if datos[str(lstDip.index(datos)+1)]["﻿diputado_id"] == dip:
            name.set(datos[str(lstDip.index(datos)+1)]["diputado_nombre"]+" "+datos[str(lstDip.index(datos)+1)]["diputado_apellido"])
            for element in lstVia:
                if element[str(lstVia.index(datos)+1)]["Persona_apellido_y_nombre"] == datos[str(lstDip.index(datos)+1)]["diputado_apellido"]+" "+datos[str(lstDip.index(datos)+1)]["diputado_nombre"]:
                    contador+=1
            proBusc.set(datos[str(lstDip.index(datos))]["diputado_distrito"])
            cantViajes.set(contador)
            bloqBusc.set(datos[str(lstDip.index(datos))]["diputado_bloque"])
            añoInicio.set(datos[str(lstDip.index(datos))]["mandato_inicio"])

def calc1():
    print('par_support.calc1')
    sys.stdout.flush()
    contador=0
    pro=nomProvincia.get().upper()
    for datos in lstDip:
        if datos[str(lstDip.index(datos)+1)]["diputado_distrito"] == pro:
            contador+=1
    proCantidad.set(contador)

def calc2():
    print('par_support.calc2')
    sys.stdout.flush()
    contador=0
    blo=bloque.get().upper()
    for datos in lstDip:
        if datos[str(lstDip.index(datos)+1)]["diputado_bloque"] == blo and datos[str(lstDip.index(datos)+1)]["diputado_genero"] == "F":
            contador+=1
            mujeres.set(contador)
        if datos[str(lstDip.index(datos)+1)]["diputado_bloque"] == blo and datos[str(lstDip.index(datos)+1)]["diputado_genero"] == "M":
            contador+=1
            hombres.set(contador)

def calc3():
    print('par_support.calc3')
    sys.stdout.flush()
    contador=0
    orig=origen.get()
    dest=destino.get()
    for datos in lstVia:
        if datos[str(lstVia.index(datos)+1)]["Origen_ciudad"] == orig and datos[str(lstVia.index(datos)+1)]["Destino_ciudad"] == dest:
            contador+=1
    cantidadVia.set(contador)

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import par
    par.vp_start_gui()





