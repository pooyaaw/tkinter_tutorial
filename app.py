from tkinter import *

# this creates the window
root = Tk()

# these are label widgets
myLabel1 = Label(root, text="Hello bruh!").grid(row=0, column=0)
myLabel2 = Label(root, text="I'm learing tkinter.").grid(row=1, column=5)
myLabel3 = Label(root, text="        ").grid(row=1, column=1)

# myLabel1
# myLabel2
# myLabel3
# so the rows and coluns are relative

root.mainloop()
