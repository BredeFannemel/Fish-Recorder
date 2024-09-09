import tkinter as tk
from tkinter import ttk, messagebox

class DataEntry(tk.Frame):
    def __init__(self, master, traits_manager):
        super().__init__(master)
        self.traits_manager = traits_manager
        self.plate_selected = False
        self.current_well_index = 1  # Track the current well for automatic assignment

        # Plate Selection Widgets
        self.plate_var = tk.StringVar(value="SB2023Test_01")
        self.well_var = tk.StringVar()

        self.plate_label = tk.Label(self, text="Plate:")
        self.plate_label.grid(row=0, column=0, sticky="e")
        self.plate_entry = tk.Entry(self, textvariable=self.plate_var)
        self.plate_entry.grid(row=0, column=1, sticky="w")

        self.well_label = tk.Label(self, text="Well:")
        self.well_label.grid(row=1, column=0, sticky="e")
        self.well_entry = tk.Entry(self, textvariable=self.well_var)
        self.well_entry.grid(row=1, column=1, sticky="w")

        # Confirm Plate Selection
        self.confirm_button = tk.Button(self, text="Confirm Plate", command=self.confirm_plate)
        self.confirm_button.grid(row=2, column=0, columnspan=2, pady=5)

        # Display plate
        self.well_plate_frame = tk.Frame(self)
        self.well_plate_frame.grid(row=4, column=0, columnspan=2, pady=10)
        self.wells = {}
        self.create_well_plate()

        # New Plate Button
        self.new_plate_button = tk.Button(self, text="New Plate", command=self.new_plate)
        self.new_plate_button.grid(row=3, column=0, columnspan=2, pady=5)

    def confirm_plate(self):
        """Confirm the selected plate."""
        if not self.plate_selected:
            plate = self.plate_var.get()
            self.plate_selected = True
            messagebox.showinfo("Plate Confirmed", f"Plate {plate} confirmed.")
        else:
            messagebox.showwarning("Plate Already Confirmed", "You have already confirmed a plate. Use 'New Plate' to change.")

    def new_plate(self):
        """Allow user to change the plate."""
        self.plate_selected = False
        self.plate_var.set("")
        self.well_var.set("")
        self.plate_entry.config(state=tk.NORMAL)
        self.well_entry.config(state=tk.NORMAL)
        self.current_well_index = 1  # Reset well assignment index

    def assign_well(self):
        """Automatic well assignment logic."""
        rows = "ABCDEFGH"
        cols = [str(i).zfill(2) for i in range(1, 13)]
        # Skip A01 for control, starting from A02
        available_wells = [row + col for row in rows for col in cols if row + col != "A01"]
        
        if self.current_well_index >= len(available_wells):
            return None  # No wells available

        next_well = available_wells[self.current_well_index]
        self.current_well_index += 1
        return next_well
