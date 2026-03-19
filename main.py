import socket

# Vera file-la irunthu import panna error vantha, logic-ai ingaiyae direct-ah vechukkalam
def scan_ports(target, ports):
    print(f"\n[!] Scanning target: {target}")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"[*] Port {port}: OPEN")
        else:
            print(f"[-] Port {port}: CLOSED")
        sock.close()

def brute_force(target_url, username, passwords):
    print(f"\n[!] Starting Brute Force on: {target_url}")
    for password in passwords:
        print(f"[-] Trying: {password}...")
    print("[+] Brute force simulation complete.")

def menu():
    print("\n" + "="*40)
    print("   PENETRATION TESTING TOOLKIT   ")
    print("="*40)
    print("1. Port Scanner")
    print("2. Brute Force")
    print("3. Exit")

while True:
    menu()
    choice = input("\nEnter choice: ")

    if choice == "1":
        target = input("Enter target IP: ")
        ports = [21, 22, 80, 443]
        scan_ports(target, ports)
    
    elif choice == "2":
        url = input("Enter target URL: ")
        user = input("Enter username: ")
        passwords = ["123456", "admin", "password"]
        brute_force(url, user, passwords)
        
    elif choice == "3":
        print("Exiting...")
        break