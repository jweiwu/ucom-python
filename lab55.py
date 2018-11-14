import Tkinter
import tkFont


def func1(val):
    label1.config(text="Scale value = %d" % int(val))


top = Tkinter.Tk()
sel1 = Tkinter.IntVar()
sel1.set(25)

string1 = "value=%d"
myFont = tkFont.Font(family="Arial", size=24)

label1 = Tkinter.Label(top, text="Your choice", font=myFont)
label1.pack()
scale1 = Tkinter.Scale(top, font=myFont, variable=sel1, orient='h',
                       from_=0, to=100, command=func1, showvalue=False)
scale1.pack(fill=Tkinter.BOTH, expand=1)

top.maxsize(300, 80)
top.minsize(300, 80)
top.mainloop()
