import os
import tempfile
import shutil
from .exceptions import *


class Dnsmasq:
    def __init__(self, dnsmasq_conf='/etc/dnsmasq.conf'):
        """

        :param dnsmasq_conf:
        :return:
        """
        self.lease_time = '12h'
        self.dnsmasq_conf = dnsmasq_conf
        self.list = self.__read_conf()

    # @staticmethod
    def exists_name(self, name) -> bool:
        """

        :param name:
        :return:
        """
        # origin = self.__read_conf()
        for i in self.list:
            if name in i:
                return True
        return False

    # @staticmethod
    def exists_ip(self, ip):
        """

        :param ip:
        :return:
        """
        # origin = self.__read_conf()
        for i in self.list:
            if ip in i:
                return True
        return False

    def add(self, name, ip):
        """

        :param name:
        :param ip:
        :return:
        """
        if self.exists_name(name):
            raise NameAlreadyExists("Already exists: %s" % name)
        if self.exists_ip(ip):
            raise IPAlreadyExists("Already exists: %s" % ip)
        self.list.append("dhcp-host=%s,%s" % (name, ip))
        self.__write_conf()
        return None

    def delete(self, name):
        clean = []
        for i in self.__read_conf():
            if name not in i:
                clean.append(i)
        self.__write_conf()
        return True

    def __read_conf(self):
        """

        :return:
        """
        origin = []
        for i in open(self.dnsmasq_conf, "r"):
            origin.append(i.rstrip())
        return origin

    def __write_conf(self) -> bool:
        """

        :return:
        """
        fd, path = tempfile.mkstemp(suffix='.txt', text=True)
        with open(path, 'w') as fpw:
            fpw.writelines(self.list)
        os.close(fd)

        shutil.copyfile(path, self.dnsmasq_conf)

        os.unlink(path)

        return True
