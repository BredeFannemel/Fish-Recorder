import tkinter as tk
from data_entry import DataEntry
from summary import Summary
from plot import Plot
from import_export import ImportExport

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Fish Recorder")

        # Initialize the components
        self.data_entry = DataEntry(self)
        self.summary = Summary(self)
        self.plot = Plot(self)
        self.import_export = ImportExport(self)

        # Layout
        self.data_entry.grid(row=0, column=0, padx=10, pady=10)
        self.summary.grid(row=1, column=0, padx=10, pady=10)
        self.plot.grid(row=0, column=10, rowspan=2, padx=10, pady=10)

        # Import file button
        self.import_button = tk.Button(self, text="Import File", command=self.import_export.import_file)
        self.import_button.grid(row=2, column=0, columnspan=2, pady=10)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
