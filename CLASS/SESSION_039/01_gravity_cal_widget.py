from tkinter import *
from tkinter import ttk

# Gravitational Constant (N·m²/kg²)
G = 6.674 * (10**-11)

def calculate_gravity():
    try:
        m1 = float(mass1_var.get())
        m2 = float(mass2_var.get())
        r = float(distance_var.get())

        if r == 0:
            result_var.set("Distance cannot be zero!")
        else:
            force = G * (m1 * m2) / (r ** 2)
            result_var.set(f"Gravitational force of attraction: {force:.6e} N")
    except ValueError:
        result_var.set("Invalid input! Enter numeric values.")

def clear_fields():
    mass1_var.set("")
    mass2_var.set("")
    distance_var.set("")
    result_var.set("")

def exit_app():
    root.destroy()

# Initialize Tkinter Window
root = Tk()
root.title("Gravity Calculator")
root.geometry("400x300")

# Labels and Entry Fields
Label(root, text="Mass of Object 1 (kg):").grid(row=0, column=0, padx=10, pady=5, sticky=W)
mass1_var = StringVar()
Entry(root, textvariable=mass1_var).grid(row=0, column=1, padx=10, pady=5)

Label(root, text="Mass of Object 2 (kg):").grid(row=1, column=0, padx=10, pady=5, sticky=W)
mass2_var = StringVar()
Entry(root, textvariable=mass2_var).grid(row=1, column=1, padx=10, pady=5)

Label(root, text="Distance Between Objects (m):").grid(row=2, column=0, padx=10, pady=5, sticky=W)
distance_var = StringVar()
Entry(root, textvariable=distance_var).grid(row=2, column=1, padx=10, pady=5)

# Result Label
result_var = StringVar()
Label(root, textvariable=result_var, fg="red", font=("Arial", 30, "bold")).grid(row=3, columnspan=2, pady=10)

# Buttons
Button(root, text="Submit", command=calculate_gravity).grid(row=4, column=0, padx=10, pady=10)
Button(root, text="Clear", command=clear_fields).grid(row=4, column=1, padx=10, pady=10)
Button(root, text="Exit", command=exit_app).grid(row=5, columnspan=2, pady=10)

# Run the App
root.mainloop()

