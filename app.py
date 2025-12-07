from tkinter import *

# this creates the window
root = Tk()

# these are label widgets
myLabel1 = Label(root, text="Hello bruh!")
myLabel2 = Label(root, text="I'm learing tkinter.")

myLabel3 = Label(root, text="        ")

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)
myLabel3.grid(row=1, column=1)
# so the rows and coluns are relative

root.mainloop()
