import psutil

# List of suspicious process names (commonly associated with worms)
suspicious_processes = [
    'worm.exe',    # Example process name
    'malicious.exe',  # Example process name
    # Add more suspicious process names as needed
]

# List of suspicious ports (commonly used by worms)
suspicious_ports = [
    4444,   # Example port number
    135,    # Example port number
    # Add more suspicious ports as needed
]

def detect_suspicious_processes():
    """Detect suspicious processes running on the system."""
    suspicious_found = False
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            process_name = proc.info['name']
            if process_name in suspicious_processes:
                print(f"Suspicious process detected: {process_name} (PID: {proc.info['pid']})")
                suspicious_found = True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    
    if not suspicious_found:
        print("No suspicious processes detected.")

def detect_suspicious_network_activity():
    """Detect suspicious network activity."""
    suspicious_found = False
    for conn in psutil.net_connections():
        if conn.laddr.port in suspicious_ports:
            print(f"Suspicious network activity detected: Local Address: {conn.laddr}, Remote Address: {conn.raddr}")
            suspicious_found = True
    
    if not suspicious_found:
        print("No suspicious network activity detected.")

def main():
    print("Starting worm detection...")
    
    # Detect suspicious processes
    detect_suspicious_processes()
    
    # Detect suspicious network activity
    detect_suspicious_network_activity()

if __name__ == "__main__":
    main()
