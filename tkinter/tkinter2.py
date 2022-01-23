from tkinter import *

win = Tk()
f = Frame(win)

b1 = Button(f, text= "One")
b2 = Button(f, text= "Two")
b3 = Button(f, text="Three")

#With “pack,” you tell your widget to pack itself into its parent.
b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=LEFT)

#sets label in the second row with a string
l = Label(win, text="This is a label")
l.pack()
f.pack()

def but1():
    print("Button one was pushed")


b1.configure(command=but1)
