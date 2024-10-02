# gui/create_pyramid.py
import tkinter as tk
from tkinter import messagebox
from src.pyramid import Pyramid

def create_pyramid():
    try:
        rows = int(entry_rows.get())
        pyramid_type = entry_type.get().lower()
        pyramid = Pyramid(rows, pyramid_type)
        result = f"Total blocks for a {pyramid_type} pyramid with {rows} rows: {pyramid.total_blocks()}"
        messagebox.showinfo("Pyramid Result", result)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Pyramid Creator")

# Create and place the widgets
tk.Label(root, text="Enter the number of rows:").grid(row=0, column=0)
entry_rows = tk.Entry(root)
entry_rows.grid(row=0, column=1)

tk.Label(root, text="Enter the pyramid type (triangular/square):").grid(row=1, column=0)
entry_type = tk.Entry(root)
entry_type.grid(row=1, column=1)

tk.Button(root, text="Create Pyramid", command=create_pyramid).grid(row=2, columnspan=2)

# Run the application
root.mainloop()
