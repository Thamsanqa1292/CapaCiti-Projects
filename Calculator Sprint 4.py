# -*- coding: utf-8 -*-
"""
Created on Thu June 25 09:27:52 2020

@author: Thamsanqa
"""
from tkinter import *
from CalcLogic import *
import math

def Add():
    n = num1.get()
    n1 = num2.get()
    results = int(n) + int(n1)
    Label(calc,text = results).pack()
    

def Subtract():
    t = num1.get()
    t1 = num2.get()
    results = int(t) - int(t1)
    Label(calc,text = results).pack()
    
def Divide():
    t = num1.get()
    t1 = num2.get()
    results = int(t) / int(t1)
    Label(calc,text = results).pack()

def Multiply():
    t = num1.get()
    t1 = num2.get()
    results = int(t) * int(t1)
    Label(calc,text = results).pack()
    

    
calc = Tk()
num1 = StringVar()
num2 = StringVar()
#Create a title for our form
calc.title("Welcome to Thamsanqa Dube Calculations")
#Defines the minimum width and height of our form
calc.minsize(width = 400,height = 350)
#Defines maximum height and width of our form
calc.maxsize(width = 500,height = 400)
#Used to create labels on the form
Label(calc,text = "Enter First Number:", width = 30).pack()
#Entry is used to create a textbox
Entry(calc,width = 30, textvariable = num1).pack()

Label(calc,text = "Enter Second Number:", width = 30).pack()
Entry(calc,width = 30, textvariable = num2).pack()
#Button used to trigger an event
button = Button(calc, text = "Add",command = Add, width = 20,bg = "black", fg = "white").pack()
button = Button(calc, text = "Subtract",command = Subtract, width = 20,bg = "grey",fg = "white").pack()
button = Button(calc, text = "Divide",command = Divide, width = 20,bg = "black", fg = "white").pack()
button = Button(calc, text = "Multiply",command = Multiply, width = 20,bg = "grey",fg = "white").pack()
button = Button(calc, text = "Click to Exit",command = calc.destroy, width = 20,bg = "black", fg = "white").pack()
calc.mainloop()