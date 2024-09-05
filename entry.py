import tkinter as tk
from tkinter import messagebox

class DataEntry(tk.Frame):
    def __init__(self, master, traits_manager):
        super().__init__(master)
        self.traits_manager = traits_manager
        self.plate_selected = False

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

        # New Plate Button
        self.new_plate_button = tk.Button(self, text="New Plate", command=self.new_plate)
        self.new_plate_button.grid(row=3, column=0, columnspan=2, pady=5)

        # Well Plate Display
        self.well_plate_frame = tk.Frame(self)
        self.well_plate_frame.grid(row=4, column=0, columnspan=2, pady=10)
        self.wells = {}
        self.create_well_plate()

        # Initialize current well index
        self.current_well_index = 1

    def confirm_plate(self):
        """Confirm the selected plate."""
        if not self.plate_selected:
            plate = self.plate_var.get()
            self.plate_selected = True
            messagebox.showinfo("Plate Confirmed", f"Plate {plate} confirmed.")
        else:
            messagebox.showwarning("Plate Already Confirmed", "You have already confirmed a plate. Use 'New Plate' to change.")

    def new_plate(self):
        """Allow user to change the plate and reset wells."""
        self.plate_selected = False
        self.plate_var.set("")
        self.well_var.set("")
        self.plate_entry.config(state=tk.NORMAL)
        self.well_entry.config(state=tk.NORMAL)

        # Reset well assignment
        self.current_well_index = 1
        self.reset_well_plate()

    def create_well_plate(self):
        """Create a visual representation of the well plate (8x12 grid)."""
        rows = "ABCDEFGH"
        for i, row in enumerate(rows):
            for col in range(1, 13):
                well_id = f"{row}{col:02d}"
                color = "red" if well_id == "A01" else "white"  # Mark A01 as reserved
                button = tk.Button(self.well_plate_frame, text=well_id, width=4, bg=color, state=tk.NORMAL)
                button.grid(row=i, column=col-1)
                self.wells[well_id] = button

    def reset_well_plate(self):
        """Reset the well plate display."""
        for well_id, button in self.wells.items():
            color = "red" if well_id == "A01" else "white"  # Mark A01 as reserved
            button.config(bg=color)

    def assign_well(self):
        """Assign the next available well."""
        rows = "ABCDEFGH"
        while self.current_well_index < 97:  # Total of 96 wells (A01 to H12)
            row = rows[(self.current_well_index - 1) // 12]  # Calculate row
            col = (self.current_well_index - 1) % 12 + 1     # Calculate column
            well_id = f"{row}{col:02d}"

            # Skip A01 as it is reserved
            if well_id != "A01":
                self.wells[well_id].config(bg="green")  # Mark the well as used
                self.current_well_index += 1
                return well_id

            self.current_well_index += 1
        messagebox.showwarning("No More Wells", "All wells are occupied on this plate.")
        return None
