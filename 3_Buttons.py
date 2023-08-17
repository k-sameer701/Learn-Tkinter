from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text = 'Look! I clicked a Button')
    myLabel.pack()

myButton = Button(root, text = 'Click Me', padx = 50, command = myClick, fg='blue', bg='grey')

# ❓ In Tkinter, a "Button" is a widget that users can interact with by clicking on it. It's used to trigger actions or functions when clicked. Buttons can display text or images 

# state = DISABLED 👉 Button will be clicked.
# padx 👉 Padding in x-direction.
# pady 👉 Padding in y-direction.
# command 👉 Use to call your function.
# fg 👉 It is used to provide colours to the texts inside the button.
# bg 👉 It is used to change the background colour of the button.


# 🔥 Showing it on the screen
myButton.pack()

root.mainloop()