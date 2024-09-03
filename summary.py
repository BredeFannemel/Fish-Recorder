import tkinter as tk

class Summary(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        self.summary_label = tk.Label(self, text="Summary")
        self.summary_label.grid(row=0, column=0, columnspan=2, pady=10)
        self.summary_text = tk.Text(self, height=10, width=50)
        self.summary_text.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

    def update_summary(self, recorded_data):
        self.summary_text.delete(1.0, tk.END)
        if recorded_data:
            for record in recorded_data:
                self.summary_text.insert(tk.END, f"{record}\n")
        else:
            self.summary_text.insert(tk.END, "No records available.\n")
