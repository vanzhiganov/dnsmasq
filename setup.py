from setuptools import setup
from dnsmasq import __version__

setup(
    name="dnsmasq",
    version=__version__,
    author="Vyacheslav Anzhiganov",
    author_email='vanzhiganov@ya.ru',
    packages=[
        "dnsmasq"
    ],
    install_requires=[
    ]
)
