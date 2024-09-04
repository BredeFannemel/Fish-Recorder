import tkinter as tk
from tkinter import ttk, messagebox

class DataEntry(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        # Input field (Animal ID)
        self.animal_entry_label = ttk.Label(self, text="Animal ID:")
        self.animal_entry = ttk.Entry(self)
        self.animal_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        self.animal_entry_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")

        # Weight float
        self.weight_label = ttk.Label(self, text="Weight:")
        self.weight_entry = ttk.Entry(self, validate="key", validatecommand=(self.register(self.validate_float), '%P'))
        self.weight_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.weight_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # Sex combobox
        self.sex_label = ttk.Label(self, text="Sex:")
        self.sex_combobox = ttk.Combobox(self, values=["Female", "Male", "Unknown"], state="readonly")
        self.sex_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.sex_combobox.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Maturation combobox
        self.maturation_label = ttk.Label(self, text="Maturation:")
        self.maturation_combobox = ttk.Combobox(self, values=["Mature", "Immature", "Unknown"], state="readonly")
        self.maturation_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.maturation_combobox.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        # Selection combobox
        self.selection_label = ttk.Label(self, text="Selection:")
        self.selection_combobox = ttk.Combobox(self, values=["Selected", "Culled"], state="readonly")
        self.selection_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.selection_combobox.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        # Freefield1 entry
        self.freefield1_entry_label = ttk.Label(self, text="Freefield 1:")
        self.freefield1_entry = ttk.Entry(self)
        self.freefield1_entry.grid(row=5, column=1, padx=10, pady=5, sticky="w")
        self.freefield1_entry_label.grid(row=5, column=0, padx=10, pady=5, sticky="e")

        #Freefield2 entry
        self.freefield2_entry_label = ttk.Label(self, text="Freefield 2:")
        self.freefield2_entry = ttk.Entry(self)
        self.freefield2_entry.grid(row=6, column=1, padx=10, pady=5, sticky="w")
        self.freefield2_entry_label.grid(row=6, column=0, padx=10, pady=5, sticky="e")

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
