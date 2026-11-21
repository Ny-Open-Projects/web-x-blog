---
title: [Q626] SOCKS5 代理协议:握手与请求格式
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q626 · SOCKS5 代理协议:握手与请求格式

> 难度:★★★★ | 标签:SOCKS5, 代理, 二进制协议

**问**:SOCKS5 比 HTTP 代理强在哪?握手报文长什么样?

**答**:SOCKS5 是传输层级的代理协议:不解析 HTTP,支持 TCP 与 UDP ASSOCIATE,支持多种认证方法协商。握手两步:客户端发 `05 nmethods methods`(05 是版本,带支持的方法列表),服务端选一个回 `05 method`(00=无认证,02=用户密码);认证后发请求 `05 CMD 00 ATYP addr port`,CMD=01 是 CONNECT,ATYP 区分 IPv4/域名/IPv6,服务端回 `05 00 00 ATYP bndaddr bndport` 表示成功,之后同样是盲转发。相比 HTTP CONNECT,它协议更轻、天然支持 UDP 与域名解析代理端。

```python
# file: code/02_并发与网络工程/q626_socks5.py
import socket
import struct
import threading
import time


def pump(a: socket.socket, b: socket.socket) -> None:
    try:
        while True:
            data = a.recv(65536)
            if not data:
                break
            b.sendall(data)
    except OSError:
        pass
    finally:
        for s in (a, b):
            try:
                s.shutdown(socket.SHUT_RDWR)
            except OSError:
                pass


def socks5_server(stop: threading.Event, port_box: list) -> None:
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    srv.listen(8)
    port_box.append(srv.getsockname()[1])
    srv.settimeout(0.2)
    while not stop.is_set():
        try:
            c, _ = srv.accept()
        except socket.timeout:
            continue
        threading.Thread(target=handle, args=(c,), daemon=True).start()
    srv.close()


def recv_n(sock: socket.socket, n: int) -> bytes:
    buf = b""
    while len(buf) < n:
        chunk = sock.recv(n - len(buf))
        if not chunk:
            raise ConnectionError("closed")
        buf += chunk
    return buf


def handle(c: socket.socket) -> None:
    try:
        c.settimeout(2)
        ver, nmethods = recv_n(c, 2)
        methods = recv_n(c, nmethods)
        assert ver == 5 and 0 in methods, "不支持的版本或无可用认证方法"
        c.sendall(b"\x05\x00")  # 选择无认证
        req = recv_n(c, 4)      # VER CMD RSV ATYP
        _ver, cmd, _rsv, atyp = req
        if atyp == 1:           # IPv4
            addr = socket.inet_ntoa(recv_n(c, 4))
        elif atyp == 3:         # 域名
            ln = recv_n(c, 1)[0]
            addr = recv_n(c, ln).decode()
        else:
            raise ValueError("仅演示 IPv4 与域名")
        (port,) = struct.unpack("!H", recv_n(c, 2))
        print(f"[socks5] CONNECT {addr}:{port} cmd={cmd}")
        remote = socket.create_connection((addr, port), timeout=2)
        c.sendall(b"\x05\x00\x00\x01" + socket.inet_aton("0.0.0.0") + struct.pack("!H", 0))
        t = threading.Thread(target=pump, args=(c, remote), daemon=True)
        t.start()
        pump(remote, c)
        t.join(timeout=1)
    except Exception as e:
        print(f"[socks5] 失败: {e!r}")
        try:
            c.sendall(b"\x05\x01\x00\x01" + b"\x00" * 6)
        except OSError:
            pass
    finally:
        c.close()


def echo_target(stop: threading.Event, port_box: list) -> None:
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    srv.listen(4)
    port_box.append(srv.getsockname()[1])
    srv.settimeout(0.2)
    while not stop.is_set():
        try:
            conn, _ = srv.accept()
        except socket.timeout:
            continue
        try:
            data = conn.recv(1024)
            conn.sendall(b"target:" + data)
        except OSError:
            pass
        conn.close()
    srv.close()


if __name__ == "__main__":
    stop = threading.Event()
    px: list = []
    tg: list = []
    threading.Thread(target=socks5_server, args=(stop, px), daemon=True).start()
    threading.Thread(target=echo_target, args=(stop, tg), daemon=True).start()
    while not (px and tg):
        time.sleep(0.01)

    c = socket.create_connection(("127.0.0.1", px[0]))
    c.sendall(b"\x05\x01\x00")            # 版本5, 1个方法, 无认证
    c.sendall(b"\x05\x01\x00\x01" + socket.inet_aton("127.0.0.1") + struct.pack("!H", tg[0]))
    c.settimeout(2)
    print("方法协商响应:", c.recv(2).hex())
    reply = c.recv(10)
    print("连接响应:", reply.hex(), "(05 00 表示成功)")
    c.sendall(b"via-socks5")
    print("隧道内数据:", c.recv(64).decode())
    c.close()
    stop.set()
```

**追问**:1) 为什么 curl 的 socks5h 和 socks5 选项结果不同?——socks5h 把域名解析也交给代理端做(远程解析,避免 DNS 泄漏/污染),socks5 在本地解析后只传 IP。2) 方法协商为什么设计成「客户端列清单、服务端选一个」?——版本演进兼容:老客户端只带 NO-AUTH,新服务端可选要求认证,不支持就回 0xFF 让客户端放弃;扩展不破坏老实现,这是二进制协议设计的通用范式。3) ATYP 三种地址类型怎么用?——IPv4/IPv6 直接地址;域名类型(0x03)把解析交给代理端(等价 socks5h 的语义,内网域名解析不出局),域名最长 255 字节因为长度字段是单字节。4) 生产陷阱?——握手没读完就当隧道用,残留字节污染第一条请求;UDP ASSOCIATE 回包的 BND.ADDR 写 0.0.0.0 客户端连错;无 TLS 的 SOCKS5 密码字段明文传输;版本字节写错(0x04)变成 SOCKS4 协议错乱。

---
