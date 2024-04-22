from scapy.all import *

def wifi_security_analysis():
    print("[*] Scanning nearby Wi-Fi networks...")

    # Sniff Wi-Fi packets for 10 seconds
    packets = sniff(timeout=10, iface="wlan0mon", prn=lambda x: x.summary())

    print("\n[*] Analyzing security features...\n")

    for packet in packets:
        if packet.haslayer(Dot11):
            # Extract SSID and BSSID
            ssid = packet[Dot11].info.decode()
            bssid = packet[Dot11].addr3

            # Check encryption type
            if packet[Dot11].type == 0 and packet[Dot11].subtype == 8:
                encryption = "WEP"
            elif packet[Dot11].type == 0 and packet[Dot11].subtype == 4:
                encryption = "WPA"
            elif packet[Dot11].type == 0 and packet[Dot11].subtype == 5:
                encryption = "WPA2"
            else:
                encryption = "Unknown"

            print(f"SSID: {ssid}, BSSID: {bssid}, Encryption: {encryption}")

if __name__ == "__main__":
    wifi_security_analysis()

from scapy.all import *

def wifi_security_analysis():
    print("[*] Scanning nearby Wi-Fi networks...")

    # Set the interface to monitor mode
    interface = "wlan0mon"  # Replace with your monitor mode interface
    os.system(f"sudo ifconfig {interface} down")
    os.system(f"sudo iwconfig {interface} mode monitor")
    os.system(f"sudo ifconfig {interface} up")

    # Sniff Wi-Fi packets for 10 seconds
    packets = sniff(timeout=10, iface=interface, prn=lambda x: x.summary())

    print("\n[*] Analyzing security features...\n")

    for packet in packets:
        if packet.haslayer(Dot11):
            # Extract SSID and BSSID
            ssid = packet[Dot11].info.decode()
            bssid = packet[Dot11].addr3

            # Check encryption type
            if packet[Dot11].type == 0 and packet[Dot11].subtype == 8:
                encryption = "WEP"
            elif packet[Dot11].type == 0 and packet[Dot11].subtype == 4:
                encryption = "WPA"
            elif packet[Dot11].type == 0 and packet[Dot11].subtype == 5:
                encryption = "WPA2"
            else:
                encryption = "Unknown"

            print(f"SSID: {ssid}, BSSID: {bssid}, Encryption: {encryption}")

    # Restore the interface to managed mode
    os.system(f"sudo ifconfig {interface} down")
    os.system(f"sudo iwconfig {interface} mode managed")
    os.system(f"sudo ifconfig {interface} up")

if __name__ == "__main__":
    wifi_security_analysis()
