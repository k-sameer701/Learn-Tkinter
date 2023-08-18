from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('New Window')

def open_new_Window():
    top = Toplevel()
    top.title('Second Window')
    
    global my_image

    my_image = ImageTk.PhotoImage(Image.open('D:\CodingStuff\Learn Tinter\Image_Utilities\Vr-surgery.jpg'))
    my_label = Label(top, image=my_image).pack()

    button_close = Button(top, text='Close', command=top.destroy).pack()

button_open = Button(root, text='Open', command=open_new_Window).pack()

root.mainloop()