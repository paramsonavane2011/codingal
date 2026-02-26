from tkinter import *
from datetime import date

root = Tk()
root.title("Getting started with widgets")
root.geometry("400x300")

label = Label(text="Hey there!", fg="white", bg="#072F5F", height=1, width=300)

nameLabel = Label(text="Full name", bg="#3895D3")
nameEntry = Entry()

def display():
    name = nameEntry.get()
    global message
    message = "Welcome to the app!\nToday's date is: "
    greeting = f"Hello {name}\n"
    textBox.insert(END, greeting)
    textBox.insert(END, message)
    textBox.insert(END, date.today())

textBox = Text(height=3)

btn = Button(text="Begin", command=display(), height=1, bg="#1261A0", fg="white")

label.pack()
nameLabel.pack()
nameEntry.pack()
btn.pack()
textBox.pack()

root.mainloop()