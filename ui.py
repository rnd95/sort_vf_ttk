#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

#  in conjunction with Tcl version 8.6


import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

_location = os.path.dirname(__file__)

import ui_support

_bgcolor = '#d9d9d9'
_fgcolor = '#000000'
_tabfg1 = 'black' 
_tabfg2 = 'white' 
_bgmode = 'light' 
_tabbg1 = '#d9d9d9' 
_tabbg2 = 'gray40' 

_style_code_ran = 0
def _style_code():
    global _style_code_ran
    if _style_code_ran: return        
    try: ui_support.root.tk.call('source',
                os.path.join(_location, 'themes', 'default.tcl'))
    except: pass
    style = ttk.Style()
    style.theme_use('default')
    style.configure('.', font = "TkDefaultFont")
    if sys.platform == "win32":
       style.theme_use('winnative')    
    _style_code_ran = 1
    print("in conjunction with Tcl version 8.6\nApr 17, 2024 12:54:17 PM EEST  platform: Windows NT\nBuild EXE May 01, 2024 09:40:59 AM")
    print("Список районов (папки)", ui_support.district_folders)
    
class SortVF_UI:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        top.geometry("275x259+658+253")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("Сортування")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="#000000")

        self.top = top
        self.che49 = tk.IntVar()

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        _style_code()
        self.SortVF_instance = ui_support.SortVF(ui_support.district_folders)


        self.Label_SheetType = tk.Label(self.top)
        self.Label_SheetType.place(relx=0.109, rely=0.193, height=30, width=128)
        self.Label_SheetType.configure(activebackground="#d9d9d9")
        self.Label_SheetType.configure(activeforeground="black")
        self.Label_SheetType.configure(anchor='w')
        self.Label_SheetType.configure(background="#d9d9d9")
        self.Label_SheetType.configure(compound='left')
        self.Label_SheetType.configure(disabledforeground="#a3a3a3")
        self.Label_SheetType.configure(font="-family {Segoe UI} -size 14")
        self.Label_SheetType.configure(foreground="#000000")
        self.Label_SheetType.configure(highlightbackground="#d9d9d9")
        self.Label_SheetType.configure(highlightcolor="#000000")
        self.Label_SheetType.configure(text='''Тип відомості:''')

        self.Entry_SheetType = tk.Entry(self.top)
        self.Entry_SheetType.place(relx=0.618, rely=0.193, height=30
                , relwidth=0.196)
        self.Entry_SheetType.configure(background="white")
        self.Entry_SheetType.configure(disabledforeground="#a3a3a3")
        self.Entry_SheetType.configure(font="-family {Segoe UI} -size 15")
        self.Entry_SheetType.configure(foreground="#000000")
        self.Entry_SheetType.configure(highlightbackground="#d9d9d9")
        self.Entry_SheetType.configure(highlightcolor="#000000")
        self.Entry_SheetType.configure(insertbackground="#000000")
        self.Entry_SheetType.configure(selectbackground="#d9d9d9")
        self.Entry_SheetType.configure(selectforeground="black")

        self.Label_SheetType = tk.Label(self.top)
        self.Label_SheetType.place(relx=0.109, rely=0.193, height=30, width=128)
        self.Label_SheetType.configure(activebackground="#d9d9d9")
        self.Label_SheetType.configure(activeforeground="black")
        self.Label_SheetType.configure(anchor='w')
        self.Label_SheetType.configure(background="#d9d9d9")
        self.Label_SheetType.configure(compound='left')
        self.Label_SheetType.configure(disabledforeground="#a3a3a3")
        self.Label_SheetType.configure(font="-family {Segoe UI} -size 14")
        self.Label_SheetType.configure(foreground="#000000")
        self.Label_SheetType.configure(highlightbackground="#d9d9d9")
        self.Label_SheetType.configure(highlightcolor="#000000")
        self.Label_SheetType.configure(text='''Тип відомості:''')

        self.Entry_SheetType = tk.Entry(self.top)
        self.Entry_SheetType.place(relx=0.618, rely=0.193, height=30
                , relwidth=0.196)
        self.Entry_SheetType.configure(background="white")
        self.Entry_SheetType.configure(disabledforeground="#a3a3a3")
        self.Entry_SheetType.configure(font="-family {Segoe UI} -size 15")
        self.Entry_SheetType.configure(foreground="#000000")
        self.Entry_SheetType.configure(highlightbackground="#d9d9d9")
        self.Entry_SheetType.configure(highlightcolor="#000000")
        self.Entry_SheetType.configure(insertbackground="#000000")
        self.Entry_SheetType.configure(selectbackground="#d9d9d9")
        self.Entry_SheetType.configure(selectforeground="black")

        self.Button_SortBank = tk.Button(self.top, command=lambda: self.SortVF_instance.Method_Bank(self.Get_SheetType()))
        self.Button_SortBank.place(relx=0.182, rely=0.695, height=46, width=187)
        self.Button_SortBank.configure(activebackground="#d9d9d9")
        self.Button_SortBank.configure(activeforeground="black")
        self.Button_SortBank.configure(background="#d9d9d9")
        self.Button_SortBank.configure(cursor="arrow")
        self.Button_SortBank.configure(disabledforeground="#a3a3a3")
        self.Button_SortBank.configure(font="-family {Segoe UI} -size 9")
        self.Button_SortBank.configure(foreground="#000000")
        self.Button_SortBank.configure(highlightbackground="#d9d9d9")
        self.Button_SortBank.configure(highlightcolor="#000000")
        self.Button_SortBank.configure(text='''Сортування банків''')

        self.Button_SortPost = tk.Button(self.top, command=lambda: self.SortVF_instance.Method_Post(self.Get_SheetType(), self.Get_Month()))
        self.Button_SortPost.place(relx=0.182, rely=0.463, height=46, width=187)
        self.Button_SortPost.configure(activebackground="#d9d9d9")
        self.Button_SortPost.configure(activeforeground="black")
        self.Button_SortPost.configure(background="#d9d9d9")
        self.Button_SortPost.configure(cursor="arrow")
        self.Button_SortPost.configure(disabledforeground="#a3a3a3")
        self.Button_SortPost.configure(font="-family {Segoe UI} -size 9")
        self.Button_SortPost.configure(foreground="#000000")
        self.Button_SortPost.configure(highlightbackground="#d9d9d9")
        self.Button_SortPost.configure(highlightcolor="#000000")
        self.Button_SortPost.configure(text='''Сортування пошти''')
        self.Entry_SheetType.configure(validate='key')
        self.Entry_SheetType.configure(validatecommand=(self.Entry_SheetType.register(validate_entry), '%P'))

        self.Entry_Month = tk.Entry(self.top)
        self.Entry_Month.place(relx=0.618, rely=0.039, height=30, relwidth=0.196)

        self.Entry_Month.configure(background="white")
        self.Entry_Month.configure(disabledforeground="#a3a3a3")
        self.Entry_Month.configure(font="-family {Segoe UI} -size 15")
        self.Entry_Month.configure(foreground="#000000")
        self.Entry_Month.configure(highlightbackground="#d9d9d9")
        self.Entry_Month.configure(highlightcolor="#000000")
        self.Entry_Month.configure(insertbackground="#000000")
        self.Entry_Month.configure(selectbackground="#d9d9d9")
        self.Entry_Month.configure(selectforeground="black")
        self.Entry_Month.configure(validatecommand=(self.Entry_SheetType.register(validate_entry), '%P'))

        self.Label_Month = tk.Label(self.top)
        self.Label_Month.place(relx=0.109, rely=0.039, height=30, width=128)
        self.Label_Month.configure(activebackground="#d9d9d9")
        self.Label_Month.configure(activeforeground="black")
        self.Label_Month.configure(anchor='w')
        self.Label_Month.configure(background="#d9d9d9")
        self.Label_Month.configure(compound='left')
        self.Label_Month.configure(disabledforeground="#a3a3a3")
        self.Label_Month.configure(font="-family {Segoe UI} -size 14")
        self.Label_Month.configure(foreground="#000000")
        self.Label_Month.configure(highlightbackground="#d9d9d9")
        self.Label_Month.configure(highlightcolor="#000000")
        self.Label_Month.configure(text='''Місяць:''')

# Get Value from Entry (funcs)
    def Get_SheetType(self):
        return self.Entry_SheetType.get()
    def Get_Month(self):
        return self.Entry_Month.get()

def validate_entry(text):
    return len(text) <= 3

def start_up():
    ui_support.main()

if __name__ == '__main__':
    ui_support.main()




