#!/usr/bin/env python3
import os
import subprocess

# Function to list current firewall rules
def list_iptables():
    print("\nCurrent Firewall Rules:")
    os.system("sudo iptables -L -v -n")

# Function to list running ports
def list_running_ports():
    print("\nRunning Ports:")
    os.system("sudo ss -tuln")  # Or you can use 'netstat -tuln' if ss is not available

# Function to block a specific port
def block_port(port):
    print(f"\nBlocking port {port}...")
    os.system(f"sudo iptables -A INPUT -p tcp --dport {port} -j DROP")

# Function to enable ICMP (ping) traffic
def enable_icmp():
    print("\nEnabling ICMP (ping) traffic...")
    os.system("sudo iptables -A INPUT -p icmp --icmp-type echo-request -j ACCEPT")

# Function to disable ICMP (ping) traffic
def disable_icmp():
    print("\nDisabling ICMP (ping) traffic...")
    os.system("sudo iptables -A INPUT -p icmp --icmp-type echo-request -j REJECT")

# Function to block IP on TCP, UDP, SSH
def block_ip_on_protocol(ip, protocol):
    print(f"\nBlocking {protocol} traffic for IP: {ip}")
    if protocol.lower() == "tcp":
        os.system(f"sudo iptables -A INPUT -s {ip} -p tcp -j DROP")
    elif protocol.lower() == "udp":
        os.system(f"sudo iptables -A INPUT -s {ip} -p udp -j DROP")
    elif protocol.lower() == "ssh":
        os.system(f"sudo iptables -A INPUT -s {ip} -p tcp --dport 22 -j DROP")
    else:
        print("Invalid protocol specified.")

# Function to allow IP on TCP, UDP, SSH
def allow_ip_on_protocol(ip, protocol):
    print(f"\nAllowing {protocol} traffic for IP: {ip}")
    if protocol.lower() == "tcp":
        os.system(f"sudo iptables -A INPUT -s {ip} -p tcp -j ACCEPT")
    elif protocol.lower() == "udp":
        os.system(f"sudo iptables -A INPUT -s {ip} -p udp -j ACCEPT")
    elif protocol.lower() == "ssh":
        os.system(f"sudo iptables -A INPUT -s {ip} -p tcp --dport 22 -j ACCEPT")
    else:
        print("Invalid protocol specified.")

# Function to allow a specific port
def allow_port(port):
    print(f"\nAllowing port {port}...")
    os.system(f"sudo iptables -A INPUT -p tcp --dport {port} -j ACCEPT")

# Function to execute any command provided by the user
def execute_command():
    command = input("\nEnter the command to execute: ")
    os.system(command)

def set_icmp_status(allow: bool):
    """
    Enable or disable ICMP ping requests by modifying sysctl configuration.
    :param allow: True to allow ICMP, False to block ICMP.
    """
    value = '0' if allow else '1'
    config_line = f"net.ipv4.icmp_echo_ignore_all = {value}"
    
    sysctl_file = '/etc/sysctl.conf'
    backup_file = sysctl_file + '.backup'
    if not os.path.exists(backup_file):
        print(f"Creating a backup of {sysctl_file} at {backup_file}")
        subprocess.run(['cp', sysctl_file, backup_file], check=True)
    
    updated = False
    with open(sysctl_file, 'r') as file:
        lines = file.readlines()
    
    with open(sysctl_file, 'w') as file:
        for line in lines:
            if line.startswith("net.ipv4.icmp_echo_ignore_all"):
                file.write(config_line + "\n")
                updated = True
            else:
                file.write(line)
        
        if not updated:
            file.write(config_line + "\n")
    
    print(f"ICMP status updated in {sysctl_file}: {'Allowed' if allow else 'Blocked'}")
    
    subprocess.run(['sysctl', '-p'], check=True)

# Main Menu function
def menu():
    while True:
        print("/\\___________.__                              .__  .__/\ ")
        print(")/\\_   _____/|__|______   ______  _  _______  |  | |  )/ ")
        print("   |    __)  |  \\_  __ \\_/ __ \\ \\/ \\/ /\\__  \\ |  | |  |  ")
        print("   |     \\   |  ||  | \\/\\  ___/\\     /  / __ \\|  |_|  |__")
        print("   \\___  /   |__||__|    \\___  >\\/\\_/  (____  /____/____/")
        print("       \\/                    \\/             \\/           ")
        print("/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\ ")
        print(")/)/)/)/)/)/)/)/)/)/)/)/)/)/)/)/)/)/)/)/)/)/)/)/)/)/)/)/ ")

        print("\nFirewall Control Menu")
        print("1. List current firewall rules")
        print("2. List running ports")
        print("3. Block a specific port")
        print("4. Enable ICMP (ping)")
        print("5. Disable ICMP (ping)")
        print("6. Block IP on TCP, UDP, or SSH")
        print("7. Allow IP on TCP, UDP, or SSH")
        print("8. Allow a specific port")
        print("9. Execute a custom command")
        print("22. Allow ICMP (enable ping)")
        print("23. Block ICMP (disable ping)")
        print("10. Exit")

        choice = input("Choose an option (1-10): ")

        if choice == "1":
            list_iptables()
        elif choice == "2":
            list_running_ports()
        elif choice == "3":
            port = input("Enter the port number to block: ")
            block_port(port)
        elif choice == "4":
            enable_icmp()
        elif choice == "5":
            disable_icmp()
        elif choice == "6":
            ip = input("Enter the IP address to block: ")
            protocol = input("Enter the protocol to block (tcp/udp/ssh): ").strip().lower()
            block_ip_on_protocol(ip, protocol)
        elif choice == "7":
            ip = input("Enter the IP address to allow: ")
            protocol = input("Enter the protocol to allow (tcp/udp/ssh): ").strip().lower()
            allow_ip_on_protocol(ip, protocol)
        elif choice == "8":
            port = input("Enter the port number to allow: ")
            allow_port(port)
        elif choice == "9":
            execute_command()
        elif choice == '22':
            set_icmp_status(True)
        elif choice == '23':
            set_icmp_status(False)
        elif choice == "10":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point of the program
if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting gracefully...")

