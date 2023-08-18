from tkinter import *

root = Tk()
root.title('Frames')

frame = LabelFrame(root, text='This is my Frame....', padx=50, pady=50)
frame.pack(padx=100, pady=100)

b = Button(frame, text='Click Here')
b.pack()

root.mainloop()