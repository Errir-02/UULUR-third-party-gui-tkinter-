from tkinter import *

mainColor, currecntBackgroundColor = "#424242"
trueDark = "#000000"
trueDarkOn = False

gui = Tk()
gui.geometry=("500x500")
gui.config(background=mainColor)

def changeColor():
  if trueDarkOn == True:
    gui.config(background=trueDark)
    trueDarkOn = False
    return
  elif TrueDarkOn == False:
    gui.config(background=mainColor)
    trueDarkOn = True
    return


switchDark = Button(gui,height=2, width=2,bg="#484a48",fg="white",text="color",bd="0p",)
switchDark.place(relx = 0.5, rely=0.5)


gui.mainloop()
