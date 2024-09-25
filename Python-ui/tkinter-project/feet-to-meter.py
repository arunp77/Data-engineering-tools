"""_summary_
    Reference: https://tkdocs.com/tutorial/firstexample.html
    
    Objective: We'll create a simple GUI tool to convert a distance in feet to the equivalent distance in meters. 
"""


from tkinter import *                        #  imported everything (*) from the tkinter module
from tkinter import ttk

def calculate(*args):
    """
    Convert the value entered in the 'feet' entry field to meters and 
    display the result in the 'meters' label. If the input is invalid, 
    the function will silently handle the ValueError.
    
    Args:
        *args: Additional arguments passed from event bindings.
        
    Formula:
        meters = feet × 0.3048
    
    Details:
        The conversion uses the formula meters = feet × 0.3048.
        To ensure the result is rounded to 4 decimal places, the following operations are performed:
        
        meters.set(int(0.3048 * value * 10000.0 + 0.5) / 10000.0)
        
        Breakdown of the calculation:
            - 0.3048: The conversion factor from feet to meters.
            - value: The number entered by the user in feet.
            - value * 0.3048: This converts the feet value to meters.
            - * 10000.0 and / 10000.0: This scales the result to 4 decimal places.
            - + 0.5: Adding 0.5 ensures proper rounding when converting to an integer.
            - int(...): This truncates any additional decimal places beyond 4, ensuring the precision to four decimal places.
    
    Raises:
        ValueError: If the input cannot be converted to a float, the error is silently caught and no action is taken.
    """
    try:
        value = float(feet.get())
        # Convert feet to meters and round to 4 decimal places
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        # If the input is not a valid number, do nothing
        pass

# Create the main application window
root = Tk()
root.title("Feet to Meters")

# Create a frame that will hold all the widgets with padding
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

# Configure the main application window to resize properly
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Create a StringVar to store the input value for feet
feet = StringVar()

# Create an entry widget for inputting the feet value
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

# Create a StringVar to store the output value for meters
meters = StringVar()

# Create a label to display the result in meters
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

# Create a button to trigger the calculation when clicked
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

# Create labels for the text descriptions
ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

# Add padding to all child widgets within the mainframe
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

# Set the initial focus to the feet entry widget
feet_entry.focus()

# Bind the Enter/Return key to trigger the calculation
root.bind("<Return>", calculate)


# Start the Tkinter event loop to run the application
root.mainloop()
