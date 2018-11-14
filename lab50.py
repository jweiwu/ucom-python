# encoding=UTF8
import Tkinter
import tkFont

top = Tkinter.Tk()
myFont = tkFont.Font(family="Arial", size=32)
myCFont = tkFont.Font(family="@微軟正黑體", size=32)
for font in tkFont.families():
    print font,
print ""
label1 = Tkinter.Label(top, text="Hello Tk!", padx=30, pady=30, bg='#F00',
                       fg='#0F0', font=myFont)
label2 = Tkinter.Label(top, text="Hello again!", padx=30, pady=30,
                       fg='#F00',
                       bg='#0F0', font=myFont)
label3 = Tkinter.Label(top, text="中文效果", font=myCFont)
label2.pack()
label1.pack()
label3.pack()
top.mainloop()
