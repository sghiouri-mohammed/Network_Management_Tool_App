from netmiko import ConnectHandler
import getpass
import logging
import datetime


def ssh_connect(ip, username, password):
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

        # Exit configuration mode if in
        if connection.check_config_mode():
            connection.exit_config_mode()

        # Close the connection
        connection.disconnect()

        return "SSH connection successful"

    except Exception as e:
        logging.error(f"Connection or command execution error: {e}")
        print(f"\033[91mConnection or command execution error: {e}\033[0m")
