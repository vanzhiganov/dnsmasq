# dnsmasq

Python dnsmasq library

## how to use

MAC-address generate.

```python
from dnsmasq import mac
mac.gen()
```

```python
from dnsmasq import dnsmasq

dns = dnsmasq.Dnsmasq("/etc/dnsmasq.d/cloud.conf")

dns.exists_name('52:54:00::6b:dc:1f')
dns.add('52:54:00::6b:dc:1f', '192.168.1.11')
dns.delete('52:54:00::6b:dc:1f')
```
