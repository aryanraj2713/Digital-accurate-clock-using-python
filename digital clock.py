
import time
from tkinter import *

root = Tk()
root.title("Digital Clock : ---Aryan Raj")
root.resizable()
lbl = Label(root)
lbl.grid(row=0, column=0)


def display():
    time_get = time.strftime("%Y/%m/%d\n%I:%M:%S %p")
    lbl.config(text=time_get, bg='black', fg='red',
               font=('Butterbelly', 100, 'bold'))
    lbl.after(200, display)


display()
root.mainloop()
