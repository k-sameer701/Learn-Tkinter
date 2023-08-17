from tkinter import *

root = Tk()     # It makes a Basic GUI

# 🤖 Creating a label widget
myLabel1 = Label(root, text='Hello World!')
myLabel2 = Label(root, text='My name is Khan')

# 🔥 Showing it on the screen

# ❓ The grid manager allows you to specify rows and columns to which you can place widgets, making it easier to align and position widgets in a more precise manner compared to the pack geometry manager.

# ❓ You can also use the rowspan and columnspan options to make a widget span multiple rows or columns.

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)

root.mainloop()     