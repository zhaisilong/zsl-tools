# Socket

Python 的socket模块提供了与 Berkeley 套接字 API 的接口。

`socket.SOCK_STREAM` 用于为 `TCP` 创建套接字，而`socket.SOCK_DGRAM` 为 `UDP` 创建套接字

创建套接字时，必须指定其地址族。 然后，我们只能在套接字中使用该类型的地址。

- AF_UNIX，AF_LOCAL-本地通讯
- AF_INET-IPv4 Internet 协议
- AF_INET6-IPv6 Internet 协议
- AF_IPX-IPX-Novell 协议
- AF_BLUETOOTH-无线蓝牙协议
- AF_PACKET-底层数据包接口

对于 `AF_INET` 地址族，指定了一对（主机，端口）。 `host` 是一个字符串，表示互联网域表示法中的主机名（如 `example.com`）或 IPv4 地址（如 `93.184.216.34` ），并且 port 是整数。

```python
import socket

# 获取 IP 地址
ip = socket.gethostbyname('example.com')
print(ip)

# UDP 套接字示例
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:

    message = b''
    addr = ("djxmmx.net", 17)

    s.sendto(message, addr)

    data, address = s.recvfrom(1024)
    print(data.decode())

# TCP 套接字示例
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    host = "time.nist.gov"
    port = 13

    s.connect((host, port))
    s.sendall(b'')
    print(str(s.recv(4096), 'utf-8'))
    
```

## See also

- [Python 套接字教程](https://geek-docs.com/python/python-tutorial/python-socket.html)

- [Python 网络编程](https://www.runoob.com/python/python-socket.html)