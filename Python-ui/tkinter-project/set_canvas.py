""" 
Reference: https://www.geeksforgeeks.org/how-to-change-a-tkinter-window-background-color/
"""

import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Tkinter Window Background Color")

# Set the window size
root.geometry("400x300")

# Create a canvas and set its background color
canvas = tk.Canvas(root, bg='lightcoral')
canvas.pack(fill=tk.BOTH, expand=True)

# Run the application
root.mainloop()
