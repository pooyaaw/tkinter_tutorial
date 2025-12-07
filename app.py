from tkinter import *

# this creates the window
root = Tk()

# these are label widgets
myLabel1 = Label(root, text="Hellowww bruh!")
myLabel2 = Label(root, text="I'm learing tkinter.")
myButton = Button(root, text="Click Here (because I said so)")

myLabel1.pack()
myLabel2.pack()
myButton.pack()

root.mainloop()
