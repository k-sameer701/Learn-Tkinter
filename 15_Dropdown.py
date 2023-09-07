from tkinter import *
from PIL import Image, ImageTk

root = Tk()

root.title('DropDown')
root.geometry('400x400')

# 🔥 DROP-DOWN BOXES:

def show():
    mylabel = Label(root, text=clicked.get())
    mylabel.pack()

Options = [
    "Monday", 
    "Tuesday", 
    "Wednesday", 
    "Thursday", 
    "Friday", 
    "Saturday", 
    "Sunday"
]

# ❓DEFAULT CASE FOR DROP-DOWN 👇

clicked = StringVar()
clicked.set(Options[0])

# 🔥 OptionMenu -> It allows to create options in the dropdown.

drop = OptionMenu(root, clicked, *Options)
drop.pack()

my_button = Button(root, text='Show Selected Item', command=show)
my_button.pack()
                  
root.mainloop()