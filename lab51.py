import Tkinter
import tkFont

counter = 0


class Foo:
    def __init__(self, counter):
        self.counter = counter


f1 = Foo(0)


def ClickMe():
    global counter
    counter += 1
    label1.config(text="Button1 clicked %d times" % counter, bg="#FFF", fg="#000")


def ClickMe2():
    label1.config(text="Button2 Clicked")


def ClickMe3():
    f1.counter = f1.counter + 1
    label1.config(text="Button3 Clicked % d times" % f1.counter, fg="#FFF", bg="#000")


def func1(ev):
    label1.config(text='enter event', fg='#F00')


def func2(ev):
    label1.config(text="leave event", fg='#0F0')


top = Tkinter.Tk()
myFont = tkFont.Font(family="Arial", size=28)
label1 = Tkinter.Label(top, text="Display", font=myFont)
button1 = Tkinter.Button(top, text="Click Me 1!", font=myFont, command=ClickMe)
button2 = Tkinter.Button(top, text="Click Me 2!", font=myFont, command=ClickMe2)
button3 = Tkinter.Button(top, text="Click Me 3!", font=myFont, command=ClickMe3)

label1.pack()
button1.pack()
button2.pack()
button3.pack()

button1.bind('<Leave>', func2)
button1.bind('<Enter>', func1)

top.minsize(400, 300)
top.maxsize(400, 300)
top.mainloop()
