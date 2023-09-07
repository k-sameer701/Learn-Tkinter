from tkinter import *
from PIL import Image, ImageTk

root = Tk()

root.title('CheckBoxes')
root.geometry('400x400')

def show():
    myLabel = Label(root, text=var.get()).pack()

var = IntVar()

c = Checkbutton(root, text = "Check this Box", variable=var)
c.pack()



myButton = Button(root, text="Show selection", command=show)
myButton.pack()

root.mainloop()