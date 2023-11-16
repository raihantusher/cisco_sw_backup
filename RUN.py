import configparser
from cisco_backup import backup_cisco_device


config = configparser.ConfigParser()

config.read('cisco_host_config.ini') #path of your .ini file

#print(config.sections())


for host in config.sections():
    hostname = host
    host_ip  = config[host]['host_ip']
    username  = config[host]['user']
    password = config[host]['password']
    port     = config[host]['port']

    backup_cisco_device(hostname, host_ip, username, password, port, log_file="log.txt")


    