# coding: utf-8

import shutil
import subprocess
from exceptions inport *

__author__ = 'vanzhiganov'


class Dnsmasq(object):
    def __init__(self, dnsmasq_conf='/etc/lxc/dnsmasq.conf'):
        """

        :param dnsmasq_conf:
        :return:
        """
        self.dnsmasq_conf = dnsmasq_conf
        self.list = self.__read_conf()

    # @staticmethod
    def exists_name(self, name):
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

    def __write_conf(self):
        """

        :return:
        """
        f = open("/tmp/dnsmasq.conf", 'w')
        f.writelines(self.list)
        f.close()
        shutil.copyfile("/tmp/dnsmasq.conf", "/etc/lxc/dnsmasq.conf")
        return None
