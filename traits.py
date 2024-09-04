import tkinter as tk

class TraitsManager:
    def __init__(self, master, traits, form_frame, callback):
        self.traits = traits
        self.form_frame = form_frame
        self.callback = callback
        self.selected_traits = []

        # Checkbuttons for each trait
        self.trait_vars = {}
        self.checkbuttons = {}
        for i, trait in enumerate(self.traits):
            var = tk.BooleanVar()
            chk = tk.Checkbutton(master, text=trait, variable=var)
            chk.grid(row=i, column=0, sticky="w")
            self.trait_vars[trait] = var
            self.checkbuttons[trait] = chk

        # Apply button
        self.apply_button = tk.Button(master, text="Apply Selection", command=self.apply_selection)
        self.apply_button.grid(row=len(self.traits), column=0, pady=5)

    def apply_selection(self):
        """Apply the selected traits and show corresponding entry fields."""
        self.selected_traits = [trait for trait in self.traits if self.trait_vars[trait].get()]
        self.callback(self.selected_traits)
        self.update_form()

    def update_form(self):
        """Update the form fields based on the selected traits."""
        for widget in self.form_frame.winfo_children():
            widget.destroy()

        self.entries = {}
        for i, trait in enumerate(self.selected_traits):
            label = tk.Label(self.form_frame, text=f"{trait}:")
            label.grid(row=i, column=0, sticky="e")
            entry = tk.Entry(self.form_frame)
            entry.grid(row=i, column=1, sticky="w")
            self.entries[trait] = entry

    def get_entry_values(self):
        """Retrieve values entered in the form."""
        return {trait: self.entries[trait].get() for trait in self.selected_traits}
