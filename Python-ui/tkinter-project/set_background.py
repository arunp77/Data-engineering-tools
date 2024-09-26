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

# Change the background color using configure
root.configure(bg='lightblue')


ttk.Button(root, text="Hello World").grid()

# Run the application
root.mainloop()