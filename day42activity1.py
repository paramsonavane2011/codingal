from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

win = Tk()
win.title("600x500")
win.rowconfigure(0, minsize=800, weight=1)
win.columnconfigure(1, minsize=800, weight=1)

def openFile():
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    txtEdit.delete(1.0, END)

    with open(filepath, "r") as inputFile:
        text = inputFile.read()
        txtEdit.insert(END, text)
        inputFile.close()

    win.title(f"Text Editor -> {filepath}")

def saveFile():
    filepath = asksaveasfilename(defaultextension="*.txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    with open(filepath, "w") as outputFile:
        text = txtEdit.get(1.0, END)
        outputFile.write(text)

    win.title(f"Text Editor -> {filepath}")

txtEdit = Text(win)
buttonFrame = Frame(win, relief=RAISED, bd=2)
openBtn = Button(buttonFrame, text="Open", command=openFile)
saveBtn = Button(buttonFrame, text="Save As..", command=saveFile)

openBtn.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
saveBtn.grid(row=1, column=0, sticky="ew", padx=5)

buttonFrame.grid(row=0, column=0, sticky="ns")
txtEdit.grid(row=0, column=1, sticky="nsew")

win.mainloop()


