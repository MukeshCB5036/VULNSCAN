# VULNSCAN

VULNSCAN is a simple vulnerability scanner designed to scan IP addresses and ports for potential vulnerabilities. The tool allows you to scan a target IP and its ports, and it generates a report of the findings.

## Features

- Scans a specified IP address for open ports in a given range.
- Displays the status of each port (open/closed).
- Generates a detailed report of the scan results.
- Customizable for different scan targets and port ranges.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/MukeshCB5036/VULNSCAN.git
Install the required dependencies:
pip install -r requirements.txt

Usage
To run the vulnerability scan, execute the following command in the project directory:
python main.py
The script will prompt you to enter a target IP and a range of ports to scan.
After the scan is complete, you will be presented with the option to save the scan results to a file.

Example
[+] Scanning 192.168.1.1 ports 22-80 ...
Host: 192.168.1.1 (Router)
Protocol: tcp
Port: 22   State: open
Port: 80   State: open

Report Generation
After the scan is completed, you can choose to save the results to a .md file, which includes the scan details and findings.
Contributing
Feel free to open issues and submit pull requests. All contributions are welcome!

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes.
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature-branch).
Create a new pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Nmap for port scanning.
Pyfiglet for ASCII banners.
