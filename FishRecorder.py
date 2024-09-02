import tkinter as tk
from tkinter import ttk, messagebox

class BMK_rec(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("BMK rec v.1.0")
        self.selected_fields = ["Animal ID", "Weight", "Sex", "Selection", "Freefield 1", "Freefield 2"]
        self.create_widgets()

    def create_widgets(self):
        # Animal ID entry
        self.animal_entry_label = ttk.Label(self, text="Animal ID:")
        self.animal_entry = ttk.Entry(self)
        self.animal_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        self.animal_entry_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")

        # Weight entry with float validation
        self.weight_label = ttk.Label(self, text="Weight:")
        self.weight_entry = ttk.Entry(self, validate="key", validatecommand=(self.register(self.validate_float), '%P'))
        self.weight_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.weight_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # Sex combobox
        self.sex_label = ttk.Label(self, text="Sex:")
        self.sex_combobox = ttk.Combobox(self, values=["Female", "Male", "Unknown"], state="readonly")
        self.sex_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.sex_combobox.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Selection combobox
        self.selection_label = ttk.Label(self, text="Selection:")
        self.selection_combobox = ttk.Combobox(self, values=["Selected", "Culled"], state="readonly")
        self.selection_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.selection_combobox.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        # Freefield1 entry
        self.freefield1_entry_label = ttk.Label(self, text="Freefield 1:")
        self.freefield1_entry = ttk.Entry(self)
        self.freefield1_entry.grid(row=4, column=1, padx=10, pady=5, sticky="w")
        self.freefield1_entry_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")

        # Freefield2 entry
        self.freefield2_entry_label = ttk.Label(self, text="Freefield 2:")
        self.freefield2_entry = ttk.Entry(self)
        self.freefield2_entry.grid(row=5, column=1, padx=10, pady=5, sticky="w")
        self.freefield2_entry_label.grid(row=5, column=0, padx=10, pady=5, sticky="e")

        # Save button
        self.save_button = ttk.Button(self, text="Save", command=self.save_record)
        self.save_button.grid(row=6, column=0, columnspan=2, pady=10)
        self.save_button.bind("<Return>", lambda event: self.save_record())

    def validate_float(self, value_if_allowed):
        """ Validate that the input is a float number """
        if value_if_allowed in ["", "-", ".", "-."]:
            return True
        try:
            float(value_if_allowed)
            return True
        except ValueError:
            return False

    def save_record(self):
        # Gather data from fields
        record = {
            "Animal ID": self.animal_entry.get().strip(),
            "Weight": self.weight_entry.get().strip(),
            "Sex": self.sex_combobox.get(),
            "Selection": self.selection_combobox.get(),
            "Freefield 1": self.freefield1_entry.get().strip(),
            "Freefield 2": self.freefield2_entry.get().strip(),
        }

        # Check if all required fields are filled
        if all(record.values()):
            # Assuming a recorded_data list to store records
            self.recorded_data.append(record)
            self.clear_form()

            messagebox.showinfo("Success", "Record saved successfully!")
        else:
            messagebox.showwarning("Warning", "Please fill out all fields.")

    def clear_form(self):
        """ Clear all fields after saving a record """
        self.animal_entry.delete(0, tk.END)
        self.weight_entry.delete(0, tk.END)
        self.sex_combobox.set('')
        self.selection_combobox.set('')
        self.freefield1_entry.delete(0, tk.END)
        self.freefield2_entry.delete(0, tk.END)

if __name__ == "__main__":
    app = BMK_rec()
    app.mainloop()
