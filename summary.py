import tkinter as tk
from collections import defaultdict
from statistics import mean

class SummaryManager:
    def __init__(self, master):
        self.master = master

        # Layout
        self.summary_frame = tk.Frame(self.master)
        self.summary_frame.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")

        # Text widget for displaying the summary
        self.summary_text = tk.Text(self.summary_frame, height=10, width=100, state=tk.DISABLED)
        self.summary_text.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")

        # Scrollbar for the text widget
        scrollbar = tk.Scrollbar(self.summary_frame, command=self.summary_text.yview)
        scrollbar.grid(row=0, column=1, sticky='ns')
        self.summary_text['yscrollcommand'] = scrollbar.set

        # Initialize data structures to hold records
        self.records = []
        self.records_by_day = defaultdict(list)
        self.records_by_sex = defaultdict(list)
        self.records_by_selection = defaultdict(list)

    def add_record(self, record):
        """ Add a new record and update the summary. """
        self.records.append(record)
        date = record['Timestamp'].split()[0]
        self.records_by_day[date].append(record)
        self.records_by_sex[record['Sex']].append(record)
        self.records_by_selection[record['Selection']].append(record)
        self.update_summary()

    def update_summary(self):
        """ Update the summary display with calculated statistics. """
        self.summary_text.config(state=tk.NORMAL)
        self.summary_text.delete(1.0, tk.END)

        if not self.records:
            self.summary_text.insert(tk.END, "No records available.\n")
        else:
            # Total number of fish recorded
            total_fish = len(self.records)
            self.summary_text.insert(tk.END, f"Total fish recorded: {total_fish}\n")

            # Average weight
            weights = [float(record['Weight']) for record in self.records if 'Weight' in record and record['Weight']]
            avg_weight = mean(weights) if weights else 'N/A'
            self.summary_text.insert(tk.END, f"Average weight: {avg_weight:.2f} g\n")

            # Fish count per day
            self.summary_text.insert(tk.END, "\nFish recorded per day:\n")
            for day, records in self.records_by_day.items():
                self.summary_text.insert(tk.END, f"  {day}: {len(records)} fish\n")

            # Average weight per sex
            self.summary_text.insert(tk.END, "\nAverage weight per sex:\n")
            for sex, records in self.records_by_sex.items():
                sex_weights = [float(record['Weight']) for record in records if 'Weight' in record and record['Weight']]
                avg_sex_weight = mean(sex_weights) if sex_weights else 'N/A'
                self.summary_text.insert(tk.END, f"  {sex}: {avg_sex_weight:.2f} g\n")

            # Fish count by selection
            self.summary_text.insert(tk.END, "\nFish count by selection:\n")
            for selection, records in self.records_by_selection.items():
                self.summary_text.insert(tk.END, f"  {selection}: {len(records)} fish\n")

        self.summary_text.config(state=tk.DISABLED)

    def reset_summary(self):
        """ Reset all summaries. """
        self.records.clear()
        self.records_by_day.clear()
        self.records_by_sex.clear()
        self.records_by_selection.clear()
        self.update_summary()
