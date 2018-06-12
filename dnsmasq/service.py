import subprocess


class Service(object):
    def restart(self):
        subprocess.call("service dnsmasq restart", shell=True)
        return True

    def pid(self):
        return None
