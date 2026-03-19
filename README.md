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

##  OUTPUT
https://private-user-images.githubusercontent.com/268330820/566062839-414f0db9-f98f-4eda-829d-8779e080355f.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzM5MDA0OTAsIm5iZiI6MTc3MzkwMDE5MCwicGF0aCI6Ii8yNjgzMzA4MjAvNTY2MDYyODM5LTQxNGYwZGI5LWY5OGYtNGVkYS04MjlkLTg3NzllMDgwMzU1Zi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwMzE5JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDMxOVQwNjAzMTBaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1mZTg3ODRlOTUwZGM3Y2E1NzdmZjczYTY4ZGMzNmM4NmY0Y2MxZTE3MzFhZjIwM2M4N2RkMzhlYjkxYTZlYzg0JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.Z6UFCB13ZTKTFPdi9aTAUrjTwguA-bfZ-U0OcxKQhrE
##  Usage
To run the toolkit, open your terminal in the project folder and use the following command:
```bash
python main.py
