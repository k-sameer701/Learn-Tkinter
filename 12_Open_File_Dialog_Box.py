from tkinter import *
from PIL import ImageTk, Image

# 🔥 IMPORT FILEDIALOG
from tkinter import filedialog

root = Tk()
root.title('File Dialog Box')

def open():

    global my_image

    # 👻 HOW TO OPEN A FILE DIALOG BOX

    root.filename = filedialog.askopenfilename(initialdir="/Image_Utilities", title="Select A File", filetypes=(("png files", "*.png"), ("all files", "'.'")))

    # root.filename -> It contains only the path of the file

    my_label = Label(root, text=root.filename).pack()

    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()

my_button = Button(root, text="Open File", command=open).pack()

root.mainloop()