from tkinter import *
from tkinter import filedialog

def openfile():
    filepath = filedialog.askopenfilename()
    print(filepath)

window = Tk()
button = Button(text="open", command= openfile)
button.pack()
window.mainloop()