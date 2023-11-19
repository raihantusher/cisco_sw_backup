import configparser
import ping3
from automation.AutomationFactory import AutomationFactory


def is_host_reachable(host, timeout=1):
    """
    Check if a host is reachable using ICMP echo requests.

    :param host: The host to ping.
    :param timeout: Timeout for the ping request in seconds.
    :return: True if the host is reachable, False otherwise.
    """
    # pinger = ping3.Ping(timeout=timeout)

    try:
        response = ping3.ping(host, timeout=1)
        if response is not None:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False


config = configparser.ConfigParser()

config.read('cisco_host_config.ini')  # path of your .ini file
# print(config.sections())


for host in config.sections():
    hostname = host
    host_ip = config[host]['host_ip']
    username = config[host]['user']
    password = config[host]['password']
    port = config[host]['port']
    type = config[host]['type']

    # host_to_ping = "example.com"
    result = is_host_reachable(host_ip)

    # if result:
    #     automation = AutomationFactory.get_obj(type)
    #     automation.start_backup(hostname, host_ip, username, password, port, log_file="log.txt")
    # else:
    #     print(f"{hostname}-{host_ip} is not reachable.")

    automation = AutomationFactory.get_obj(type)
    automation.start_backup(hostname, host_ip, username, password, port, log_file="log.txt")
