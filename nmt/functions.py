from netmiko import ConnectHandler
import getpass
import logging
import datetime


def ssh_connect(ip, username, password, interface):
    try:
        # Define connection parameters
        cisco_device = {
            'device_type': 'cisco_ios',
            'host': ip,
            'username': username,
            'password': password,
        }

        # Establish SSH connection
        connection = ConnectHandler(**cisco_device)

        # Enter enable mode
        connection.enable()

        # Enter configuration mode
        connection.config_mode()

        # Execute the shutdown and no shutdown commands
        commands = [f"interface {interface}", "shutdown", "no shutdown", "end", "write memory"]
        output = connection.send_config_set(commands)

        # Exit configuration mode
        connection.exit_config_mode()

        # Close the connection
        connection.disconnect()

        return output

    except Exception as e:
        logging.error(f"Connection or command execution error: {e}")
        print(f"\033[91mConnection or command execution error: {e}\033[0m")