# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 23:42:57 2023
simple calculator built using python and tkinter gui
@author: 91913
"""

import tkinter as tk

root=tk.Tk()

calculation = ""

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

def add(symbol):
    global calculation
    calculation = calculation + str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,calculation)
    
def evaluate_calculation():
    global calculation
    try:
        calculation=str(eval(calculation))
        text_result.delete(1.0,"end")
        text_result.insert(1.0,calculation)
    except:
        clear_field()
        text_result.insert(1.0,Error)
        
    
    
text_result = tk.Text(root,height=2,width=19,font=("Arial",22))
text_result.grid(columnspan=5)
                                                                                                                                

bt1=tk.Button(root,text="1",width=5,height=5,font=("Arial",7),command=lambda:add(1))
bt2=tk.Button(root,text="2",width=5,height=5,font=("Arial",7),command=lambda:add(2))
bt3=tk.Button(root,text="3",width=5,height=5,font=("Arial",7),command=lambda:add(3))
bt4=tk.Button(root,text="4",width=5,height=5,font=("Arial",7),command=lambda:add(4))
bt5=tk.Button(root,text="5",width=5,height=5,font=("Arial",7),command=lambda:add(5))
bt6=tk.Button(root,text="6",width=5,height=5,font=("Arial",7),command=lambda:add(6))
bt7=tk.Button(root,text="7",width=5,height=5,font=("Arial",7),command=lambda:add(7))
bt8=tk.Button(root,text="8",width=5,height=5,font=("Arial",7),command=lambda:add(8))
bt9=tk.Button(root,text="9",width=5,height=5,font=("Arial",7),command=lambda:add(9))
bt0=tk.Button(root,text="0",width=5,height=5,font=("Arial",7),command=lambda:add(0))
btadd=tk.Button(root,text="+",width=5,height=5,font=("Arial",7),command=lambda:add("+"))
btsub=tk.Button(root,text="-",width=5,height=5,font=("Arial",7),command=lambda:add("-"))
btmul=tk.Button(root,text="x",width=5,height=5,font=("Arial",7),command=lambda:add("x"))
btdiv=tk.Button(root,text="/",width=5,height=5,font=("Arial",7),command=lambda:add("/"))
btequal=tk.Button(root,text="=",width=5,height=5,font=("Arial",7),command=evaluate_calculation)
btclear=tk.Button(root,text="c",width=5,height=5,font=("Arial",7),command=clear_field)


bt1.grid(row=2,column=0)
bt2.grid(row=2,column=1)
bt3.grid(row=2,column=2)
bt4.grid(row=3,column=0)
bt5.grid(row=3,column=1)
bt6.grid(row=3,column=2)
bt7.grid(row=4,column=0)
bt8.grid(row=4,column=1)
bt9.grid(row=4,column=2)
bt0.grid(row=5,column=1)
btadd.grid(row=6,column=0)
btsub.grid(row=6,column=1)
btmul.grid(row=6,column=2)
btdiv.grid(row=6,column=3)
btequal.grid(row=5,column=2)
btclear.grid(row=5,column=0)


root.geometry("300x450")
root.mainloop()


