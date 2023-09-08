from tkinter import *

root = Tk()

root.title('Label Options')

# 🔥 Important Label Options:

# text      -   Adds the text
# bd        -   Background
# fg        -   Foreground
# font      -   Sets the Font
# padx      -   x Padding
# pady      -   y Padding
# relief    -   Border Styling (SUNKEN, RAISED, GROOVE, RIDGE)

# 🔥 Important Pack Options:

# anchor    -   nw (north-west)
# side      -   TOP, BOTTOM, RIGHT, LEFT

# fill      -   X   OR  Y

my_label = Label(root, text = 'Hello there, How you doing? ')
my_label.pack(side=LEFT, fill=X)
root.mainloop()