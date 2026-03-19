import socket

def scan_ports(target, ports):
    print(f"\n[!] Scanning target: {target}")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"[*] Port {port}: OPEN")
        else:
            print(f"[-] Port {port}: CLOSED")
        sock.close()