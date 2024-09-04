import tkinter as tk
from tkinter import ttk

class TraitsManager:
    def __init__(self, master, traits, form_frame, apply_callback):
        self.master = master
        self.traits = traits
        self.form_frame = form_frame
        self.apply_callback = apply_callback

        # Create BooleanVars for each trait
        self.trait_vars = {trait: tk.BooleanVar() for trait in self.traits}

        # Create checkboxes for each trait
        for i, trait in enumerate(self.traits):
            tk.Checkbutton(self.master, text=trait, variable=self.trait_vars[trait]).grid(row=i, column=0, sticky="w")

        # Apply selection button
        self.apply_traits_button = tk.Button(self.master, text="Apply Selection", command=self.apply_trait_selection)
        self.apply_traits_button.grid(row=len(self.traits) + 1, column=0, pady=5)

        # Dictionary to store entry widgets
        self.entry_widgets = {}

    def apply_trait_selection(self):
        """Apply selected traits and dynamically create form fields."""
        # Clear previous widgets
        for widget in self.form_frame.winfo_children():
            widget.destroy()

        # Get selected traits
        selected_traits = [trait for trait, var in self.trait_vars.items() if var.get()]

        # Create form fields based on selected traits
        for idx, trait in enumerate(selected_traits):
            label = tk.Label(self.form_frame, text=f"{trait}:")
            label.grid(row=idx, column=0, padx=10, pady=5, sticky="e")

            # Assign the appropriate input type for each trait
            if trait == "Weight":
                entry = ttk.Entry(self.form_frame, validate="key")
            elif trait == "Sex":
                entry = ttk.Combobox(self.form_frame, values=["Male", "Female", "Unknown"], state="readonly")
            elif trait == "Maturation":
                entry = ttk.Combobox(self.form_frame, values=["Mature", "Immature", "Unknown"], state="readonly")
            elif trait == "Selection":
                entry = ttk.Combobox(self.form_frame, values=["Selected", "Culled"], state="readonly")
            else:
                entry = ttk.Entry(self.form_frame)

            entry.grid(row=idx, column=1, padx=10, pady=5, sticky="w")
            self.entry_widgets[trait] = entry

        # Call the apply callback if necessary
        if self.apply_callback:
            self.apply_callback(selected_traits)

    def get_entry_values(self):
        """Returns the current values in the form."""
        return {trait: widget.get() for trait, widget in self.entry_widgets.items()}

    def clear_entries(self):
        """Clear all the entry fields."""
        for widget in self.entry_widgets.values():
            widget.delete(0, tk.END)

