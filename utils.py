import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class PlotManager:
    def __init__(self, master):
        self.master = master
        self.fig, self.ax = plt.subplots(figsize=(6, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.get_tk_widget().pack()

    def update_histogram(self, weights):
        """ Update the histogram with new data """
        self.ax.clear()
        self.ax.hist(weights, bins=10, color='blue', edgecolor='black')
        self.ax.set_title("Weight Distribution")
        self.ax.set_xlabel("Weight")
        self.ax.set_ylabel("Number of Fish")
        self.canvas.draw()
