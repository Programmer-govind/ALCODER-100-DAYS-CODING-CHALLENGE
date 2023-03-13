#made a digital clock

import turtle
from tkinter import *
from tkinter.ttk import *
from time import strftime
a=Tk()
s=turtle.Screen()
s.bgcolor('black')
a.title('Clock')
b=("/storage/emulated/0/DCIM/DIGITAL.TXT")

def time():
    string=strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000,time)
    
label=Label(a,font=('Arial',50),background='black',foreground='red',)
label.pack(anchor='center')
time()

   
mainloop()