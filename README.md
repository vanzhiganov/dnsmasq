# dnsmasq

Python dnsmasq library

## how to use

```
import dnsmasq
dns = dnsmasq.Dnsmasq("/etc/dnsmasq.d/cloud.conf")
```

```
dns.exists_name('test')
dns.add('test', '10.10.10.10')
dns.delete('test')
```
