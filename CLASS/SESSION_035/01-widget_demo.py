# Import required GUI package
import tkinter
import tkinter.ttk
import sys

# Handler functions
def terminate(param):
    print(f"Exiting app... {param}")
    sys.exit(0)

# Create a main window by making an object of Tk class
root_window = tkinter.Tk()

# Add title of Window
root_window.title('CPA - Python 49 batch Window - Widget Demo')

master_frame = tkinter.ttk.Frame(root_window, padding="3 3 12 12")
master_frame.grid(row=0, column=0, sticky=(tkinter.N, tkinter.W, tkinter.E, tkinter.S))

B = tkinter.Button(master_frame)
B.configure(text="Exit Button", command=lambda:terminate("Mau Mau test"))
B.grid(row=1, column=1, sticky=tkinter.E)


# Set minimumn Width & height
root_window.minsize(400,300)

# Set max Width & height
root_window.maxsize(1600,1200)

# Enter event loop
root_window.mainloop()

