from tkinter import *

win = Tk()
win.title("Event Handling")
win.geometry("400x400")

def handle_click(event):
    print("Left mouse button")

button1 = Button(text="Button 1")
button2 = Button(text="Button 2")
button1.pack()
button2.pack()

button1.bind("<Button-1>", handle_click)

win.mainloop()