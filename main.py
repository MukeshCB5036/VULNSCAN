import nmap
import pyfiglet
from utils.parser import get_target_ip, get_port_range
from utils.report import generate_report

def scan_target(ip, port_range):
    scanner = nmap.PortScanner()
    args = f'-p {port_range}'
    
    print(f"[+] Scanning {ip} ports {port_range} ...")
    scanner.scan(hosts=ip, arguments=args)
    scan_results = f"Scan results for {ip}:\n"
    
    for host in scanner.all_hosts():
        scan_results += f"Host: {host} ({scanner[host].hostname()})\n"
        for proto in scanner[host].all_protocols():
            scan_results += f"Protocol: {proto}\n"
            lport = scanner[host][proto].keys()
            for port in lport:
                scan_results += f"Port: {port}\tState: {scanner[host][proto][port]['state']}\n"
    
    return scan_results

def main():
    ascii_banner = pyfiglet.figlet_format("VulnScan")
    print(ascii_banner)
    target_ip = get_target_ip()
    port_range = get_port_range()
    findings = scan_target(target_ip, port_range)
    
    # Display scan results on the screen
    print("\n[+] Scan Results:")
    print(findings)
    save_report = input("\nDo you want to save the results to a file? (y/n): ").lower()
    if save_report == 'y':
        generate_report(findings)
        print(f"\n[+] Report saved successfully.")
    else:
        print("\n[+] Report not saved.")

if __name__ == "__main__":
    main()

