from datetime import datetime
import os

def generate_report(results):
    # Create reports directory if it doesn't exist
    if not os.path.exists('reports'):
        os.makedirs('reports')
    # Get the current date and time
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d_%H%M%S")
    fname = f'reports/scan_report_{current_time}.md'
    
    # Write the scan results to the file
    with open(fname, 'w') as md:
        md.write("# Scan Results\n")
        md.write(f"Scan completed at {current_time}\n\n")
        md.write(results)
    
    print(f"[+] Report generated: {fname}")

