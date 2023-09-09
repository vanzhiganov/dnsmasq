import subprocess
from .exceptions import ConfigSyntaxException


class Service:
    def restart(self) -> bool:
        if self.test():
            subprocess.call("systemctl restart dnsmasq", shell=True)
            return True
        return False

    @staticmethod
    def test():
        test = subprocess.run(["dnsmasq", "--test"], capture_output=True, text=True)
        if test.stderr.strip() == "dnsmasq: syntax check OK.":
            return True
        raise ConfigSyntaxException(test.stderr.strip())
