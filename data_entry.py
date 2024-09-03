import tkinter as tk
from tkinter import ttk, messagebox

class DataEntry(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        # Input fields (Animal ID, Weight, etc.)
        self.animal_entry_label = ttk.Label(self, text="Animal ID:")
        self.animal_entry = ttk.Entry(self)
        self.animal_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        self.animal_entry_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")

        # Other fields as previously defined (Weight, Sex, Maturation, etc.)
        # (Repeat the code for creating fields like in your initial script)

        # Save button
        self.save_button = ttk.Button(self, text="Save", command=self.save_record)
        self.save_button.grid(row=7, column=0, columnspan=2, pady=10)
        self.save_button.bind("<Return>", lambda event: self.save_record())

    def save_record(self):
        # Gather data, perform validation, and save the record
        # (Implement the logic similar to your current script)

        # Reset form fields
        self.clear_form()

    def clear_form(self):
        self.animal_entry.delete(0, tk.END)
        # Reset other fields like sex_combobox, maturation_combobox, etc.

    def validate_float(self, value_if_allowed):
        """ Validate that the input is a float number """
        if value_if_allowed in ["", "-", ".", "-."]:
            return True
        try:
            float(value_if_allowed)
            return True
        except ValueError:
            return False
