import Tkinter
import tkFont


# def func1():
#     label1.config(text='you choose iphoneXS')
#
#
# def func2():
#     label1.config(text="you choose iphoneXR")


def func():
    if sel1.get() == 1:
        label1.config(text='You choose iphoneXS')
    elif sel1.get() == 2:
        label1.config(text="You choose iphoneXR")


top = Tkinter.Tk()
sel1 = Tkinter.IntVar()
sel1.set(2)
myFont = tkFont.Font(family="Arial", size=24)
label1 = Tkinter.Label(top, text="Your choice", font=myFont)
label1.pack()
radioButton1 = Tkinter.Radiobutton(top, text="iphoneXS",
                                   font=myFont,
                                   variable=sel1,
                                   value=1,
                                   command=func)
radioButton1.pack()
radioButton2 = Tkinter.Radiobutton(top, text="iphoneXR",
                                   font=myFont,
                                   variable=sel1,
                                   value=2,
                                   command=func)
radioButton2.pack()


top.maxsize(350, 200)
top.minsize(350, 200)
top.mainloop()
