import os
import subprocess
import sys

def start_packet_capture(interface):
    try:
        subprocess.Popen(["tcpdump", "-i", interface, "-w", "captured_packets.pcap"])
    except Exception as e:
        print(f"Error starting packet capture: {e}")
        sys.exit(1)

def stop_packet_capture():
    try:
        subprocess.Popen(["killall", "tcpdump"])
    except Exception as e:
        print(f"Error stopping packet capture: {e}")
        sys.exit(1)

def analyze_packets():
    try:
        os.system("suricata -r captured_packets.pcap")
    except Exception as e:
        print(f"Error analyzing packets with Suricata: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python advanced_ids.py <interface> <duration>")
        sys.exit(1)

    interface = sys.argv[1]
    duration = int(sys.argv[2])

    print(f"Starting packet capture on interface {interface}...")
    start_packet_capture(interface)

    print(f"Capturing packets for {duration} seconds...")
    try:
        import time
        time.sleep(duration)
    except KeyboardInterrupt:
        pass

    print("Stopping packet capture...")
    stop_packet_capture()

    print("Analyzing captured packets...")
    analyze_packets()

    print("IDS analysis completed.")
