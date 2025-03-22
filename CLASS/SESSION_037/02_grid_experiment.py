import tkinter

root_window = tkinter.Tk()
root_window.title("Grid Experiment")

B1 = tkinter.Button(root_window, text = 'OK') #root window is parent
B2 = tkinter.Button(root_window, text = 'Cancel')
B3 = tkinter.Button(root_window, text = 'Retry')

B1.grid(row = 1, column = 1, sticky=(tkinter.E, tkinter.W))
B2.grid(row = 2, column = 1, sticky=(tkinter.E, tkinter.W))
B3.grid(row = 3, column = 1, sticky=(tkinter.E, tkinter.W))

##For horizontal alignment
#B1.grid(row = 1, column = 1)
#B2.grid(row = 1, column = 2)
#B3.grid(row = 1, column = 3)

root_window.mainloop()



#               N
#               |
#               |
#               |
#   E   ----------------- W
#               |
#               |
#               |
#               S
#
#
#   East, West, North, South directions for sticky
#
