import random as ran
from tkinter import *

root=Tk()
root.geometry("700x450")

l1=Label(root,text='',font=("times",200))

# using unicode characters

def roll():
    number=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    l1.config(text=f'{ran.choice(number)}{ran.choice(number)}')
    l1.pack()
b1=Button(root,text="click to roll !",bg="blue",fg="white",command=roll)
b1.place(x=330,y=0)

root.mainloop()
