from tkinter import *

win = Tk()
win.title("Getting Started with Widgets")
win.geometry("400x300")

heading = Label(text="Product")

num1 = Label(text="Number 1:")
entry1 = Entry()
num2 = Label(text="Number 2:")
entry2 = Entry()


def calculate():
    product = int(entry1.get()) * int(entry2.get())
    answer = Label(text=f"The product is \"{product}\"")
    answer.pack()

res = Button(text="Calculate", command=calculate, height=2, width=10, bg="blue", fg="white")
heading.pack()
num1.pack()
entry1.pack()
num2.pack()
entry2.pack()
res.pack()
win.mainloop()