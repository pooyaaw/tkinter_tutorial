from tkinter import *

# this creates the window
root = Tk()

# Entry Widget for entering data
# fg and bg work on Entry too for changing foreground and background color
e = Entry(root, width="50", borderwidth="5")
myl = Label(root, text="first enter your name: ")
myl.pack()
e.pack()
e.get()  # gets whatever you entered into the widget


def myClick():
    myLabel = Label(root, text="hello " + e.get())
    myLabel.pack()


myButton = Button(root,  command=myClick, text="then click Here",
                  padx=30, pady=30, fg="brown", bg="lightgreen")
# you cant write  command=myClick() because the () will have the myClick executed anyway.
# and when you click it again it wont be executed every time you click it.
myButton.pack()

root.mainloop()
