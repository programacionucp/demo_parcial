#############################################################################
# Generated by PAGE version 5.0.3
#  in conjunction with Tcl version 8.6
#  Jun 01, 2020 05:45:20 PM -03  platform: Windows NT
set vTcl(timestamp) ""


if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(pr,menufgcolor) #000000
set vTcl(pr,menubgcolor) #d9d9d9
set vTcl(pr,menuanalogcolor) #ececec
set vTcl(pr,treehighlight) firebrick
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
}




proc vTclWindow.top43 {base} {
    global vTcl
    if {$base == ""} {
        set base .top43
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 1000x1000+575+0
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1924 1055
    wm minsize $top 148 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "New Toplevel"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    labelframe $top.lab45 \
        -font TkDefaultFont -foreground black \
        -text {Cantidad de Diputados por Provincia} \
        -background $vTcl(actual_gui_bg) -height 225 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 920 
    vTcl:DefineAlias "$top.lab45" "Labelframe1" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.lab45
    label $site_3_0.lab44 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) -text Provincia 
    vTcl:DefineAlias "$site_3_0.lab44" "Label1" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab45 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Cantidad: 
    vTcl:DefineAlias "$site_3_0.lab45" "Label1_1" vTcl:WidgetProc "Toplevel1" 1
    ttk::combobox $site_3_0.tCo46 \
        -font TkTextFont -textvariable combobox -foreground {} -background {} \
        -takefocus {} 
    vTcl:DefineAlias "$site_3_0.tCo46" "TCombobox1" vTcl:WidgetProc "Toplevel1" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_3_0.tBu47 \
        -command calcularCantxProvincia -takefocus {} -text CALCULAR 
    vTcl:DefineAlias "$site_3_0.tBu47" "TButton1" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab48 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -relief sunken 
    vTcl:DefineAlias "$site_3_0.lab48" "lblCantProvincia" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.lab44 \
        -in $site_3_0 -x 0 -relx 0.065 -y 0 -rely 0.222 -width 0 \
        -relwidth 0.078 -height 0 -relheight 0.111 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab45 \
        -in $site_3_0 -x 0 -relx 0.554 -y 0 -rely 0.222 -width 0 \
        -relwidth 0.078 -height 0 -relheight 0.111 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tCo46 \
        -in $site_3_0 -x 0 -relx 0.152 -y 0 -rely 0.222 -width 0 \
        -relwidth 0.202 -height 0 -relheight 0.111 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tBu47 \
        -in $site_3_0 -x 0 -relx 0.402 -y 0 -rely 0.178 -width 98 -relwidth 0 \
        -height 45 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab48 \
        -in $site_3_0 -x 0 -relx 0.652 -y 0 -rely 0.222 -width 0 \
        -relwidth 0.078 -height 0 -relheight 0.111 -anchor nw \
        -bordermode ignore 
    labelframe $top.lab47 \
        -font TkDefaultFont -foreground black \
        -text {Cantidad de Diputados por Bloques Politicos} \
        -background $vTcl(actual_gui_bg) -height 180 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 920 
    vTcl:DefineAlias "$top.lab47" "Labelframe1_1" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.lab47
    ttk::label $site_3_0.tLa49 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font TkDefaultFont -relief flat -anchor w -justify left \
        -text Bloque: 
    vTcl:DefineAlias "$site_3_0.tLa49" "TLabel1" vTcl:WidgetProc "Toplevel1" 1
    ttk::label $site_3_0.tLa50 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font TkDefaultFont -relief flat -anchor w -justify left \
        -text Hombres: 
    vTcl:DefineAlias "$site_3_0.tLa50" "TLabel2" vTcl:WidgetProc "Toplevel1" 1
    ttk::label $site_3_0.tLa51 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font TkDefaultFont -relief flat -anchor w -justify left \
        -text Mujeres: 
    vTcl:DefineAlias "$site_3_0.tLa51" "TLabel3" vTcl:WidgetProc "Toplevel1" 1
    ttk::label $site_3_0.tLa52 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font TkDefaultFont -relief flat -anchor w -justify left -text 0 
    vTcl:DefineAlias "$site_3_0.tLa52" "lblHombres" vTcl:WidgetProc "Toplevel1" 1
    ttk::label $site_3_0.tLa53 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font TkDefaultFont -relief flat -anchor w -justify left -text 0 
    vTcl:DefineAlias "$site_3_0.tLa53" "lblMujeres" vTcl:WidgetProc "Toplevel1" 1
    ttk::entry $site_3_0.tEn54 \
        -font TkTextFont -foreground {} -background {} -takefocus {} \
        -cursor ibeam 
    vTcl:DefineAlias "$site_3_0.tEn54" "entryBloque" vTcl:WidgetProc "Toplevel1" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_3_0.tBu55 \
        -command calcularBloque -takefocus {} -text CALCULAR 
    vTcl:DefineAlias "$site_3_0.tBu55" "TButton2" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.tLa49 \
        -in $site_3_0 -x 0 -relx 0.065 -y 0 -rely 0.265 -height 0 \
        -relheight 0.106 -anchor nw -bordermode ignore 
    place $site_3_0.tLa50 \
        -in $site_3_0 -x 0 -relx 0.576 -y 0 -rely 0.265 -width 0 \
        -relwidth 0.082 -height 0 -relheight 0.106 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tLa51 \
        -in $site_3_0 -x 0 -relx 0.576 -y 0 -rely 0.487 -width 0 \
        -relwidth 0.071 -height 0 -relheight 0.106 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tLa52 \
        -in $site_3_0 -x 0 -relx 0.717 -y 0 -rely 0.265 -width 0 \
        -relwidth 0.046 -height 0 -relheight 0.106 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tLa53 \
        -in $site_3_0 -x 0 -relx 0.717 -y 0 -rely 0.487 -width 0 \
        -relwidth 0.06 -height 0 -relheight 0.106 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tEn54 \
        -in $site_3_0 -x 0 -relx 0.141 -y 0 -rely 0.265 -height 0 \
        -relheight 0.115 -anchor nw -bordermode ignore 
    place $site_3_0.tBu55 \
        -in $site_3_0 -x 0 -relx 0.391 -y 0 -rely 0.265 -height 30 \
        -relheight 0 -anchor nw -bordermode ignore 
    labelframe $top.lab48 \
        -font TkDefaultFont -foreground black -text {Cantidad de Viajes} \
        -background $vTcl(actual_gui_bg) -height 180 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 920 
    vTcl:DefineAlias "$top.lab48" "Labelframe1_2" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.lab48
    label $site_3_0.lab56 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) -text Origen: 
    vTcl:DefineAlias "$site_3_0.lab56" "Label2" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab57 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -text {Destino: } 
    vTcl:DefineAlias "$site_3_0.lab57" "Label3" vTcl:WidgetProc "Toplevel1" 1
    ttk::combobox $site_3_0.tCo58 \
        -font TkTextFont -textvariable combobox2 -foreground {} \
        -background {} -takefocus {} 
    vTcl:DefineAlias "$site_3_0.tCo58" "TCombobox2" vTcl:WidgetProc "Toplevel1" 1
    ttk::combobox $site_3_0.tCo59 \
        -font TkTextFont -textvariable combobox3 -foreground {} \
        -background {} -takefocus {} 
    vTcl:DefineAlias "$site_3_0.tCo59" "TCombobox3" vTcl:WidgetProc "Toplevel1" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_3_0.tBu60 \
        -command calcularCantDestino -takefocus {} -text CALCULAR 
    vTcl:DefineAlias "$site_3_0.tBu60" "TButton3" vTcl:WidgetProc "Toplevel1" 1
    ttk::label $site_3_0.tLa61 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font TkDefaultFont -relief flat -anchor w -justify left \
        -text Cantidad: 
    vTcl:DefineAlias "$site_3_0.tLa61" "TLabel4" vTcl:WidgetProc "Toplevel1" 1
    ttk::label $site_3_0.tLa62 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font TkDefaultFont -relief flat -anchor w -justify left -text 0 
    vTcl:DefineAlias "$site_3_0.tLa62" "lblCantidadDestino" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.lab56 \
        -in $site_3_0 -x 0 -relx 0.087 -y 0 -rely 0.221 -width 0 \
        -relwidth 0.067 -height 0 -relheight 0.115 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab57 \
        -in $site_3_0 -x 0 -relx 0.087 -y 0 -rely 0.442 -width 0 \
        -relwidth 0.07 -height 0 -relheight 0.115 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tCo58 \
        -in $site_3_0 -x 0 -relx 0.174 -y 0 -rely 0.221 -width 0 \
        -relwidth 0.203 -height 0 -relheight 0.115 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tCo59 \
        -in $site_3_0 -x 0 -relx 0.174 -y 0 -rely 0.442 -width 0 \
        -relwidth 0.203 -height 0 -relheight 0.115 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tBu60 \
        -in $site_3_0 -x 0 -relx 0.446 -y 0 -rely 0.31 -height 30 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tLa61 \
        -in $site_3_0 -x 0 -relx 0.652 -y 0 -rely 0.31 -width 0 \
        -relwidth 0.08 -height 0 -relheight 0.106 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tLa62 \
        -in $site_3_0 -x 0 -relx 0.761 -y 0 -rely 0.31 -width 0 \
        -relwidth 0.049 -height 0 -relheight 0.106 -anchor nw \
        -bordermode ignore 
    labelframe $top.lab50 \
        -font TkDefaultFont -foreground black -text {Buscador de Diputados} \
        -background $vTcl(actual_gui_bg) -height 180 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 920 
    vTcl:DefineAlias "$top.lab50" "Labelframe1_3" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.lab50
    label $site_3_0.lab63 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -text {Diputado ID:} 
    vTcl:DefineAlias "$site_3_0.lab63" "Label4" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab64 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -text {Nombre Completo:} 
    vTcl:DefineAlias "$site_3_0.lab64" "Label5" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab65 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) -text Provincia: 
    vTcl:DefineAlias "$site_3_0.lab65" "Label6" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab66 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -text {Cantidad de Viajes:} 
    vTcl:DefineAlias "$site_3_0.lab66" "Label7" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab67 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) -text Bloque: 
    vTcl:DefineAlias "$site_3_0.lab67" "Label8" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab68 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -text {Año Inicio:} 
    vTcl:DefineAlias "$site_3_0.lab68" "Label9" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent69 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) -insertbackground black -width 144 
    vTcl:DefineAlias "$site_3_0.ent69" "entryID" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab70 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) -text - 
    vTcl:DefineAlias "$site_3_0.lab70" "lblNombre" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab71 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) -text - 
    vTcl:DefineAlias "$site_3_0.lab71" "lblProvincia" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab72 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) -text - 
    vTcl:DefineAlias "$site_3_0.lab72" "lblViajes" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab73 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) -text - 
    vTcl:DefineAlias "$site_3_0.lab73" "lblBloque" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab74 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) -text - 
    vTcl:DefineAlias "$site_3_0.lab74" "lblAnio" vTcl:WidgetProc "Toplevel1" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_3_0.tBu75 \
        -command buscadorDiputados -takefocus {} -text CALCULAR 
    vTcl:DefineAlias "$site_3_0.tBu75" "TButton4" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.lab63 \
        -in $site_3_0 -x 0 -relx 0.076 -y 0 -rely 0.18 -width 0 -relwidth 0.1 \
        -height 0 -relheight 0.117 -anchor nw -bordermode ignore 
    place $site_3_0.lab64 \
        -in $site_3_0 -x 0 -relx 0.065 -y 0 -rely 0.36 -width 0 \
        -relwidth 0.154 -height 0 -relheight 0.117 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab65 \
        -in $site_3_0 -x 0 -relx 0.065 -y 0 -rely 0.541 -width 0 \
        -relwidth 0.133 -height 0 -relheight 0.117 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab66 \
        -in $site_3_0 -x 0 -relx 0.076 -y 0 -rely 0.766 -width 0 \
        -relwidth 0.145 -height 0 -relheight 0.117 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab67 \
        -in $site_3_0 -x 0 -relx 0.522 -y 0 -rely 0.18 -height 0 \
        -relheight 0.117 -anchor nw -bordermode ignore 
    place $site_3_0.lab68 \
        -in $site_3_0 -x 0 -relx 0.511 -y 0 -rely 0.405 -width 0 \
        -relwidth 0.101 -height 0 -relheight 0.117 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent69 \
        -in $site_3_0 -x 0 -relx 0.196 -y 0 -rely 0.18 -width 144 -relwidth 0 \
        -height 24 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab70 \
        -in $site_3_0 -x 0 -relx 0.25 -y 0 -rely 0.36 -width 0 \
        -relwidth 0.176 -height 0 -relheight 0.117 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab71 \
        -in $site_3_0 -x 0 -relx 0.283 -y 0 -rely 0.541 -width 0 \
        -relwidth 0.111 -height 0 -relheight 0.117 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab72 \
        -in $site_3_0 -x 0 -relx 0.283 -y 0 -rely 0.766 -width 0 \
        -relwidth 0.11 -height 0 -relheight 0.117 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab73 \
        -in $site_3_0 -x 0 -relx 0.652 -y 0 -rely 0.18 -width 0 \
        -relwidth 0.046 -height 0 -relheight 0.117 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab74 \
        -in $site_3_0 -x 0 -relx 0.652 -y 0 -rely 0.405 -width 0 \
        -relwidth 0.046 -height 0 -relheight 0.117 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tBu75 \
        -in $site_3_0 -x 0 -relx 0.522 -y 0 -rely 0.676 -height 30 \
        -relheight 0 -anchor nw -bordermode ignore 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.lab45 \
        -in $top -x 0 -relx 0.04 -y 0 -rely 0.03 -width 0 -relwidth 0.92 \
        -height 0 -relheight 0.225 -anchor nw -bordermode ignore 
    place $top.lab47 \
        -in $top -x 0 -relx 0.04 -y 0 -rely 0.27 -width 0 -relwidth 0.92 \
        -height 0 -relheight 0.226 -anchor nw -bordermode ignore 
    place $top.lab48 \
        -in $top -x 0 -relx 0.04 -y 0 -rely 0.522 -width 0 -relwidth 0.92 \
        -height 0 -relheight 0.226 -anchor nw -bordermode ignore 
    place $top.lab50 \
        -in $top -x 0 -relx 0.04 -y 0 -rely 0.76 -width 0 -relwidth 0.92 \
        -height 0 -relheight 0.222 -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top43 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

