from tkinter import *

# this creates the window
root = Tk()


def myClick():
    myLabel = Label(root, text="Look! I clicked a button!")
    myLabel.pack()


myButton = Button(root,  command=myClick, text="Click Here",
                  padx=30, pady=30, fg="green", bg="black")
# you cant write  command=myClick() because the () will have the myClick executed anyway.
# and when you click it again it wont be executed every time you click it.


myButton.pack()

root.mainloop()
