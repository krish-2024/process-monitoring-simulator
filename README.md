#Real-Time Process Monitoring Dashboard

-A simple Python tool that displays real-time system statistics including:

	-CPU usage

	-Memory usage

	-Running processes (PID, name, CPU%, memory%)

-The project contains two versions:

	-CLI Dashboard (runs in terminal)

	-GUI Dashboard (using Tkinter)


##Project Structure
process_monitoring_dashboard/
│
├── cli.py                  # CLI entry point
├── app.py                  # GUI entry point (Tkinter)
│
├── monitor/
│   ├── __init__.py
│   ├── process_utils.py    # Process listing and utilities
│   ├── dashboard.py        # CLI dashboard logic
│   └── dashboard_gui.py    # GUI dashboard logic
│
└── requirements.txt

## Features
-CLI Version

	-Displays real-time CPU and memory usage

	-Shows top running processes

	-Allows killing a process via PID

	-Refreshes automatically

## Run it using:
```bash
python cli.py --watch
```


## Kill a process:
```bash
python cli.py --kill <PID>
```
-GUI Version (Tkinter)

	-Clean window showing CPU and memory usage

	-Auto-updating process table

	-Refreshes every second

## Run it using:
```bash
python app.py
```

##Installation

-Clone the repository:
```bash
git clone <your-repo-url>
cd process_monitoring_dashboard
```

-Install dependencies:
```bash
pip install -r requirements.txt
```

# Technologies Used

-Python

-psutil — system process & resource monitoring

-Tkinter — GUI interface

-argparse — CLI support
