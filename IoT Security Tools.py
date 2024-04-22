from scapy.all import *

def scan_iot_devices(network_prefix):
    """Scan for IoT devices in a network."""
    try:
        devices = []
        for i in range(1, 255):  # Replace with appropriate range
            ip = f"{network_prefix}.{i}"
            response = sr1(IP(dst=ip)/ICMP(), timeout=1, verbose=0)
            if response:
                if response.haslayer(TCP) or response.haslayer(UDP):
                    devices.append(ip)
                    print(f"Found IoT device at {ip}")
        return devices
    except Exception as e:
        print(f"Error scanning IoT devices: {e}")

if __name__ == "__main__":
    network_prefix = "192.168.1"  # Replace with your network prefix
    iot_devices = scan_iot_devices(network_prefix)
    print(f"Detected IoT devices: {iot_devices}")
