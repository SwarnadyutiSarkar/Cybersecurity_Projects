from scapy.all import *

def monitor_ics_traffic(interface):
    """Monitor ICS traffic on a specific network interface."""
    try:
        sniff(iface=interface, prn=process_packet, store=0)
    except Exception as e:
        print(f"Error monitoring ICS traffic: {e}")

def process_packet(packet):
    """Process and analyze ICS packets."""
    try:
        if packet.haslayer(IP) and packet.haslayer(TCP):
            src_ip = packet[IP].src
            dst_ip = packet[IP].dst
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            payload = packet[TCP].payload
            
            # Perform anomaly detection and security analysis (simplified example)
            if "modbus" in payload.lower():
                print(f"Potential Modbus traffic detected from {src_ip}:{src_port} to {dst_ip}:{dst_port}")
                # Implement additional security checks and analysis here
            elif "dnp3" in payload.lower():
                print(f"Potential DNP3 traffic detected from {src_ip}:{src_port} to {dst_ip}:{dst_port}")
                # Implement additional security checks and analysis here
            else:
                print(f"Unknown ICS traffic detected from {src_ip}:{src_port} to {dst_ip}:{dst_port}")
                # Implement additional security checks and analysis here
    except Exception as e:
        print(f"Error processing packet: {e}")

if __name__ == "__main__":
    interface = "eth0"  # Replace with the network interface to monitor
    monitor_ics_traffic(interface)
