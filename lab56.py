import Tkinter
import tkFont


def updateText(ev):
    label1.config(text='Result: %s' % entry1.get())


top = Tkinter.Tk()
myFont = tkFont.Font(family="Arial", size=24)

label1 = Tkinter.Label(top, text="Input Something...", font=myFont)
label1.pack()
entry1 = Tkinter.Entry(top, font=myFont)
entry1.pack()
entry1.bind('<Return>', updateText)
button1 = Tkinter.Button(top, text="Submit", font=myFont)
button1.pack()
button1.bind('<Button-1>', updateText)
top.mainloop()
