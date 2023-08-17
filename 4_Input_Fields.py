from tkinter import *

root = Tk()

enter = Entry(root, width = 50, bg='yellow', borderwidth = 5)
# Entry 👉 It is used to generate a input box.
# fg 👉 It is used to provide colours to the texts inside the button.
# bg 👉 It is used to change the background colour of the button.
# borderwidth 👉 It is used to change the width of the border.

enter.pack()

def myClick():
    hello  = "Hello, " + enter.get()
    # enter.get() 👉 It is used to get the text from the input box (enter) .
    myLabel = Label(root, text = hello)
    
    myLabel.pack()

myButton = Button(root, text='Enter your Name', command = myClick)

myButton.pack()

root.mainloop()