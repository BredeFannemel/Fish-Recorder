import tkinter as tk
from tkinter import ttk, messagebox
from traits import TraitsManager
from entry import DataEntry
from summary import SummaryManager
import datetime

class FishRecorder(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Fish Recorder")

        # Traits Manager Setup
        traits = ["Animal ID", "Weight", "Sex", "Maturation", "Selection", "Freefield1", "Freefield2", "Freefield3", "Freefield4"]
        self.trait_frame = tk.Frame(self)
        self.trait_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        self.form_frame = tk.Frame(self)
        self.form_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nw")

        self.traits_manager = TraitsManager(self.trait_frame, traits, self.form_frame, self.on_traits_applied)

        # Data Entry Setup
        self.data_entry = DataEntry(self, self.traits_manager)
        self.data_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nw")

        # Summary Manager Setup
        self.summary_manager = SummaryManager(self)
        self.summary_manager.grid(row=0, column=2, rowspan=3, padx=10, pady=10, sticky="ne")

        # Save Button
        self.save_button = ttk.Button(self, text="Save", command=self.save_record)
        self.save_button.grid(row=2, column=0, columnspan=2, pady=10)

    def on_traits_applied(self, selected_traits):
        # Callback when traits are applied
        print(f"Selected Traits: {selected_traits}")

    def save_record(self):
        # Save the current record to a text file
        record = self.traits_manager.get_entry_values()

        # Convert weight to float if it's present
        try:
            record["Weight"] = float(record["Weight"])
        except ValueError:
            messagebox.showwarning("Invalid Weight", "Weight must be a valid number.")
            return

        # Add plate and well to record (from DataEntry)
        record["Plate"] = self.data_entry.plate_var.get()

        # Automatically assign well if none is entered
        if not self.data_entry.well_var.get():
            well = self.data_entry.assign_well()
            if well:
                record["Well"] = well
            else:
                messagebox.showwarning("No Well Available", "No well available to assign.")
                return  # Exit if no wells available
        else:
            record["Well"] = self.data_entry.well_var.get()

        # Add timestamp
        record["Timestamp"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Reset form fields
        self.traits_manager.clear_entries()

        # Add record to summary manager
        self.summary_manager.add_record(record)

if __name__ == "__main__":
    app = FishRecorder()
    app.mainloop()
