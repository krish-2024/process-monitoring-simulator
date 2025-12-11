import tkinter as tk
from tkinter import ttk
import psutil
from .process_utils import list_processes


class DashboardGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Real-Time Process Monitoring Dashboard")
        self.root.geometry("700x500")

        # CPU + RAM Labels
        self.cpu_label = tk.Label(root, text="CPU Usage: ", font=("Arial", 12))
        self.cpu_label.pack()

        self.memory_label = tk.Label(root, text="Memory Usage: ", font=("Arial", 12))
        self.memory_label.pack()

        # Process Table
        columns = ("PID", "Name", "CPU%", "MEM%")
        self.tree = ttk.Treeview(root, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)

        self.tree.pack(fill=tk.BOTH, expand=True)

        # Start update loop
        self.update_dashboard()

    def update_dashboard(self):
        # Update CPU + RAM
        cpu = psutil.cpu_percent()
        mem = psutil.virtual_memory().percent

        self.cpu_label.config(text=f"CPU Usage: {cpu}%")
        self.memory_label.config(text=f"Memory Usage: {mem}%")

        # Refresh process table
        for row in self.tree.get_children():
            self.tree.delete(row)

        processes = sorted(list_processes(), key=lambda x: x["cpu_percent"], reverse=True)

        for proc in processes[:20]:  # Show top 20
            self.tree.insert("", tk.END, values=(
                proc["pid"],
                proc["name"],
                proc["cpu_percent"],
                round(proc["memory_percent"], 2)
            ))

        # Repeat every 1000ms (1 second)
        self.root.after(1000, self.update_dashboard)
