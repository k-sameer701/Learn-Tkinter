from tkinter import *

root = Tk()     # It makes a Basic GUI
# ❓ Tk() is a class constructor used to create the main application.
# ❓ The main application window is also commonly referred to as the "root" window. This root window acts as the top-level container for all the other GUI widgets, such as buttons, labels, text fields, etc.


# 🤖 Creating a label widget

# ❓"Label" is a widget that is used to display a text or an image. It provides a way to show static text or images

myLabel = Label(root, text='Hello World!')

# 🔥 Showing it on the screen with the help of pack
myLabel.pack()

root.mainloop()     

# ❓ The event loop (mainloop()) is essential for keeping your GUI responsive to user interactions and for handling various events that occur within your application.