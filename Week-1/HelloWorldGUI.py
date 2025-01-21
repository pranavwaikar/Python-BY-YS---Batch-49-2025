"""
This program creates a simple GUI application using the Tkinter library. 
It has the following features:
1. A "Welcome" button that displays a greeting message in the application window.
2. An "Exit" button that displays an exit message and then closes the application after a short delay.
3. A Label widget to display messages dynamically based on user interactions.
The GUI window is designed to be simple and user-friendly.
"""

import sys
from tkinter import *

def greetings():
    output_label.config(text="Hey, How are you?")

def terminate():
    output_label.config(text="Exiting the app...")
    rootWindow.after(2000, sys.exit)  # Exit after displaying the message for 2 seconds

# Create the main window
rootWindow = Tk()
rootWindow.title("Window of Pranav")
rootWindow.geometry("300x200")  # Set the size of the window

# Create a Label to display output messages
output_label = Label(rootWindow, text="", font=("Arial", 12))
output_label.grid(row=0, column=0, columnspan=2, pady=10)

# Create the Welcome button
B1 = Button(rootWindow, text="Welcome", command=greetings)
B1.grid(row=1, column=0, padx=10, pady=10)

# Create the Exit button
B2 = Button(rootWindow, text="Exit", command=terminate)
B2.grid(row=1, column=1, padx=10, pady=10)

# Run the application
rootWindow.mainloop()