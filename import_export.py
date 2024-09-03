import tkinter as tk
from tkinter import filedialog

class ImportManager:
    def __init__(self, master):
        self.master = master

        self.import_button = tk.Button(self.master, text="Import Animal Information", command=self.import_file)
        self.import_button.grid(row=0, column=0, pady=5)

    def import_file(self):
        """ Handle the import of animal data from a file """
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file:
                data = file.read()
                # Process the imported data
                print("Data imported:", data)
