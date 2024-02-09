from tkinter import *
from tkinter import messagebox

def click():
   # messagebox.showinfo(title='this is a info title box', message='you are a person')

window = Tk()


button = Button(window, command = click, text="click me")
button.pack()
window.mainloop()
