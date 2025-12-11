import tkinter as tk
from monitor.dashboard_gui import DashboardGUI

def main():
    root = tk.Tk()
    DashboardGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
