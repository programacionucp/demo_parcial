#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 5.0.3
#  in conjunction with Tcl version 8.6
#    May 27, 2020 04:17:14 PM -03  platform: Windows NT

import sys

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

import COVID19

def set_Tk_var():
    global pais
    pais = tk.StringVar()
    global dia
    dia = tk.StringVar()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
    configInicial()

def configInicial():
    global contConfirArg,contConfirPy,contConfirUru,contConfirBr
    global contFallArg,contFallPy,contFallUru,contFallBr
    global contRecupArg,contRecupPy,contRecupUru,contRecupBr

def buscarPorPais():
    print('DEMO_PARCIAL_IRALA_support.buscarPorPais')
    sys.stdout.flush()

def cargarDatos():

    lstDatos=COVID19.getListaDatos()
    for unPais in lstDatos:
        if unPais["pais"]=="Argentina":
            contConfirArg=int(unPais["confirmados"])
            contFallArg=int(unPais["muertos"])
            contRecupArg=int(unPais["recuperados"])
            w.lblArgentinaConfirmados.configure(text=contConfirArg)
            w.lblArgentinaFallecidos.configure(text=contFallArg)
            w.lblArgentinaRecuperados.configure(text=contRecupArg)

        elif unPais["pais"]=="Paraguay":
            contConfirPy=int(unPais["confirmados"])
            contFallPy=int(unPais["muertos"])
            contRecupPy=int(unPais["recuperados"])
            w.lblParaguayConfirmados.configure(text=contConfirPy)
            w.lblParaguayConfirmados.configure(text=contFallPy)
            w.lblParaguayConfirmados.configure(text=contRecupPy)

        elif unPais["pais"]=="Uruguay":
            contConfirUru=int(unPais["confirmados"])
            contFallUru=int(unPais["muertos"])
            contRecupUru=int(unPais["recuperados"])
            w.lblUruguayConfirmados.configure(text=contConfirUru)
            w.lblUruguayConfirmados.configure(text=contFallUru)
            w.lblUruguayConfirmados.configure(text=contRecupUru)

        elif unPais["pais"]=="Argentina":
            contConfirBr=int(unPais["confirmados"])
            contFallBr=int(unPais["muertos"])
            contRecupBr=int(unPais["recuperados"])
            w.lblBrasilConfirmados.configure(text=contConfirBr)
            w.lblBrasilConfirmados.configure(text=contFallBr)
            w.lblBrasilConfirmados.configure(text=contRecupBr)

def masRecuperados():
    print('DEMO_PARCIAL_IRALA_support.masRecuperados')
    sys.stdout.flush()

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import DEMO_PARCIAL_IRALA
    DEMO_PARCIAL_IRALA.vp_start_gui()


cargarDatos()

