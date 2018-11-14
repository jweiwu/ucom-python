import Tkinter
import tkFont


def f1(ev):
    message1.config(text=str % (ev.x, ev.y))


top = Tkinter.Tk()

myFont = tkFont.Font(family="Arial", size=32)

str = 'Move to [ %d, %d ]'

message1 = Tkinter.Message(top, text=str % (0, 0), width=500, font=myFont)
label1 = Tkinter.Label(top, text="Region", font=myFont, padx=30, pady=30, bg='#FF0')

message1.pack()
label1.pack()

label1.bind('<Motion>', f1)

top.minsize(500, 200)
top.maxsize(500, 200)

top.mainloop()
