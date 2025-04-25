def get_target_ip():
    # Ask the user for the target IP or CIDR range
    target_ip = input("Enter target IP or CIDR range (e.g. 192.168.1.0/24): ")
    return target_ip

def get_port_range():
    # Ask the user for the port range to scan
    port_range = input("Enter port range to scan (e.g. 20-80): ")
    return port_range

