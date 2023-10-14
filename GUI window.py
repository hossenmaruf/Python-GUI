from tkinter import *

window = Tk() #instantiate an instance of a window
window.geometry("420x420")
window.title("Python GUI program")

icon = PhotoImage(file='logo.png')
window.iconphoto(True,icon)
window.config(background="#5cfcff")


photo = PhotoImage(file='download.png')

label = Label(window,
              text="PYTHON?",
              font=('Arial',40,'bold'),
              fg='#00FF00',
              bg='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound='bottom')
label.pack()
#label.place(x=0,y=0)

window.mainloop() #place window on computer screen, listen for events