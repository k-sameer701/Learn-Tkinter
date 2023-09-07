from tkinter import *
from PIL import Image, ImageTk

root = Tk()

# 🔥 .geometry('__ x __') -> It defines the area

root.geometry('400x400')

root.title('Sliders')

# 👻 CREATING A VERTICAL SLIDER 

vertical = Scale(root, from_=0, to=200, orient=VERTICAL)
vertical.pack()

# from_     -> starting form
# to        -> ending at
# orient    -> Orientation of the slider

horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL)
horizontal.pack()

root.mainloop()