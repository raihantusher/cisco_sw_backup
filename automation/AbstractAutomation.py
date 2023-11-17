# Python program showing
# abstract base class work
from abc import ABC, abstractmethod


class AbstractAutomation(ABC):
    @abstractmethod
    def start_backup(self, hostname, host_ip, username, password, port, log_file):
        pass
