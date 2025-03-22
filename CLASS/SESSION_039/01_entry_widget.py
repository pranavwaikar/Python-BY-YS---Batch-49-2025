from tkinter import *
from tkinter import ttk

def print_entered_text():
    s = svE1.get()
    print(s)
    # L1.configure(text=s)

root_window = Tk()
root_window.title("Entry widget Easy")

root_window.minsize(300,200)
root_window.maxsize(800,600)

L1 = Label(root_window)
L1.configure(text="Enter something")
L1.grid(row=0, column=0)

svE1 = StringVar()
E1 = Entry(root_window)
E1.configure(textvariable=svE1)
E1.grid(row=0,column=1)

B1 = Button(root_window)
B1.configure(text="Print",  command=print_entered_text)
B1.grid(row=1, column=0)

L1 = Label(root_window)
# L1.configure(text="")
L1.configure(textvariable=svE1)
L1.grid(row=1, column=1)

root_window.mainloop()
