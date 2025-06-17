import socket

def scan_ports(host, ports):
    open_ports = []
    print(f"🔍 Scanning {host} for open ports...")
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(0.3)
                result = sock.connect_ex((host, port))
                if result == 0:
                    print(f"🟢 Port {port} is open")
                    open_ports.append(port)
        except Exception as e:
            print(f"⚠️ Error on port {port}: {e}")
    return open_ports