import tkinter as tk
from plot import Plot  # Import PlotManager from plot.py
from summary import SummaryManager  # Import SummaryManager from summary.py
from traits import TraitsManager  # Import TraitsManager from traits.py
from import_export import ImportManager  # Import ImportManager from importer.py

class FishRecorderApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Fish Recorder")

        # Create main frames
        self.input_frame = tk.Frame(self)
        self.input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        self.plot_frame = tk.Frame(self)
        self.plot_frame.grid(row=0, column=1, padx=10, pady=10, sticky="ne")

        self.summary_frame = tk.Frame(self)
        self.summary_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Initialize components
        self.plot_manager = PlotManager(self.plot_frame)
        self.summary_manager = SummaryManager(self.summary_frame)

        self.traits = ["Animal ID", "Weight", "Sex", "Maturation", "Selection", "Freefield 1", "Freefield 2"]
        self.traits_manager = TraitsManager(self.input_frame, self.traits, self.apply_traits)

        self.statistics = ["Number of Fish Recorded", "Average Weight", "Average Weight per Sex", 
                           "Percentage of Mature Fish", "Number of Registered Today"]

        self.import_manager = ImportManager(self.input_frame)

        # Create the save button
        self.save_button = tk.Button(self.input_frame, text="Save", command=self.save_record)
        self.save_button.grid(row=len(self.traits) + len(self.statistics) + 3, column=0, pady=5)

    def apply_traits(self, selected_traits):
        """ Handle the application of selected traits """
        print("Selected traits:", selected_traits)
        # Logic to update UI based on selected traits

    def save_record(self):
        """ Handle saving the record """
        # Logic to save the record
        print("Record saved!")

if __name__ == "__main__":
    app = FishRecorderApp()
    app.mainloop()

