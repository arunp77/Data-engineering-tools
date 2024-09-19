import tkinter as tk
from tkinter import ttk

class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("DataVista: Complex Data Analytics")
        self.root.geometry("800x600")
        self.create_widgets()

    def create_widgets(self):
        label = ttk.Label(self.root, text="Welcome to DataVista")
        label.pack(pady=20)

        # Placeholder for additional widgets
        load_button = ttk.Button(self.root, text="Load Data", command=self.load_data)
        load_button.pack(pady=10)

    def load_data(self):
        # Placeholder for load data functionality
        print("Load data functionality goes here.")

    def run(self):
        self.root.mainloop()
