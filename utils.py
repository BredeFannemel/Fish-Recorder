import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class PlotManagerSummary:
    def __init__(self, master):
        self.master = master
        self.fig, self.ax = plt.subplots(figsize=(6, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.get_tk_widget().pack()

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
