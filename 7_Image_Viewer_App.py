from tkinter import *
from PIL import ImageTk, Image
root = Tk()

root.title('Image Viewer')
root.iconbitmap('D:\CodingStuff\Learn Tinter\Image_Utilities\Twitter-logo.ico')

my_image_1 = ImageTk.PhotoImage(Image.open('D:\CodingStuff\Learn Tinter\Image_Utilities\Image (1).jpg'))
my_image_2 = ImageTk.PhotoImage(Image.open('D:\CodingStuff\Learn Tinter\Image_Utilities\Image (2).jpg'))
my_image_3 = ImageTk.PhotoImage(Image.open('D:\CodingStuff\Learn Tinter\Image_Utilities\Image (3).jpg'))
my_image_4 = ImageTk.PhotoImage(Image.open('D:\CodingStuff\Learn Tinter\Image_Utilities\Image (4).jpg'))
my_image_5 = ImageTk.PhotoImage(Image.open('D:\CodingStuff\Learn Tinter\Image_Utilities\Image (5).jpg'))

image_list = [my_image_1, my_image_2, my_image_3, my_image_4, my_image_5]

status = Label(root, text='Image 1 of ' + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

my_label = Label(image=my_image_1)
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_number):
    global my_label
    global button_forward
    global button_backward

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])

    button_backward = Button(root, text='<<', command= lambda : backward(image_number-1))
    button_forward = Button(root, text='>>', command= lambda: forward(image_number+1))

    if image_number == 5:
        button_forward = Button(root, text='>>', state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_backward.grid(row=1, column=0)   
    button_forward.grid(row=1, column=2)
    
    # UPDATE STATUS BAR
    
    status = Label(root, text='Image '+str(image_number)+' of ' + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)
    

def backward(image_number):
    global my_label
    global button_forward
    global button_backward

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])

    button_backward = Button(root, text='<<', command = lambda : backward(image_number-1))
    button_forward = Button(root, text='>>', command = lambda : forward(image_number+1))
    if image_number == 1:
        button_backward = Button(root, text='<<', state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_backward.grid(row=1, column=0)   
    button_forward.grid(row=1, column=2)

    # UPDATE STATUS BAR

    status = Label(root, text='Image '+str(image_number)+' of ' + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

button_backward = Button(root, text='<<', command= lambda : backward(), state=DISABLED)
button_exit = Button(root, text='Exit', command = root.quit)
button_forward = Button(root, text='>>', command= lambda: forward(2))

button_backward.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)

root.mainloop()
