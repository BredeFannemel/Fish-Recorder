import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Plot(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        self.fig, self.ax = plt.subplots(figsize=(5, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().grid(row=1, column=2, padx=10, pady=10)

    def update_histogram(self, weights):
        self.ax.clear()
        self.ax.hist(weights, bins=10, color='blue', edgecolor='black')
        self.ax.set_title("Weight Distribution")
        self.ax.set_xlabel("Weight")
        self.ax.set_ylabel("Number of Fish")
        self.canvas.draw()
