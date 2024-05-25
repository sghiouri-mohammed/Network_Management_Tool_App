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


if __name__ == "__main__":

    # Initialize logging
    today = datetime.date.today()
    logging.basicConfig(filename=f'logs/{today}.log', level=logging.DEBUG)
    logger = logging.getLogger("netmiko")

    # ANSI color codes
    cred = '\033[91m'
    cgrn = '\033[92m'
    cend = '\033[0m'

    # Prompt the user for login credentials
    ip = '192.168.1.2'
    username = 'admin'
    password = 'admin'

    # Execute SSH connection
    result = ssh_connect(ip, username, password)

    if result:
        print(f"{cgrn}{result}{cend}")

        # Log connection success
        with open(f'{today}.log', 'a') as logFile:
            logFile.write(f'{datetime.datetime.now()} : {username} connected to {ip}\n')

    else:
        print(f"{cred}No output received from the device or an error occurred.{cend}")

