import tkinter
import tkinter.ttk
import sys

def ok_button_handler():
    print("Ok button is cklicked")


def cancel_button_handler():
    print("Cancel button is cklicked")


def exit_button_handler():
    print("Exit button is cklicked")
    sys.exit(0)

# main window creation

root_window = tkinter.Tk()
root_window.title("An exercise in button handlers")

#widget construction

#Ok button
ok_button = tkinter.Button(root_window)
ok_button.configure(text='Ok', command = ok_button_handler)
ok_button.grid(row= 1, column =1, sticky=(tkinter.E, tkinter.W))

#Cancel button
cancel_button = tkinter.Button(root_window)
cancel_button.configure(text='Cancel', command = cancel_button_handler)
cancel_button.grid(row= 2, column =1, sticky=(tkinter.E, tkinter.W))

#Exit button
exit_button = tkinter.Button(root_window)
exit_button.configure(text='Exit', command = exit_button_handler)
exit_button.grid(row= 3, column =1, sticky=(tkinter.E, tkinter.W))

#entering mainloop
root_window.mainloop()
