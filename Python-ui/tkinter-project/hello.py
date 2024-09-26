"""
This script creates a basic Tkinter window with a single button labeled 'Hello World'.

Modules:
    tkinter: Provides the core GUI framework.
    tkinter.ttk: Provides themed widgets for Tkinter.`

Functionality:
    - A root window is created using Tk().
    - A button is created using the ttk.Button() widget and displayed with the text 'Hello World'.
    - The button is placed in the root window using the grid geometry manager.
    - The Tkinter event loop is started using root.mainloop() to display the window and keep it open.

Usage:
    Simply run the script to display the GUI window with the button.
    python hello.py
    
Refrence:
    https://tkdocs.com/tutorial/install.html
"""

from tkinter import *
from tkinter import ttk

root = Tk()
ttk.Button(root, text="Hello World").grid()



root.mainloop()