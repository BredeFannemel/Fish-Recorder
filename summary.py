import tkinter as tk

class SummaryManager:
    def __init__(self, master):
        self.master = master
        self.summary_text = tk.Text(self.master, height=10, width=100)
        self.summary_text.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
        self.records_by_selection = {}

    def update_summary(self, records):
        """ Update the summary display with new records """
        self.summary_text.delete(1.0, tk.END)
        if records:
            for record in records:
                self.summary_text.insert(tk.END, f"{record}\n")
        else:
            self.summary_text.insert(tk.END, "No records available.\n")

    def add_record(self, record):
        """ Add a new record to the summary """
        selection = record.get('Selection', 'Unselected')
        if selection not in self.records_by_selection:
            self.records_by_selection[selection] = []
        self.records_by_selection[selection].append(record)
        self.update_summary(self.records_by_selection[selection])
