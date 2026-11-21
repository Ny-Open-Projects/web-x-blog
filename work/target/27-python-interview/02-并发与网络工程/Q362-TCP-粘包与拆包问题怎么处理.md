---
title: [Q362] TCP 粘包与拆包问题怎么处理
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q362 · TCP 粘包与拆包问题怎么处理

> 难度:★★★ | 标签:网络编程, TCP, 协议设计

**问**:什么是 TCP 粘包?为什么 UDP 没有"粘包"?如何设计协议解决?

**答**:TCP 是字节流协议,没有消息边界,多次 `send` 的数据可能被合并一次 `recv` 读出(粘包),也可能一条消息被分多次读出(拆包)。UDP 保留报文边界所以不存在此问题。解决思路本质是"应用层自定义边界":①定长消息;②分隔符(如 `\n`,需转义);③长度前缀——头部用固定字节声明 body 长度,是最通用方案。

```python
# file: code/02_并发与网络工程/q362_sticky_pack.py
"""长度前缀协议:4 字节大端长度 + body,解决 TCP 粘包。"""
import socket
import struct
import threading

HEADER = struct.Struct("!I")  # 网络字节序(大端)uint32


def send_msg(sock, payload: bytes):
    sock.sendall(HEADER.pack(len(payload)) + payload)


def recv_exact(sock, n: int) -> bytes:
    """循环读满 n 字节,连接关闭则抛异常。"""
    buf = bytearray()
    while len(buf) < n:
        chunk = sock.recv(n - len(buf))
        if not chunk:
            raise ConnectionError("peer closed")
        buf.extend(chunk)
    return bytes(buf)


def recv_msg(sock) -> bytes:
    (length,) = HEADER.unpack(recv_exact(sock, 4))
    if length > 10 * 1024 * 1024:  # 防恶意超大包
        raise ValueError("payload too large")
    return recv_exact(sock, length)


def main():
    srv = socket.socket()
    srv.bind(("127.0.0.1", 0))
    srv.listen(1)
    port = srv.getsockname()[1]
    threading.Thread(target=_serve, args=(srv,), daemon=True).start()

    cli = socket.create_connection(("127.0.0.1", port))
    # 连发三条模拟粘包,服务端按帧逐条还原
    for i in range(3):
        send_msg(cli, f"msg-{i}".encode())
    cli.close()
    srv.close()


def _serve(srv):
    conn, _ = srv.accept()
    with conn:
        for _ in range(3):
            print("recv frame:", recv_msg(conn))


if __name__ == "__main__":
    main()
```

**追问**:
- 换行分隔协议有什么坑?body 中若含分隔符会截断错误,需要转义或限定 body 为不含分隔符的文本(如 Redis 协议的组合方案)。
- `recv(1024)` 返回不足 1024 字节是错误吗?不是,TCP 只保证有序可靠,不保证一次读满,必须循环读。
