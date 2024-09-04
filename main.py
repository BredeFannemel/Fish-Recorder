import tkinter as tk
from tkinter import ttk
from traits import TraitsManager

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

        #2 Save Button
        self.save_button = ttk.Button(self, text="Save", command=self.save_record)
        self.save_button.grid(row=1, column=0, padx=10, pady=10)

    def on_traits_applied(self, selected_traits):
        """Callback when traits are applied."""
        print(f"Selected Traits: {selected_traits}")

    def save_record(self):
        """Save the record."""
        values = self.traits_manager.get_entry_values()
        print(f"Record to Save: {values}")
        self.traits_manager.clear_entries()

if __name__ == "__main__":
    app = FishRecorder()
    app.mainloop()
