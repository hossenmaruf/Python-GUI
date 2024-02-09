from tkinter import *
from tkinter import messagebox

def click():
    messagebox.showinfo()

window = Tk()
button = Button(window, command =click, text="click me")
button.pack()

window.mainloop()