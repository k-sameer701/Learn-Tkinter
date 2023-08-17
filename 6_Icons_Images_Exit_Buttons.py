from tkinter import *

# Write the below command to use images in your program
from PIL import ImageTk, Image

root = Tk()

root.title("Icons")
# root.title() 👉 It will change the title that you provide.

root.iconbitmap('D:\CodingStuff\Learn Tinter\Image_Utilities\Twitter-logo.ico')
# root.iconbitmap() 👉 It will change the icon of the output screen that will appear.

# 🔥 Adding Images in your Program.

# Step 1️⃣ : Define the image
my_image = ImageTk.PhotoImage(Image.open('D:\CodingStuff\Learn Tinter\Image_Utilities\Vr-surgery.jpg'))

# Step 2️⃣ : Use that image in a label
my_label = Label(image=my_image)

# Step 3️⃣ : Display the image using pack or grid.
my_label.pack()


# 🔥 Creating an exit button.

button_exit = Button(root, text = 'Exit Program', command=root.quit)
button_exit.pack()


root.mainloop()