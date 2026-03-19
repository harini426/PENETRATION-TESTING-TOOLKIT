# Penetration Testing Toolkit

**COMPANY**: CODTECH IT SOLUTIONS
**NAME**: S. HARINI
**INTERN ID**: CTIS6595
**DOMAIN**: CYBER SECURITY & ETHICAL HACKING
**DURATION**: 4 WEEKS
**MENTOR**: NEELA SANTHOSH

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

##OUTPUT

<img width="1920" height="1020" alt="Image" src="https://github.com/user-attachments/assets/414f0db9-f98f-4eda-829d-8779e080355f" />


<img width="1920" height="1020" alt="Image" src="https://github.com/user-attachments/assets/e55b53a7-3eb4-43b0-9eed-86370246b3f4" />


<img width="1920" height="1020" alt="Image" src="https://github.com/user-attachments/assets/3f3a7343-061d-466b-b542-988126a45750" />
