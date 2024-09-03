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

    def apply_traits(self):
        """ Apply selected traits by calling the provided callback """
        selected_traits = [trait for trait, var in self.trait_vars.items() if var.get()]
        self.apply_callback(selected_traits)
