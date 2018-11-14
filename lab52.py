import Tkinter
import tkFont


def func1(ev):
    label1.config(text="left single click")


def func2(ev):
    label1.config(text="right double click")


def func3(ev):
    label1.config(text='mid button drag')


top = Tkinter.Tk()
myFont = tkFont.Font(family="Arial", size=32)
label1 = Tkinter.Label(top, text="display", font=myFont)
button1 = Tkinter.Button(top, text="Click Me!", font=myFont)
label1.pack()
button1.pack()
button1.bind('<Button-1>', func1)
button1.bind('<Double-3>', func2)
button1.bind('<B2-Motion>', func3)
top.mainloop()
