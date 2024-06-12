import tkinter as tk
from Scheduler import Rapat, schedule_rapats
import matplotlib.pyplot as plt
import matplotlib.backends.backend_tkagg as tkagg
from matplotlib.figure import Figure

class App:
    def __init__(self, root):
        self.root = root
        self.root.configure(bg='#31312d')
        self.entries = []
        self.rapats = []

        self.label = tk.Label(root, text="Enter number of meetings:", bg='#31312d', fg='white')
        self.label.pack(pady = 10)

        self.entry = tk.Entry(root, fg='black', bg='white')  # Change text color to black and background color to white
        self.entry.pack(pady = 10)

        self.button = tk.Button(root, text="Submit", command=self.create_entries, fg='white', bg='#1b99ee')
        self.button.pack(pady = 10)

    def create_entries(self):
        num = int(self.entry.get())
        self.entry.destroy()
        self.label.destroy()
        self.button.destroy()

        for i in range(num):
            frame = tk.Frame(self.root, bg='#31312d')
            frame.pack()

            label = tk.Label(frame, text=f"Meeting {i+1}:", bg='#31312d', fg='white')
            label.grid(row=0, column=0)

            name_label = tk.Label(frame, text="Name:", bg='#31312d', fg='white')
            name_label.grid(row=0, column=1)
            name_entry = tk.Entry(frame, fg='black', bg='white')  # Change text color to black and background color to white
            name_entry.grid(row=0, column=2, padx=10, pady=10)

            availability_label = tk.Label(frame, text="Availability:", bg='#31312d', fg='white')
            availability_label.grid(row=0, column=3)
            availability_entry = tk.Entry(frame, fg='black', bg='white')  # Change text color to black and background color to white
            availability_entry.grid(row=0, column=4, padx=10, pady=10)

            unavailability_label = tk.Label(frame, text="Unavailability:", bg='#31312d', fg='white')
            unavailability_label.grid(row=0, column=5)
            unavailability_entry = tk.Entry(frame, fg='black', bg='white')  # Change text color to black and background color to white
            unavailability_entry.grid(row=0, column=6, padx=10, pady=10)

            duration_label = tk.Label(frame, text="Duration:", bg='#31312d', fg='white')
            duration_label.grid(row=0, column=7)
            duration_entry = tk.Entry(frame, fg='black', bg='white')  # Change text color to black and background color to white
            duration_entry.grid(row=0, column=8, padx=10, pady=10)

            self.entries.append((name_entry, availability_entry, unavailability_entry, duration_entry))

        self.button = tk.Button(self.root, text="Schedule Meetings", command=self.schedule_meetings, fg='white', bg='#1b99ee')
        self.button.pack(pady = 20)

        self.output = tk.Text(self.root, fg='black', bg='white')
        self.output.pack(pady=20)

    def schedule_meetings(self):
        for entry in self.entries:
            name, availability, unavailability, duration = entry
            self.rapats.append(Rapat(name.get(), int(availability.get()), int(unavailability.get()), int(duration.get())))

        scheduled_rapats = schedule_rapats(self.rapats)

        # Create a new figure for the Gantt chart
        fig = Figure(figsize=(6, 3), dpi=100)
        ax = fig.add_subplot(111)

        yticks = []
        yticklabels = []
        for i, rapat in enumerate(scheduled_rapats):
            start = rapat.availability
            end = rapat.estimate_of_complete
            ax.broken_barh([(start, end-start)], (i-0.4, 0.8), facecolors='blue')
            yticks.append(i)
            yticklabels.append(rapat.name)

        ax.set_yticks(yticks)
        ax.set_yticklabels(yticklabels)
        ax.set_xlabel('Time')

        # Create a new window to display the Gantt chart
        chart_window = tk.Toplevel(self.root)
        chart_window.title('Gantt Chart')

        # Create a canvas to display the figure in the new window
        canvas = tkagg.FigureCanvasTkAgg(fig, master=chart_window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        for rapat in scheduled_rapats:
            self.output.insert(tk.END, f"Rapat {rapat.name} diadakan pada jam {rapat.availability} dan selesai pada jam {rapat.estimate_of_complete}\n")

root = tk.Tk()
app = App(root)
root.mainloop()