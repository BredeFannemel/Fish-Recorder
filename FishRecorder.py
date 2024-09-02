import tkinter as tk
from tkinter import ttk, messagebox
import csv
from collections import defaultdict

class FishRecorder(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Fish Recorder")
        self.selected_fields = ["Animal ID", "Weight", "Sex", "Maturation", "Selection", "Freefield 1", "Freefield 2"]
        self.recorded_data = []  # Initialize the list to store records
        self.statistics_options = defaultdict(list)  # Store options for statistics
        self.create_widgets()

    def create_widgets(self):
        # Animal ID entry
        self.animal_entry_label = ttk.Label(self, text="Animal ID:")
        self.animal_entry = ttk.Entry(self)
        self.animal_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        self.animal_entry_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")

        # Weight entry with float validation
        self.weight_label = ttk.Label(self, text="Weight:")
        self.weight_entry = ttk.Entry(self, validate="key", validatecommand=(self.register(self.validate_float), '%P'))
        self.weight_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.weight_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # Sex combobox
        self.sex_label = ttk.Label(self, text="Sex:")
        self.sex_combobox = ttk.Combobox(self, values=["Female", "Male", "Unknown"], state="readonly")
        self.sex_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.sex_combobox.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Maturation combobox
        self.maturation_label = ttk.Label(self, text="Maturation:")
        self.maturation_combobox = ttk.Combobox(self, values=["Mature", "Immature", "Unknown"], state="readonly")
        self.maturation_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.maturation_combobox.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        # Selection combobox
        self.selection_label = ttk.Label(self, text="Selection:")
        self.selection_combobox = ttk.Combobox(self, values=["Selected", "Culled"], state="readonly")
        self.selection_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.selection_combobox.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        # Freefield1 entry
        self.freefield1_entry_label = ttk.Label(self, text="Freefield 1:")
        self.freefield1_entry = ttk.Entry(self)
        self.freefield1_entry.grid(row=5, column=1, padx=10, pady=5, sticky="w")
        self.freefield1_entry_label.grid(row=5, column=0, padx=10, pady=5, sticky="e")

        # Freefield2 entry
        self.freefield2_entry_label = ttk.Label(self, text="Freefield 2:")
        self.freefield2_entry = ttk.Entry(self)
        self.freefield2_entry.grid(row=6, column=1, padx=10, pady=5, sticky="w")
        self.freefield2_entry_label.grid(row=6, column=0, padx=10, pady=5, sticky="e")

        # Save button
        self.save_button = ttk.Button(self, text="Save", command=self.save_record)
        self.save_button.grid(row=7, column=0, columnspan=2, pady=10)
        self.save_button.bind("<Return>", lambda event: self.save_record())

        # Statistics configuration button
        self.stats_button = ttk.Button(self, text="Configure Statistics", command=self.configure_statistics)
        self.stats_button.grid(row=8, column=0, columnspan=2, pady=10)

        # Summary Table
        self.summary_label = ttk.Label(self, text="Summary")
        self.summary_label.grid(row=9, column=0, columnspan=2, pady=10)
        self.summary_text = tk.Text(self, height=10, width=50)
        self.summary_text.grid(row=10, column=0, columnspan=2, padx=10, pady=5)

    def validate_float(self, value_if_allowed):
        """ Validate that the input is a float number """
        if value_if_allowed in ["", "-", ".", "-."]:
            return True
        try:
            float(value_if_allowed)
            return True
        except ValueError:
            return False

    def save_record(self):
        # Gather data from fields
        record = {
            "Animal ID": self.animal_entry.get().strip(),
            "Weight": self.weight_entry.get().strip(),
            "Sex": self.sex_combobox.get(),
            "Maturation": self.maturation_combobox.get(),
            "Selection": self.selection_combobox.get(),
            "Freefield 1": self.freefield1_entry.get().strip(),
            "Freefield 2": self.freefield2_entry.get().strip(),
        }

        # Check if all required fields are filled
        if all(record.values()):
            # Store the record
            self.recorded_data.append(record)
            self.update_summary()
            self.save_to_file(record)
            self.clear_form()

            messagebox.showinfo("Success", "Record saved successfully!")
        else:
            messagebox.showwarning("Warning", "Please fill out all fields.")

    def save_to_file(self, record):
        """ Save the current record to a text file in tabulated format """
        with open('fish_records.txt', 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.selected_fields, delimiter='\t')
            if file.tell() == 0:  # Write header if the file is new/empty
                writer.writeheader()
            writer.writerow(record)

    def clear_form(self):
        """ Clear all fields after saving a record """
        self.animal_entry.delete(0, tk.END)
        self.weight_entry.delete(0, tk.END)
        self.sex_combobox.set('')
        self.maturation_combobox.set('')
        self.selection_combobox.set('')
        self.freefield1_entry.delete(0, tk.END)
        self.freefield2_entry.delete(0, tk.END)

    def update_summary(self):
        """ Update the summary table with recorded data """
        self.summary_text.delete(1.0, tk.END)
        if self.recorded_data:
            for record in self.recorded_data:
                self.summary_text.insert(tk.END, f"{record}\n")
        else:
            self.summary_text.insert(tk.END, "No records available.\n")

    def configure_statistics(self):
        """ Open a new window to configure which statistics to display """
        self.stats_window = tk.Toplevel(self)
        self.stats_window.title("Configure Statistics")

        # Checkbuttons for statistics options
        self.avg_weight_var = tk.BooleanVar()
        self.avg_weight_sex_var = tk.BooleanVar()
        self.avg_weight_maturation_var = tk.BooleanVar()

        tk.Checkbutton(self.stats_window, text="Average Weight", variable=self.avg_weight_var).grid(row=0, column=0, sticky="w")
        tk.Checkbutton(self.stats_window, text="Average Weight by Sex", variable=self.avg_weight_sex_var).grid(row=1, column=0, sticky="w")
        tk.Checkbutton(self.stats_window, text="Average Weight by Maturation", variable=self.avg_weight_maturation_var).grid(row=2, column=0, sticky="w")

        ttk.Button(self.stats_window, text="Apply", command=self.apply_statistics).grid(row=3, column=0, pady=10)

    def apply_statistics(self):
        """ Apply the selected statistics configuration """
        self.statistics_options.clear()

        if self.avg_weight_var.get():
            self.statistics_options['Overall'].append('Weight')
        if self.avg_weight_sex_var.get():
            self.statistics_options['Sex'].append('Weight')
        if self.avg_weight_maturation_var.get():
            self.statistics_options['Maturation'].append('Weight')

        self.update_summary_with_statistics()
        self.stats_window.destroy()

    def update_summary_with_statistics(self):
        """ Update the summary with selected statistics """
        summary_stats = {}

        # Calculate and display average weight
        if 'Overall' in self.statistics_options:
            avg_weight = sum(float(record["Weight"]) for record in self.recorded_data) / len(self.recorded_data)
            summary_stats['Average Weight'] = avg_weight

        if 'Sex' in self.statistics_options:
            sex_groups = defaultdict(list)
            for record in self.recorded_data:
                sex_groups[record["Sex"]].append(float(record["Weight"]))
            for sex, weights in sex_groups.items():
                summary_stats[f'Average Weight ({sex})'] = sum(weights) / len(weights)

        if 'Maturation' in self.statistics_options:
            maturation_groups = defaultdict(list)
            for record in self.recorded_data:
                maturation_groups[record["Maturation"]].append(float(record["Weight"]))
            for maturation, weights in maturation_groups.items():
                summary_stats[f'Average Weight ({maturation})'] = sum(weights) / len(weights)

        self.update_summary()
        self.summary_text.insert(tk.END, "\nStatistics:\n")
        for stat, value in summary_stats.items():
            self.summary_text.insert(tk.END, f"{stat}: {value:.2f}\n")

if __name__ == "__main__":
    app = FishRecorder()
    app.mainloop()


