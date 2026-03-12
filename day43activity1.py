from tkinter import *

win = Tk()
win.geometry("400x300")
win.title("main")

def topwin():
    top = Toplevel()
    top.geometry("180x100")
    top.title("toplevel")

    l2 = Label(top, text="This is toplevel window")
    l2.pack()

    top.mainloop()

l = Label(win, text="This is main window")
btn = Button(win, text="Click to open toplevel window", command=topwin)

l.pack()
btn.pack()

win.mainloop()