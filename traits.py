import tkinter as tk

class TraitsManager:
    def __init__(self, master, traits, apply_callback):
        self.master = master
        self.traits = traits
        self.apply_callback = apply_callback

        self.trait_vars = {trait: tk.BooleanVar() for trait in self.traits}
        for i, trait in enumerate(self.traits, start=1):
            tk.Checkbutton(self.master, text=trait, variable=self.trait_vars[trait]).grid(row=i, column=0, sticky="w")

        self.apply_traits_button = tk.Button(self.master, text="Apply Selection", command=self.apply_traits)
        self.apply_traits_button.grid(row=len(self.traits) + 1, column=0, pady=5)

    def apply_trait_selection(self):
        """Apply selected traits and dynamically create form fields."""
        for widget in self.form_frame.winfo_children():
            widget.destroy()  # Clear previous widgets

        self.selected_traits = [trait for trait, var in self.trait_selection_vars.items() if var.get()]

        self.entry_widgets = {}
        for idx, trait in enumerate(self.selected_traits):
            label = ttk.Label(self.form_frame, text=f"{trait}:")
            label.grid(row=idx, column=0, padx=10, pady=5, sticky="e")

            if trait == "Weight":
                entry = ttk.Entry(self.form_frame, validate="key", validatecommand=(self.register(self.validate_float), '%P'))
            elif trait == "Sex":
                entry = ttk.Combobox(self.form_frame, values=["Female", "Male", "Unknown"], state="readonly")
            elif trait == "Maturation":
                entry = ttk.Combobox(self.form_frame, values=["Mature", "Immature", "Unknown"], state="readonly")
            elif trait == "Selection":
                entry = ttk.Combobox(self.form_frame, values=["Selected", "Culled"], state="readonly")
            else:
                entry = ttk.Entry(self.form_frame)

            entry.grid(row=idx, column=1, padx=10, pady=5, sticky="w")
            self.entry_widgets[trait] = entry
