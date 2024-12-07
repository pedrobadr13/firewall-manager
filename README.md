# Firewall Manager: IPTables Control & Traffic Management Tool

A Python-based tool for managing firewall rules and network traffic using **IPTables**. This script allows you to block/allow ports, enable/disable ICMP (ping), and control IP traffic (TCP, UDP, SSH) on Linux systems.

## Features:
- List current firewall rules and active network ports.
- Block/allow specific ports to secure the network.
- Enable/disable ICMP (ping) traffic for network visibility control.
- Block/allow IP traffic for TCP, UDP, or SSH protocols.
- Execute custom commands for advanced firewall configurations.

## Prerequisites:

- **Python 3**: The script is written in Python 3, so make sure it's installed.
- **IPTables**: This tool relies on IPTables for managing firewall rules. It is typically pre-installed on most Linux distributions.

## Installation:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/firewall-manager.git
    cd firewall-manager
    ```

2. **Install dependencies:**

    - Ensure you have Python 3 and IPTables installed.
    - On most Linux systems, IPTables is already available by default.

    If you don't have Python 3 installed, install it using your package manager:

    ```bash
    sudo apt update
    sudo apt install python3
    ```

3. **Run the script:**

    You need to run the script with superuser privileges (`sudo`) to modify firewall settings.

    ```bash
    sudo python3 firewall_manager.py
    ```

    The script will present a menu with options to manage firewall rules and network traffic.

## Usage:

Once the script is running, you will see a menu with several options. You can choose to:

- List current firewall rules.
- Block/allow specific ports or IPs.
- Enable/disable ICMP traffic (ping).
- Execute custom commands.

## Important Notes:

- **Superuser Access**: Since the script modifies firewall rules and system configurations, you need to run it as a superuser (`sudo`).
- **Backup**: The script automatically creates a backup of your **/etc/sysctl.conf** when modifying ICMP settings.
- **Network Impact**: Be cautious when blocking ports or IP addresses, as it may affect your network connectivity.

## License:

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

For any issues or improvements, feel free to open an issue or submit a pull request.

