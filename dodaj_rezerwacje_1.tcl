#############################################################################
# Generated by PAGE version 5.3
#  in conjunction with Tcl version 8.6
#  Jun 20, 2020 10:10:27 AM CEST  platform: Windows NT
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
    wm geometry $top 1004x683+294+166
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1924 1061
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "New Toplevel"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    frame $top.fra44 \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 665 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -width 835 
    vTcl:DefineAlias "$top.fra44" "Frame1" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra44
    ttk::entry $site_3_0.tEn48 \
        -font TkTextFont -foreground {} -background {} -takefocus {} \
        -cursor ibeam 
    vTcl:DefineAlias "$site_3_0.tEn48" "TEntry_name" vTcl:WidgetProc "Toplevel1" 1
    ttk::entry $site_3_0.tEn50 \
        -font TkTextFont -foreground {} -background {} -takefocus {} \
        -cursor ibeam 
    vTcl:DefineAlias "$site_3_0.tEn50" "TEntry_surname" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab51 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Imię 
    vTcl:DefineAlias "$site_3_0.lab51" "Label1" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab52 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Nazwisko 
    vTcl:DefineAlias "$site_3_0.lab52" "Label1_4" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab53 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Miesiąc 
    vTcl:DefineAlias "$site_3_0.lab53" "Label1_5" vTcl:WidgetProc "Toplevel1" 1
    ttk::entry $site_3_0.tEn54 \
        -font TkTextFont -foreground {} -background {} -takefocus {} \
        -cursor ibeam 
    vTcl:DefineAlias "$site_3_0.tEn54" "TEntry_month" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab55 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Przyjazd 
    vTcl:DefineAlias "$site_3_0.lab55" "Label1_6" vTcl:WidgetProc "Toplevel1" 1
    ttk::entry $site_3_0.tEn56 \
        -font TkTextFont -foreground {} -background {} -takefocus {} \
        -cursor ibeam 
    vTcl:DefineAlias "$site_3_0.tEn56" "TEntry_arrival" vTcl:WidgetProc "Toplevel1" 1
    ttk::entry $site_3_0.tEn57 \
        -font TkTextFont -foreground {} -background {} -takefocus {} \
        -cursor ibeam 
    vTcl:DefineAlias "$site_3_0.tEn57" "TEntry_departure" vTcl:WidgetProc "Toplevel1" 1
    ttk::entry $site_3_0.tEn58 \
        -font TkTextFont -foreground {} -background {} -takefocus {} \
        -cursor ibeam 
    vTcl:DefineAlias "$site_3_0.tEn58" "TEntry_price_total" vTcl:WidgetProc "Toplevel1" 1
    ttk::entry $site_3_0.tEn59 \
        -font TkTextFont -foreground {} -background {} -takefocus {} \
        -cursor ibeam 
    vTcl:DefineAlias "$site_3_0.tEn59" "TEntry_price_ra" vTcl:WidgetProc "Toplevel1" 1
    ttk::entry $site_3_0.tEn60 \
        -font TkTextFont -foreground {} -background {} -takefocus {} \
        -cursor ibeam 
    vTcl:DefineAlias "$site_3_0.tEn60" "TEntry_exp_booking" vTcl:WidgetProc "Toplevel1" 1
    ttk::entry $site_3_0.tEn61 \
        -font TkTextFont -foreground {} -background {} -takefocus {} \
        -cursor ibeam 
    vTcl:DefineAlias "$site_3_0.tEn61" "TEntry_exp_vat" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab62 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Wyjazd 
    vTcl:DefineAlias "$site_3_0.lab62" "Label1_8" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab63 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {Kwota całk} 
    vTcl:DefineAlias "$site_3_0.lab63" "Label1_8" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab64 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {Kwota ra} 
    vTcl:DefineAlias "$site_3_0.lab64" "Label1_8" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab65 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Booking 
    vTcl:DefineAlias "$site_3_0.lab65" "Label1_8" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab66 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {Booking VAT} 
    vTcl:DefineAlias "$site_3_0.lab66" "Label1_7" vTcl:WidgetProc "Toplevel1" 1
    ttk::entry $site_3_0.tEn67 \
        -font TkTextFont -foreground {} -background {} -takefocus {} \
        -cursor ibeam 
    vTcl:DefineAlias "$site_3_0.tEn67" "TEntry_city_tax" vTcl:WidgetProc "Toplevel1" 1
    ttk::entry $site_3_0.tEn68 \
        -font TkTextFont -foreground {} -background {} -takefocus {} \
        -cursor ibeam 
    vTcl:DefineAlias "$site_3_0.tEn68" "TEntry_exp" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab69 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {Podatek miejski} 
    vTcl:DefineAlias "$site_3_0.lab69" "Label1_9" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab70 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Koszty 
    vTcl:DefineAlias "$site_3_0.lab70" "Label1_9" vTcl:WidgetProc "Toplevel1" 1
    ttk::entry $site_3_0.tEn71 \
        -font TkTextFont -foreground {} -background {} -takefocus {} \
        -cursor ibeam 
    vTcl:DefineAlias "$site_3_0.tEn71" "TEntry_gift_price" vTcl:WidgetProc "Toplevel1" 1
    ttk::entry $site_3_0.tEn72 \
        -font TkTextFont -foreground {} -background {} -takefocus {} \
        -cursor ibeam 
    vTcl:DefineAlias "$site_3_0.tEn72" "TEntry_clean_price" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab73 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Prezent 
    vTcl:DefineAlias "$site_3_0.lab73" "Label1_9" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab74 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Sprzątanie 
    vTcl:DefineAlias "$site_3_0.lab74" "Label1_9" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab75 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Apartament 
    vTcl:DefineAlias "$site_3_0.lab75" "Label1_9" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab76 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Depozyt 
    vTcl:DefineAlias "$site_3_0.lab76" "Label1_9" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab77 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Dokument 
    vTcl:DefineAlias "$site_3_0.lab77" "Label1_9" vTcl:WidgetProc "Toplevel1" 1
    ttk::entry $site_3_0.tEn78 \
        -font TkTextFont -foreground {} -background {} -takefocus {} \
        -cursor ibeam 
    vTcl:DefineAlias "$site_3_0.tEn78" "TEntry_place" vTcl:WidgetProc "Toplevel1" 1
    ttk::entry $site_3_0.tEn79 \
        -font TkTextFont -foreground {} -background {} -takefocus {} \
        -cursor ibeam 
    vTcl:DefineAlias "$site_3_0.tEn79" "TEntry_deposit" vTcl:WidgetProc "Toplevel1" 1
    ttk::entry $site_3_0.tEn80 \
        -font TkTextFont -foreground {} -background {} -takefocus {} \
        -cursor ibeam 
    vTcl:DefineAlias "$site_3_0.tEn80" "TEntry_invoice" vTcl:WidgetProc "Toplevel1" 1
    ttk::entry $site_3_0.tEn81 \
        -font TkTextFont -foreground {} -background {} -takefocus {} \
        -cursor ibeam 
    vTcl:DefineAlias "$site_3_0.tEn81" "TEntry_paid" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab82 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Opłacone? 
    vTcl:DefineAlias "$site_3_0.lab82" "Label1_10" vTcl:WidgetProc "Toplevel1" 1
    ttk::entry $site_3_0.tEn83 \
        -font TkTextFont -foreground {} -background {} -takefocus {} \
        -cursor ibeam 
    vTcl:DefineAlias "$site_3_0.tEn83" "TEntry_remaining_pay" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab84 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Dopłata 
    vTcl:DefineAlias "$site_3_0.lab84" "Label1_11" vTcl:WidgetProc "Toplevel1" 1
    ttk::entry $site_3_0.tEn86 \
        -font TkTextFont -foreground {} -background {} -takefocus {} \
        -cursor ibeam 
    vTcl:DefineAlias "$site_3_0.tEn86" "TEntry_commision" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab89 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Prowizja 
    vTcl:DefineAlias "$site_3_0.lab89" "Label1_12" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.tEn48 \
        -in $site_3_0 -x 0 -relx 0.12 -y 0 -rely 0.03 -width 176 -relwidth 0 \
        -height 31 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tEn50 \
        -in $site_3_0 -x 0 -relx 0.12 -y 0 -rely 0.105 -width 0 \
        -relwidth 0.211 -height 0 -relheight 0.047 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab51 \
        -in $site_3_0 -x 0 -relx 0.012 -y 0 -rely 0.03 -width 0 \
        -relwidth 0.077 -height 0 -relheight 0.047 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab52 \
        -in $site_3_0 -x 0 -relx 0.012 -y 0 -rely 0.105 -width 0 \
        -relwidth 0.077 -height 0 -relheight 0.047 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab53 \
        -in $site_3_0 -x 0 -relx 0.012 -y 0 -rely 0.18 -width 0 \
        -relwidth 0.077 -height 0 -relheight 0.047 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tEn54 \
        -in $site_3_0 -x 0 -relx 0.12 -y 0 -rely 0.18 -width 0 \
        -relwidth 0.212 -height 0 -relheight 0.047 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab55 \
        -in $site_3_0 -x 0 -relx 0.012 -y 0 -rely 0.256 -width 0 \
        -relwidth 0.077 -height 0 -relheight 0.048 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tEn56 \
        -in $site_3_0 -x 0 -relx 0.12 -y 0 -rely 0.256 -width 0 \
        -relwidth 0.213 -height 0 -relheight 0.048 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tEn57 \
        -in $site_3_0 -x 0 -relx 0.12 -y 0 -rely 0.331 -width 0 \
        -relwidth 0.213 -height 0 -relheight 0.048 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tEn58 \
        -in $site_3_0 -x 0 -relx 0.12 -y 0 -rely 0.406 -width 0 \
        -relwidth 0.213 -height 0 -relheight 0.048 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tEn59 \
        -in $site_3_0 -x 0 -relx 0.12 -y 0 -rely 0.481 -width 0 \
        -relwidth 0.213 -height 0 -relheight 0.048 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tEn60 \
        -in $site_3_0 -x 0 -relx 0.12 -y 0 -rely 0.556 -width 0 \
        -relwidth 0.213 -height 0 -relheight 0.048 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tEn61 \
        -in $site_3_0 -x 0 -relx 0.12 -y 0 -rely 0.632 -width 0 \
        -relwidth 0.213 -height 0 -relheight 0.048 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab62 \
        -in $site_3_0 -x 0 -relx 0.012 -y 0 -rely 0.331 -width 0 \
        -relwidth 0.077 -height 0 -relheight 0.048 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab63 \
        -in $site_3_0 -x 0 -relx 0.012 -y 0 -rely 0.406 -width 0 \
        -relwidth 0.077 -height 0 -relheight 0.048 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab64 \
        -in $site_3_0 -x 0 -relx 0.012 -y 0 -rely 0.481 -width 0 \
        -relwidth 0.077 -height 0 -relheight 0.048 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab65 \
        -in $site_3_0 -x 0 -relx 0.012 -y 0 -rely 0.556 -width 0 \
        -relwidth 0.077 -height 0 -relheight 0.048 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab66 \
        -in $site_3_0 -x 0 -relx 0.012 -y 0 -rely 0.632 -width 0 \
        -relwidth 0.089 -height 0 -relheight 0.048 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tEn67 \
        -in $site_3_0 -x 0 -relx 0.12 -y 0 -rely 0.707 -width 0 \
        -relwidth 0.213 -height 0 -relheight 0.048 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tEn68 \
        -in $site_3_0 -x 0 -relx 0.12 -y 0 -rely 0.782 -width 0 \
        -relwidth 0.213 -height 0 -relheight 0.048 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab69 \
        -in $site_3_0 -x 0 -relx 0.012 -y 0 -rely 0.707 -width 0 \
        -relwidth 0.1 -height 0 -relheight 0.048 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab70 \
        -in $site_3_0 -x 0 -relx 0.012 -y 0 -rely 0.782 -width 0 \
        -relwidth 0.089 -height 0 -relheight 0.048 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tEn71 \
        -in $site_3_0 -x 0 -relx 0.12 -y 0 -rely 0.857 -width 0 \
        -relwidth 0.213 -height 0 -relheight 0.048 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tEn72 \
        -in $site_3_0 -x 0 -relx 0.12 -y 0 -rely 0.932 -width 0 \
        -relwidth 0.213 -height 0 -relheight 0.048 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab73 \
        -in $site_3_0 -x 0 -relx 0.012 -y 0 -rely 0.857 -width 0 \
        -relwidth 0.089 -height 0 -relheight 0.048 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab74 \
        -in $site_3_0 -x 0 -relx 0.012 -y 0 -rely 0.932 -width 0 \
        -relwidth 0.089 -height 0 -relheight 0.048 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab75 \
        -in $site_3_0 -x 0 -relx 0.347 -y 0 -rely 0.03 -width 0 \
        -relwidth 0.089 -height 0 -relheight 0.048 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab76 \
        -in $site_3_0 -x 0 -relx 0.347 -y 0 -rely 0.105 -width 0 \
        -relwidth 0.089 -height 0 -relheight 0.048 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab77 \
        -in $site_3_0 -x 0 -relx 0.347 -y 0 -rely 0.18 -width 0 \
        -relwidth 0.089 -height 0 -relheight 0.048 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tEn78 \
        -in $site_3_0 -x 0 -relx 0.455 -y 0 -rely 0.03 -width 0 \
        -relwidth 0.211 -height 0 -relheight 0.047 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tEn79 \
        -in $site_3_0 -x 0 -relx 0.455 -y 0 -rely 0.105 -width 0 \
        -relwidth 0.211 -height 0 -relheight 0.047 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tEn80 \
        -in $site_3_0 -x 0 -relx 0.455 -y 0 -rely 0.18 -width 0 \
        -relwidth 0.211 -height 0 -relheight 0.047 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tEn81 \
        -in $site_3_0 -x 0 -relx 0.455 -y 0 -rely 0.256 -width 0 \
        -relwidth 0.211 -height 0 -relheight 0.047 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab82 \
        -in $site_3_0 -x 0 -relx 0.347 -y 0 -rely 0.256 -width 0 \
        -relwidth 0.089 -height 0 -relheight 0.048 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tEn83 \
        -in $site_3_0 -x 0 -relx 0.455 -y 0 -rely 0.331 -width 0 \
        -relwidth 0.212 -height 0 -relheight 0.047 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab84 \
        -in $site_3_0 -x 0 -relx 0.347 -y 0 -rely 0.331 -width 0 \
        -relwidth 0.089 -height 0 -relheight 0.048 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tEn86 \
        -in $site_3_0 -x 0 -relx 0.455 -y 0 -rely 0.406 -width 0 \
        -relwidth 0.213 -height 0 -relheight 0.047 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab89 \
        -in $site_3_0 -x 0 -relx 0.347 -y 0 -rely 0.406 -width 0 \
        -relwidth 0.089 -height 0 -relheight 0.048 -anchor nw \
        -bordermode ignore 
    button $top.but45 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Wczytaj 
    vTcl:DefineAlias "$top.but45" "Home" vTcl:WidgetProc "Toplevel1" 1
    button $top.but46 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Zapisz 
    vTcl:DefineAlias "$top.but46" "Reservation" vTcl:WidgetProc "Toplevel1" 1
    button $top.but47 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Anuluj 
    vTcl:DefineAlias "$top.but47" "Button1_2" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.fra44 \
        -in $top -x 0 -relx 0.159 -y 0 -rely 0.015 -width 0 -relwidth 0.833 \
        -height 0 -relheight 0.974 -anchor nw -bordermode ignore 
    place $top.but45 \
        -in $top -x 0 -relx 0.01 -y 0 -rely 0.015 -width 137 -relwidth 0 \
        -height 34 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but46 \
        -in $top -x 0 -relx 0.01 -y 0 -rely 0.088 -width 137 -relwidth 0 \
        -height 34 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but47 \
        -in $top -x 0 -relx 0.01 -y 0 -rely 0.161 -width 137 -relwidth 0 \
        -height 34 -relheight 0 -anchor nw -bordermode ignore 
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

