from tkinter import *
from tkinter import messagebox

win = Tk()
win.title("Event Handling")
win.geometry("200x200")

def msg():
    messagebox.showwarning("Alert!", "Stop! Virus found!")

button = Button(win, text="Click me!", command=msg)
button.place(x=50, y=50)

win.mainloop()