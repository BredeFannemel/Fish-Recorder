import tkinter as tk
from tkinter import messagebox

class DataEntry(tk.Frame):
    def __init__(self, master, traits_manager):
        super().__init__(master)
        self.traits_manager = traits_manager
        self.current_plate = 1
        self.current_well_index = 1
        self.well_plate_labels = []
        self.update_well_plate_display()
        
        # Dynamic form based on selected traits
        self.form_frame = tk.Frame(self)
        self.form_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        self.traits_manager.form_frame = self.form_frame  # Link form frame to traits manager
        self.traits_manager.apply_trait_selection()  # Initialize form with selected traits

        # Plate and Well info
        self.plate_label = tk.Label(self, text="Plate:")
        self.plate_entry = tk.Entry(self)
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

        # Confirm Plate Selection
        self.confirm_button = tk.Button(self, text="Confirm Plate", command=self.confirm_plate)
        self.confirm_button.grid(row=2, column=0, columnspan=2, pady=5)

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
                label = tk.Label(self.well_plate_labels, text=well_name, bg=color, width=3, height=1, relief="solid")
                label.grid(row=i, column=j, padx=1, pady=1)
                self.well_plate_labels.append(label)

        # Process the saving logic as needed
        print("Record saved:", entry_values)
