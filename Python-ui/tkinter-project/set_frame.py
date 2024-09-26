""" 
Reference: https://www.geeksforgeeks.org/how-to-change-a-tkinter-window-background-color/
"""

import tkinter as tk
from tkinter import ttk 

# Create the main window
root = tk.Tk()
root.title("Tkinter Window Background Color")

# Set the window size
root.geometry("400x300")

# Create a frame and place it in the window
frame = tk.Frame(root, bg='lightgreen')
frame.place(relwidth=1, relheight=1)

ttk.Button(root, text="Hello World").grid()

# Run the application
root.mainloop()