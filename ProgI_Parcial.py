#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.0.3
#  in conjunction with Tcl version 8.6
#    Jun 01, 2020 05:36:29 PM -03  platform: Windows NT

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

import ProgI_Parcial_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    ProgI_Parcial_support.set_Tk_var()
    top = Toplevel1 (root)
    ProgI_Parcial_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    ProgI_Parcial_support.set_Tk_var()
    top = Toplevel1 (w)
    ProgI_Parcial_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1000x1000+575+0")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1, 1)
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Labelframe1 = tk.LabelFrame(top)
        self.Labelframe1.place(relx=0.04, rely=0.03, relheight=0.225
                , relwidth=0.92)
        self.Labelframe1.configure(relief='groove')
        self.Labelframe1.configure(foreground="black")
        self.Labelframe1.configure(text='''Cantidad de Diputados por Provincia''')
        self.Labelframe1.configure(background="#d9d9d9")
        self.Labelframe1.configure(highlightbackground="#d9d9d9")
        self.Labelframe1.configure(highlightcolor="black")

        self.Label1 = tk.Label(self.Labelframe1)
        self.Label1.place(relx=0.065, rely=0.222, height=25, width=72
                , bordermode='ignore')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Provincia''')

        self.Label1_1 = tk.Label(self.Labelframe1)
        self.Label1_1.place(relx=0.554, rely=0.222, height=25, width=71
                , bordermode='ignore')
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(activeforeground="black")
        self.Label1_1.configure(background="#d9d9d9")
        self.Label1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1.configure(foreground="#000000")
        self.Label1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1.configure(highlightcolor="black")
        self.Label1_1.configure(text='''Cantidad:''')

        self.TCombobox1 = ttk.Combobox(self.Labelframe1)
        self.TCombobox1.place(relx=0.152, rely=0.222, relheight=0.111
                , relwidth=0.202, bordermode='ignore')
        self.TCombobox1.configure(textvariable=ProgI_Parcial_support.combobox)
        self.TCombobox1.configure(takefocus="")

        self.TButton1 = ttk.Button(self.Labelframe1)
        self.TButton1.place(relx=0.402, rely=0.178, height=45, width=98
                , bordermode='ignore')
        self.TButton1.configure(command=ProgI_Parcial_support.calcularCantxProvincia)
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''CALCULAR''')

        self.lblCantProvincia = tk.Label(self.Labelframe1)
        self.lblCantProvincia.place(relx=0.652, rely=0.222, height=25, width=72
                , bordermode='ignore')
        self.lblCantProvincia.configure(activebackground="#f9f9f9")
        self.lblCantProvincia.configure(activeforeground="black")
        self.lblCantProvincia.configure(background="#d9d9d9")
        self.lblCantProvincia.configure(disabledforeground="#a3a3a3")
        self.lblCantProvincia.configure(foreground="#000000")
        self.lblCantProvincia.configure(highlightbackground="#d9d9d9")
        self.lblCantProvincia.configure(highlightcolor="black")
        self.lblCantProvincia.configure(relief="sunken")

        self.Labelframe1_1 = tk.LabelFrame(top)
        self.Labelframe1_1.place(relx=0.04, rely=0.27, relheight=0.226
                , relwidth=0.92)
        self.Labelframe1_1.configure(relief='groove')
        self.Labelframe1_1.configure(foreground="black")
        self.Labelframe1_1.configure(text='''Cantidad de Diputados por Bloques Politicos''')
        self.Labelframe1_1.configure(background="#d9d9d9")
        self.Labelframe1_1.configure(highlightbackground="#d9d9d9")
        self.Labelframe1_1.configure(highlightcolor="black")

        self.TLabel1 = ttk.Label(self.Labelframe1_1)
        self.TLabel1.place(relx=0.065, rely=0.265, height=24, width=54
                , bordermode='ignore')
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(anchor='w')
        self.TLabel1.configure(justify='left')
        self.TLabel1.configure(text='''Bloque:''')

        self.TLabel2 = ttk.Label(self.Labelframe1_1)
        self.TLabel2.place(relx=0.576, rely=0.265, height=24, width=75
                , bordermode='ignore')
        self.TLabel2.configure(background="#d9d9d9")
        self.TLabel2.configure(foreground="#000000")
        self.TLabel2.configure(font="TkDefaultFont")
        self.TLabel2.configure(relief="flat")
        self.TLabel2.configure(anchor='w')
        self.TLabel2.configure(justify='left')
        self.TLabel2.configure(text='''Hombres:''')

        self.TLabel3 = ttk.Label(self.Labelframe1_1)
        self.TLabel3.place(relx=0.576, rely=0.487, height=24, width=65
                , bordermode='ignore')
        self.TLabel3.configure(background="#d9d9d9")
        self.TLabel3.configure(foreground="#000000")
        self.TLabel3.configure(font="TkDefaultFont")
        self.TLabel3.configure(relief="flat")
        self.TLabel3.configure(anchor='w')
        self.TLabel3.configure(justify='left')
        self.TLabel3.configure(text='''Mujeres:''')

        self.lblHombres = ttk.Label(self.Labelframe1_1)
        self.lblHombres.place(relx=0.717, rely=0.265, height=24, width=42
                , bordermode='ignore')
        self.lblHombres.configure(background="#d9d9d9")
        self.lblHombres.configure(foreground="#000000")
        self.lblHombres.configure(font="TkDefaultFont")
        self.lblHombres.configure(relief="flat")
        self.lblHombres.configure(anchor='w')
        self.lblHombres.configure(justify='left')
        self.lblHombres.configure(text='''0''')

        self.lblMujeres = ttk.Label(self.Labelframe1_1)
        self.lblMujeres.place(relx=0.717, rely=0.487, height=24, width=55
                , bordermode='ignore')
        self.lblMujeres.configure(background="#d9d9d9")
        self.lblMujeres.configure(foreground="#000000")
        self.lblMujeres.configure(font="TkDefaultFont")
        self.lblMujeres.configure(relief="flat")
        self.lblMujeres.configure(anchor='w')
        self.lblMujeres.configure(justify='left')
        self.lblMujeres.configure(text='''0''')

        self.entryBloque = ttk.Entry(self.Labelframe1_1)
        self.entryBloque.place(relx=0.141, rely=0.265, relheight=0.115
                , relwidth=0.18, bordermode='ignore')
        self.entryBloque.configure(takefocus="")
        self.entryBloque.configure(cursor="ibeam")

        self.TButton2 = ttk.Button(self.Labelframe1_1)
        self.TButton2.place(relx=0.391, rely=0.265, height=30, width=98
                , bordermode='ignore')
        self.TButton2.configure(command=ProgI_Parcial_support.calcularBloque)
        self.TButton2.configure(takefocus="")
        self.TButton2.configure(text='''CALCULAR''')

        self.Labelframe1_2 = tk.LabelFrame(top)
        self.Labelframe1_2.place(relx=0.04, rely=0.522, relheight=0.226
                , relwidth=0.92)
        self.Labelframe1_2.configure(relief='groove')
        self.Labelframe1_2.configure(foreground="black")
        self.Labelframe1_2.configure(text='''Cantidad de Viajes''')
        self.Labelframe1_2.configure(background="#d9d9d9")
        self.Labelframe1_2.configure(highlightbackground="#d9d9d9")
        self.Labelframe1_2.configure(highlightcolor="black")

        self.Label2 = tk.Label(self.Labelframe1_2)
        self.Label2.place(relx=0.087, rely=0.221, height=26, width=62
                , bordermode='ignore')
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Origen:''')

        self.Label3 = tk.Label(self.Labelframe1_2)
        self.Label3.place(relx=0.087, rely=0.442, height=26, width=64
                , bordermode='ignore')
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Destino:''')

        self.TCombobox2 = ttk.Combobox(self.Labelframe1_2)
        self.TCombobox2.place(relx=0.174, rely=0.221, relheight=0.115
                , relwidth=0.203, bordermode='ignore')
        self.TCombobox2.configure(textvariable=ProgI_Parcial_support.combobox2)
        self.TCombobox2.configure(takefocus="")

        self.TCombobox3 = ttk.Combobox(self.Labelframe1_2)
        self.TCombobox3.place(relx=0.174, rely=0.442, relheight=0.115
                , relwidth=0.203, bordermode='ignore')
        self.TCombobox3.configure(textvariable=ProgI_Parcial_support.combobox3)
        self.TCombobox3.configure(takefocus="")

        self.TButton3 = ttk.Button(self.Labelframe1_2)
        self.TButton3.place(relx=0.446, rely=0.31, height=30, width=98
                , bordermode='ignore')
        self.TButton3.configure(command=ProgI_Parcial_support.calcularCantDestino)
        self.TButton3.configure(takefocus="")
        self.TButton3.configure(text='''CALCULAR''')

        self.TLabel4 = ttk.Label(self.Labelframe1_2)
        self.TLabel4.place(relx=0.652, rely=0.31, height=24, width=73
                , bordermode='ignore')
        self.TLabel4.configure(background="#d9d9d9")
        self.TLabel4.configure(foreground="#000000")
        self.TLabel4.configure(font="TkDefaultFont")
        self.TLabel4.configure(relief="flat")
        self.TLabel4.configure(anchor='w')
        self.TLabel4.configure(justify='left')
        self.TLabel4.configure(text='''Cantidad:''')

        self.lblCantidadDestino = ttk.Label(self.Labelframe1_2)
        self.lblCantidadDestino.place(relx=0.761, rely=0.31, height=24, width=45
                , bordermode='ignore')
        self.lblCantidadDestino.configure(background="#d9d9d9")
        self.lblCantidadDestino.configure(foreground="#000000")
        self.lblCantidadDestino.configure(font="TkDefaultFont")
        self.lblCantidadDestino.configure(relief="flat")
        self.lblCantidadDestino.configure(anchor='w')
        self.lblCantidadDestino.configure(justify='left')
        self.lblCantidadDestino.configure(text='''0''')

        self.Labelframe1_3 = tk.LabelFrame(top)
        self.Labelframe1_3.place(relx=0.04, rely=0.756, relheight=0.222
                , relwidth=0.92)
        self.Labelframe1_3.configure(relief='groove')
        self.Labelframe1_3.configure(foreground="black")
        self.Labelframe1_3.configure(text='''Buscador de Diputados''')
        self.Labelframe1_3.configure(background="#d9d9d9")
        self.Labelframe1_3.configure(highlightbackground="#d9d9d9")
        self.Labelframe1_3.configure(highlightcolor="black")

        self.Label4 = tk.Label(self.Labelframe1_3)
        self.Label4.place(relx=0.076, rely=0.18, height=26, width=92
                , bordermode='ignore')
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Diputado ID:''')

        self.Label5 = tk.Label(self.Labelframe1_3)
        self.Label5.place(relx=0.065, rely=0.36, height=26, width=141
                , bordermode='ignore')
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''Nombre Completo:''')

        self.Label6 = tk.Label(self.Labelframe1_3)
        self.Label6.place(relx=0.065, rely=0.541, height=26, width=122
                , bordermode='ignore')
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''Provincia:''')

        self.Label7 = tk.Label(self.Labelframe1_3)
        self.Label7.place(relx=0.076, rely=0.766, height=26, width=133
                , bordermode='ignore')
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(text='''Cantidad de Viajes:''')

        self.Label8 = tk.Label(self.Labelframe1_3)
        self.Label8.place(relx=0.522, rely=0.18, height=26, width=56
                , bordermode='ignore')
        self.Label8.configure(background="#d9d9d9")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(text='''Bloque:''')

        self.Label9 = tk.Label(self.Labelframe1_3)
        self.Label9.place(relx=0.511, rely=0.405, height=26, width=93
                , bordermode='ignore')
        self.Label9.configure(background="#d9d9d9")
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(foreground="#000000")
        self.Label9.configure(text='''Año Inicio:''')

if __name__ == '__main__':
    vp_start_gui()





