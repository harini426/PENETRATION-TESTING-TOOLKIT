# Penetration Testing Toolkit

##  Description
This toolkit is a modular Python-based security tool designed for basic penetration testing tasks. It helps in identifying open ports, testing credential strength, and gathering service information from targets.

##  Modules
1. **Port Scanner**: Scans a target IP for open communication channels (TCP ports).
2. **Brute Forcer**: Simulates a credential-guessing attack against a specific username and target.
3. **Banner Grabber**: Retrieves the service banner (version info) from a specific port on a target.

##  Technical Stack
* **Language:** Python 3.x
* **Core Libraries:** `socket` (Network connectivity), `sys` (System parameters).
* **Environment:** Compatible with Windows, Linux, and macOS.

##  How It Works
* **Port Scanner:** Uses the TCP three-way handshake principle. The `socket` library attempts a connection; if successful (return code 0), the port is flagged as **OPEN**.
* **Brute Forcer:** Iterates through a predefined list of passwords against a specific username to simulate a credential-guessing attack.
* **Banner Grabber:** Establishes a connection to a port and reads the initial data packet sent by the server to determine the service name and version.

##  Usage
To run the toolkit, open your terminal in the project folder and use the following command:
```bash
python main.py