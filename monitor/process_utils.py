import psutil

def list_processes():
    """Return a list of running processes with basic info."""
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            processes.append(proc.info)
        except psutil.NoSuchProcess:
            continue
    return processes


def kill_process(pid: int):
    """Kill a process by PID."""
    try:
        p = psutil.Process(pid)
        p.terminate()
        return True
    except Exception:
        return False
