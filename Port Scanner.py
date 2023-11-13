import socket

# Function to scan a range of ports on a target host
def port_scan(target_host, start_port, end_port):
    try:
        # Resolve the target host to an IP address
        target_ip = socket.gethostbyname(target_host)

        # Iterate over the range of ports to scan
        for port in range(start_port, end_port + 1):
            # Create a socket object
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.settimeout(1)  # Set a timeout for socket connection

            # Attempt to connect to the target host and port
            result = client_socket.connect_ex((target_ip, port))

            # Check if the connection was successful (0 indicates success)
            if result == 0:
                print(f"Port {port} is open")

            # Close the socket
            client_socket.close()

    except socket.gaierror:
        print("Hostname could not be resolved.")
    except socket.error:
        print("Could not connect to the server.")

if __name__ == "__main__":
    target_host = input("Enter the target hostname or IP address: ")
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))

    print(f"Scanning ports {start_port}-{end_port} on {target_host}...\n")
    port_scan(target_host, start_port, end_port)
