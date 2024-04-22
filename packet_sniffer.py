from scapy.all import *

def packet_sniffer(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto

        print(f"[*] IP Packet: {src_ip} -> {dst_ip}, Protocol: {protocol}")

    if packet.haslayer(TCP):
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport
        flags = packet[TCP].flags

        print(f"    [+] TCP Packet: {src_port} -> {dst_port}, Flags: {flags}")

    if packet.haslayer(UDP):
        src_port = packet[UDP].sport
        dst_port = packet[UDP].dport

        print(f"    [+] UDP Packet: {src_port} -> {dst_port}")

if __name__ == "__main__":
    print("[*] Starting packet sniffer... Press Ctrl+C to stop.")
    sniff(filter="ip", prn=packet_sniffer, store=0)
