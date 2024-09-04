import tkinter as tk
from tkinter import ttk
from traits import TraitsManager
from entry import DataEntry
from summary import SummaryManager
import datetime  # Add this import to fix the NameError

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
        "Callback when traits are applied."
        print(f"Selected Traits: {selected_traits}")

    def save_record(self):
        "Save the current record to a text file."
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
        if not self.plate_selected:
            messagebox.showwarning("Plate Not Confirmed", "Please confirm the plate before saving.")
            return

        def save_to_file(self, record):
        "Save the current record to a text file in tabulated format"
        with open('fish_records.txt', 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=list(record.keys()), delimiter='\t')
            if file.tell() == 0:  # Write header if the file is new/empty
                writer.writeheader()
            writer.writerow(record)

        # Reset form fields
        self.traits_manager.clear_entries()

if __name__ == "__main__":
    app = FishRecorder()
    app.mainloop()
