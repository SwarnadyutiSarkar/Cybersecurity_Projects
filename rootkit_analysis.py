import psutil

def detect_hidden_processes():
    """Detect hidden processes that may indicate a rootkit."""
    try:
        # Get list of all running processes
        all_processes = psutil.process_iter(['pid', 'name'])

        # Get list of hidden processes
        hidden_processes = []
        for process in all_processes:
            if process.info['name'] == '' or process.info['pid'] == 0:
                hidden_processes.append(process.info['pid'])

        if hidden_processes:
            print(f"Hidden processes detected: {hidden_processes}")
        else:
            print("No hidden processes detected.")
    except Exception as e:
        print(f"Error detecting hidden processes: {e}")

if __name__ == "__main__":
    detect_hidden_processes()
