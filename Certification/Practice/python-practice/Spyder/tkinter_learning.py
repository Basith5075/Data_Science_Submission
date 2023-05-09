# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 01:37:11 2022

@author: basit
"""

from tkinter import *
from tkinter import ttk


class HelloWorld:
    
    def name(self):
        return 'Abdul'
    
    def sum(self,firstNum,secNum):
        firstNum = firstNum
        secondNum = secNum
        sumM = firstNum+secondNum
        return sumM

class Test:
        root = Tk()
        frm = ttk.Frame(root, padding=10)
        frm.grid()
        hw = HelloWorld()
        
        ttk.Label(frm, text=hw.name()).grid(column=0, row=0)
        ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
        ttk.Label(frm, text=hw.sum(1, 3)).grid(column=5, row=15)
        root.mainloop()
        
name = Test()