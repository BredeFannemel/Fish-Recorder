import tkinter as tk
from tkinter import ttk
from traits import TraitsManager
from entry import DataEntry
from summary import SummaryManager

class FishRecorder(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Fish Recorder")

        #1 Traits Manager Setup
        traits = ["Animal ID", "Weight", "Sex", "Maturation", "Selection", "Freefield1", "Freefield2", "Plate", "Well"]
        self.trait_frame = tk.Frame(self)
        self.trait_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        self.form_frame = tk.Frame(self)
        self.form_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nw")

        self.traits_manager = TraitsManager(self.trait_frame, traits, self.form_frame, self.on_traits_applied)

        #2 Data Entry Setup
        self.data_entry = DataEntry(self, self.traits_manager)
        self.data_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nw")

        #3 Summary Manager Setup
        self.summary_manager = SummaryManager(self)
        self.summary_manager.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nw")

        # Save Button
        self.save_button = ttk.Button(self, text="Save", command=self.save_record)
        self.save_button.grid(row=1, column=0, padx=10, pady=10)

    def on_traits_applied(self, selected_traits):
        """Callback when traits are applied."""
        print(f"Selected Traits: {selected_traits}")

    def save_record(self):
        """ Save record and update summary. """
        self.data_entry.save_record()
        new_record = self.data_entry.traits_manager.get_entry_values()
        new_record['Timestamp'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.summary_manager.add_record(new_record)

if __name__ == "__main__":
    app = FishRecorder()
    app.mainloop()
