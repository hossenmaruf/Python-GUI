from tkinter import *

food = ["pizza","hamburger","hotdog"]

window = Tk()


for index in range (len(food)):
    radiobutton = Radiobutton(window,text= food[index])
    radiobutton.pack()
window.mainloop()