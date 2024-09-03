import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class FishRecorder(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Fish Recorder")
        self.available_traits = ["Animal ID", "Weight", "Sex", "Maturation", "Selection", "Freefield 1", "Freefield 2"]
        self.selected_traits = []
        self.available_stats = ["Number of Fish Recorded", "Average Weight", "Average Weight per Sex", "Percentage of Mature Fish", "Number of Registered Today"]
        self.selected_stats = []
        self.recorded_data = []  # Initialize the list to store records
        self.load_existing_data()
        self.animal_info = {}  # To store information from imported file
        self.create_widgets()

    def create_widgets(self):
        # Trait selection
        self.trait_selection_label = ttk.Label(self, text="Select Traits to Record:")
        self.trait_selection_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.trait_selection_vars = {trait: tk.BooleanVar() for trait in self.available_traits}
        for idx, trait in enumerate(self.available_traits):
            chk = ttk.Checkbutton(self, text=trait, variable=self.trait_selection_vars[trait])
            chk.grid(row=idx + 1, column=0, padx=10, pady=2, sticky="w")

        # Apply trait selection button
        self.apply_button = ttk.Button(self, text="Apply Selection", command=self.apply_trait_selection)
        self.apply_button.grid(row=len(self.available_traits) + 1, column=0, pady=10)

        # Statistic selection
        self.stat_selection_label = ttk.Label(self, text="Select Statistics to Display:")
        self.stat_selection_label.grid(row=len(self.available_traits) + 2, column=0, padx=10, pady=5, sticky="w")

        self.stat_selection_vars = {stat: tk.BooleanVar() for stat in self.available_stats}
        for idx, stat in enumerate(self.available_stats):
            chk = ttk.Checkbutton(self, text=stat, variable=self.stat_selection_vars[stat])
            chk.grid(row=len(self.available_traits) + 3 + idx, column=0, padx=10, pady=2, sticky="w")

        # Apply statistic selection button
        self.apply_stat_button = ttk.Button(self, text="Apply Statistics", command=self.apply_stat_selection)
        self.apply_stat_button.grid(row=len(self.available_traits) + 3 + len(self.available_stats), column=0, pady=10)

        # Import file button
        self.import_button = ttk.Button(self, text="Import Animal Information", command=self.import_data)
        self.import_button.grid(row=len(self.available_traits) + 4 + len(self.available_stats), column=0, pady=10)

        # Dynamic form area
        self.form_frame = ttk.Frame(self)
        self.form_frame.grid(row=0, column=1, rowspan=len(self.available_traits) + 4 + len(self.available_stats), padx=10, pady=5, sticky="n")

        # Save button
        self.save_button = ttk.Button(self, text="Save", command=self.save_record)
        self.save_button.grid(row=len(self.available_traits) + 5 + len(self.available_stats), column=0, columnspan=2, pady=10)
        self.save_button.bind("<Return>", lambda event: self.save_record())

        # Summary Table
        self.summary_label = ttk.Label(self, text="Summary")
        self.summary_label.grid(row=len(self.available_traits) + 6 + len(self.available_stats), column=0, columnspan=2, pady=10)
        self.summary_text = tk.Text(self, height=10, width=50)
        self.summary_text.grid(row=len(self.available_traits) + 7 + len(self.available_stats), column=0, columnspan=2, padx=10, pady=5)

        # Histogram Button
        self.histogram_button = ttk.Button(self, text="Show Weight Histogram", command=self.show_histogram)
        self.histogram_button.grid(row=len(self.available_traits) + 8 + len(self.available_stats), column=0, pady=10)

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

    def apply_stat_selection(self):
        """Apply selected statistics to display in the summary."""
        self.selected_stats = [stat for stat, var in self.stat_selection_vars.items() if var.get()]
        self.update_summary()

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
        """ Save the current record """
        record = {trait: self.entry_widgets[trait].get().strip() for trait in self.selected_traits}

        # Ensure Animal ID is filled out, the rest can be optional
        if "Animal ID" in record and record["Animal ID"]:
            # Check for duplicate Animal ID in existing records
            if self.is_duplicate_animal_id(record["Animal ID"]):
                self.entry_widgets["Animal ID"].config(background="red")
                messagebox.showwarning("Duplicate ID", "This Animal ID already exists in the records.")
            else:
                self.entry_widgets["Animal ID"].config(background="white")  # Reset background color
                # Add timestamp
                record["Timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                # Store the record
                self.recorded_data.append(record)
                self.update_summary()
                self.save_to_file(record)
                self.clear_form()

                messagebox.showinfo("Success", "Record saved successfully!")
        else:
            messagebox.showwarning("Warning", "Please fill out the Animal ID field.")

    def is_duplicate_animal_id(self, animal_id):
        """ Check if the given Animal ID already exists in the recorded data """
        for record in self.recorded_data:
            if record["Animal ID"] == animal_id:
                return True
        return False

    def save_to_file(self, record):
        """ Save the current record to a text file in tabulated format """
        with open('fish_records.txt', 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.selected_traits + ["Timestamp"], delimiter='\t')
            if file.tell() == 0:  # Write header if the file is new/empty
                writer.writeheader()
            writer.writerow(record)

    def load_existing_data(self):
        """ Load existing records from the file into the recorded_data list """
        try:
            with open('fish_records.txt', 'r') as file:
                reader = csv.DictReader(file, delimiter='\t')
                self.recorded_data = [row for row in reader]
        except FileNotFoundError:
            pass  # No existing file found, start with an empty list

    def import_data(self):
        """ Import animal data from a tabulated text file """
        file_path = filedialog.askopenfilename(
            title="Select file",
            filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
        )
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    reader = csv.DictReader(file, delimiter='\t')
                    self.animal_info = {row["Animal ID"]: row for row in reader}
                    messagebox.showinfo("Import Success", "Animal information imported successfully!")
            except Exception as e:
                messagebox.showerror("Import Error", f"An error occurred while importing: {e}")

    def clear_form(self):
        """ Clear all fields after saving a record """
        for entry in self.entry_widgets.values():
            if isinstance(entry, ttk.Combobox):
                entry.set('')
            else:
                entry.delete(0, tk.END)

    def update_summary(self):
        """ Update the summary table with recorded data """
        self.summary_text.delete(1.0, tk.END)
        if not self.recorded_data:
            self.summary_text.insert(tk.END, "No records available.\n")
            return

        summary = []

        if "Number of Fish Recorded" in self.selected_stats:
            summary.append(f"Number of Fish Recorded: {len(self.recorded_data)}")

        if "Average Weight" in self.selected_stats:
            weights = [float(record["Weight"]) for record in self.recorded_data if "Weight" in record and record["Weight"]]
            if weights:
                average_weight = sum(weights) / len(weights)
                summary.append(f"Average Weight: {average_weight:.2f}")

        if "Average Weight per Sex" in self.selected_stats:
            sexes = ["Female", "Male", "Unknown"]
            for sex in sexes:
                sex_weights = [float(record["Weight"]) for record in self.recorded_data if "Weight" in record and "Sex" in record and record["Sex"] == sex and record["Weight"]]
                if sex_weights:
                    average_weight = sum(sex_weights) / len(sex_weights)
                    summary.append(f"Average Weight ({sex}): {average_weight:.2f}")

        if "Percentage of Mature Fish" in self.selected_stats:
            maturation_count = {"Mature": 0, "Immature": 0, "Unknown": 0}
            for record in self.recorded_data:
                if "Maturation" in record:
                    maturation_count[record["Maturation"]] += 1
            if len(self.recorded_data) > 0:
                mature_percentage = (maturation_count["Mature"] / len(self.recorded_data)) * 100
                summary.append(f"Percentage of Mature Fish: {mature_percentage:.2f}%")

        if "Number of Registered Today" in self.selected_stats:
            today = datetime.now().strftime("%Y-%m-%d")
            registered_today = len([record for record in self.recorded_data if record["Timestamp"].startswith(today)])
            summary.append(f"Number of Registered Today: {registered_today}")

        self.summary_text.insert(tk.END, "\n".join(summary) + "\n")

    def show_histogram(self):
        """ Display a histogram of recorded weights """
        weights = [float(record["Weight"]) for record in self.recorded_data if "Weight" in record and record["Weight"]]
        if weights:
            fig, ax = plt.subplots(figsize=(6, 4))
            ax.hist(weights, bins=10, color='blue', edgecolor='black')
            ax.set_title('Histogram of Fish Weights')
            ax.set_xlabel('Weight')
            ax.set_ylabel('Frequency')

            # Embed the plot into the Tkinter window
            canvas = FigureCanvasTkAgg(fig, master=self)
            canvas.draw()
            canvas.get_tk_widget().grid(row=len(self.available_traits) + 9 + len(self.available_stats), column=0, columnspan=2)

if __name__ == "__main__":
    app = FishRecorder()
    app.mainloop()

