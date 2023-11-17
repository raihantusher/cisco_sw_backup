import paramiko
import datetime
import time

from . import AbstractAutomation

time_now = datetime.datetime.now().strftime('%d_%b_%Y_%H_%M_%S')


class CiscoBusinessSwitch():

    def start_backup(self, hostname, host_ip, username, password, port, log_file):
        # Create an SSH client
        ssh = paramiko.SSHClient()

        # Automatically add the server's host key (this is insecure and should be avoided in production)
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        hostname = hostname + "-" + time_now

        try:
            # Connect to the device
            ssh.connect(hostname=host_ip, username=username, password=password, port=port, timeout=5)

            # Create an SSH shell
            remote_shell = ssh.invoke_shell()

            # Wait for the shell to be ready
            while not remote_shell.recv_ready():
                time.sleep(1)

            # Send the command to the device
            # remote_shell.send("terminal length 0\n")
            #
            time.sleep(2)

            cmd_str = "copy running-config tftp://192.168.1.150/" + hostname + "\n"
            remote_shell.send(cmd_str)
            time.sleep(5)  # Adjust this sleep time based on the device response time
            '''

            cmd_str = "copy running-config tftp://\n"
            remote_shell.send(cmd_str)
            time.sleep(2)


            cmd_str = host_ip+'\n'
            remote_shell.send(cmd_str)
            time.sleep(2)


            cmd_str = hostname+'\n'
            remote_shell.send(cmd_str)
            time.sleep(2)
            '''

            # Receive the command output
            output = remote_shell.recv(65535).decode("utf-8")

            # Save the output to a file
            with open(log_file, 'w') as f:
                f.write(output)

            print(f"Backup successful. Output saved to {log_file}")

        except paramiko.AuthenticationException:
            print("Authentication failed. Please verify your credentials.")
        except paramiko.SSHException as e:
            print(f"Unable to establish SSH connection: {str(e)}")
        finally:
            # Close the SSH connection
            ssh.close()


class CiscoCatalyst():

    def start_backup(self, hostname, host_ip, username, password, port, log_file):
        print("hello")
