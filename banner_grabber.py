import socket

def grab_banner(target, port):
    try:
        sock = socket.socket()
        sock.settimeout(2)
        sock.connect((target, port))
        banner = sock.recv(1024).decode().strip()
        print(f"\n[+] Service Banner: {banner}")
        sock.close()
    except:
        print("\n[-] Could not retrieve banner.")