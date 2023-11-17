from tkinter import *
from time import strftime

clock = Tk()
clock.title("DIGITAL CLOCK")

lbl = Label(clock, font="arial 168 bold", bg="#fbad00",fg="white")
lbl.pack(anchor="center", fill="both", expand="yes")

def time():
    string = strftime(" %H:%M:%S %p")
    lbl.config(text=string)
    lbl.after(1000, time)

time()
mainloop()