# Import required GUI package
import tkinter

# Create a main window by making an object of Tk class
root_window = tkinter.Tk()

# Add title of Window
root_window.title('CPA - Python 49 batch Window')

# Set minimumn Width & height
root_window.minsize(200,150)

# Set max Width & height
root_window.maxsize(800,600)

# Create a label object
my_name = tkinter.Label(root_window, text='021_Pranav_waikar', fg='green', font=('Times New Roman', 12, 'bold'))

# Place a label on give co-ordinates
my_name.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

# Enter event loop
root_window.mainloop()

