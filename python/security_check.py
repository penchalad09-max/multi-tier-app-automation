import socket

def check_ports(host="localhost", ports=[8081, 5000, 3306]):
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"✅ Port {port} is open.")
        else:
            print(f"⚠️ Port {port} is closed.")
        sock.close()

if __name__ == "__main__":
    check_ports()
