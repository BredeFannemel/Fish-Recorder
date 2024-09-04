import tkinter as tk
from tkinter import ttk, messagebox
import csv
import datetime

class DataEntry(tk.Frame):
    def __init__(self, parent, traits_manager):
        super().__init__(parent)
        self.parent = parent
        self.traits_manager = traits_manager
        self.create_widgets()
        self.current_plate = 1
        self.current_well_index = 1
        self.well_plate_labels = []
        self.update_well_plate_display()

    def create_widgets(self):
        # Dynamic form based on selected traits
        self.form_frame = tk.Frame(self)
        self.form_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        self.traits_manager.form_frame = self.form_frame  # Link form frame to traits manager
        self.traits_manager.apply_trait_selection()  # Initialize form with selected traits

        # Plate and Well info
        self.plate_label = ttk.Label(self, text="Plate:")
        self.plate_entry = ttk.Entry(self)
        self.plate_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.plate_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        self.plate_entry.bind("<Return>", self.reset_plate)  # Bind Enter key to reset plate

        self.well_label = ttk.Label(self, text="Well:")
        self.well_display = ttk.Entry(self, state="readonly")
        self.well_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.well_display.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Well plate visual display
        self.well_plate_frame = tk.Frame(self)
        self.well_plate_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        # Save button
        self.save_button = ttk.Button(self, text="Save", command=self.save_record)
        self.save_button.grid(row=4, column=0, columnspan=2, pady=10)

    def save_record(self):
        """Save the current record to a text file."""
        record = self.traits_manager.get_entry_values()

        # Add plate and well to record
        record["Plate"] = self.plate_entry.get()
        record["Well"] = self.well_display.get()

        # Add timestamp
        record["Timestamp"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Save record to file
        self.save_to_file(record)

        # Move to next well
        self.move_to_next_well()

    def save_to_file(self, record):
        """ Save the current record to a text file in tabulated format """
        with open('fish_records.txt', 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=list(record.keys()), delimiter='\t')
            if file.tell() == 0:  # Write header if the file is new/empty
                writer.writeheader()
            writer.writerow(record)

        # Reset form fields
        self.traits_manager.clear_entries()

    def validate_float(self, value_if_allowed):
        """ Validate that the input is a float number """
        if value_if_allowed in ["", "-", ".", "-."]:
            return True
        try:
            float(value_if_allowed)
            return True
        except ValueError:
            return False

    def reset_plate(self, event=None):
        """ Reset the plate and start wells from A02 again. """
        self.current_well_index = 1
        self.update_well_display()
        self.update_well_plate_display()

    def move_to_next_well(self):
        """ Move to the next well in the plate. """
        self.current_well_index += 1
        if self.current_well_index > 96:
            messagebox.showinfo("Plate Full", "Current plate is full. Please enter a new plate.")
            return
        self.update_well_display()
        self.update_well_plate_display()

    def update_well_display(self):
        """ Update the well display entry based on current well index. """
        row = (self.current_well_index - 1) // 12
        col = (self.current_well_index - 1) % 12
        well_name = f"{chr(65 + row)}{col + 1:02d}"
        self.well_display.config(state="normal")
        self.well_display.delete(0, tk.END)
        self.well_display.insert(0, well_name)
        self.well_display.config(state="readonly")

    def update_well_plate_display(self):
        """ Update the visual display of the well plate with current filled wells. """
        for label in self.well_plate_labels:
            label.destroy()
        self.well_plate_labels.clear()

        for i in range(8):  # 8 rows (A to H)
            for j in range(12):  # 12 columns (1 to 12)
                well_index = i * 12 + j + 1
                well_name = f"{chr(65 + i)}{j + 1:02d}"
                color = "green" if well_index < self.current_well_index else "white"
                label = tk.Label(self.well_plate_frame, text=well_name, bg=color, width=3, height=1, relief="solid")
                label.grid(row=i, column=j, padx=1, pady=1)
                self.well_plate_labels.append(label)
