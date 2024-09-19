import tkinter as tk
from tkinter import ttk, Text, filedialog, messagebox
import pandas as pd

class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("DataVista: Complex Data Analytics")
        self.root.geometry("1200x800")  # Resizing window to accommodate the layout

        # Configuring grid layout
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=2)
        self.root.grid_rowconfigure(1, weight=2)
        self.root.grid_rowconfigure(2, weight=2)

        self.create_widgets()

    def create_widgets(self):
        # Logo and header
        header_frame = ttk.Frame(self.root)
        header_frame.grid(row=0, column=0, sticky="nsew", columnspan=2)
        
        logo_label = ttk.Label(header_frame, text="DataVista", font=("Arial", 24, "bold"))
        logo_label.grid(row=0, column=0, padx=10, pady=10)
        
        # Contact information
        contact_info = ttk.Label(header_frame, text="Affiliation: Vision - Analytica\nEmail: arunp77@gmail.com\nGitHub: https://github.com/arunp77", font=("Arial", 10))
        contact_info.grid(row=0, column=1, padx=10, pady=10)

        # "Load Data" label
        load_data_label = ttk.Label(self.root, text="Load the data", font=("Arial", 16))
        load_data_label.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        # Load Data button without the frame
        load_button = ttk.Button(self.root, text="Click here", command=self.load_data)
        load_button.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        # Top 5 rows section (without a frame, just as a text widget)
        self.data_display = Text(self.root, height=6, width=40)
        self.data_display.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)
        self.data_display.insert(tk.END, "Please load the data to see the first 5 rows...\n")
        self.data_display.config(state=tk.DISABLED)

        # Plot areas (these remain the same as placeholders)
        self.first_plot_frame = ttk.Frame(self.root, width=400, height=300)
        self.first_plot_frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)
        ttk.Label(self.first_plot_frame, text="Place for the first plot").pack(expand=True)

        self.second_plot_frame = ttk.Frame(self.root, width=400, height=300)
        self.second_plot_frame.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)
        ttk.Label(self.second_plot_frame, text="Place for the Second plot").pack(expand=True)

        self.third_plot_frame = ttk.Frame(self.root, width=400, height=150)
        self.third_plot_frame.grid(row=3, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
        ttk.Label(self.third_plot_frame, text="Place for the Third plot").pack(expand=True)

    def load_data(self):
        # Open file dialog to load the Excel file
        file_path = filedialog.askopenfilename(
            filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")]
        )

        if file_path:
            try:
                # Load data from Excel file
                data = pd.read_excel(file_path)

                # Display first 5 rows of the loaded data
                self.display_first_5_rows(data)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load the file:\n{str(e)}")
        else:
            messagebox.showwarning("No file", "No file selected!")

    def display_first_5_rows(self, data):
        # Clear the existing text in the data display section
        self.data_display.config(state=tk.NORMAL)
        self.data_display.delete(1.0, tk.END)

        # Format the data to be displayed (first 5 rows)
        first_5_rows = data.head(5).to_string(index=False)

        # Insert data into the text widget
        self.data_display.insert(tk.END, first_5_rows)
        self.data_display.config(state=tk.DISABLED)

    def run(self):
        self.root.mainloop()

