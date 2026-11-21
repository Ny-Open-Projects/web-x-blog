---
title: [Q361] 用 socket 写一个最小 TCP 服务端与客户端
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q361 · 用 socket 写一个最小 TCP 服务端与客户端

> 难度:★★☆ | 标签:网络编程, socket, TCP

**问**:请用标准库 socket 手写一个最小的 TCP echo 服务端和客户端,并说明每一步系统调用的含义。

**答**:服务端流程是 `socket → bind → listen → accept`,客户端是 `socket → connect`。`bind` 绑定地址端口,`listen` 把套接字转为被动监听( backlog 是半连接/全连接队列长度),`accept` 阻塞直到有连接到来返回新的 conn 套接字,后续读写都在 conn 上进行。收发的是 bytes,记得 `sendall` 保证发完、`recv(bufsize)` 指定单次上限。

```python
# file: code/02_并发与网络工程/q361_tcp_echo.py
"""最小 TCP echo 服务端 + 客户端,单进程可自测。"""
import socket
import threading


def start_server(host="127.0.0.1", port=0):
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 快速重启
    srv.bind((host, port))
    srv.listen(5)  # backlog:等待 accept 的连接队列长度
    srv.settimeout(2)
    return srv


def handle_client(conn):
    with conn:
        while True:
            data = conn.recv(1024)  # 返回 bytes,空表示对端关闭
            if not data:
                break
            conn.sendall(data)  # 循环发送直到全部写完


def main():
    srv = start_server()
    port = srv.getsockname()[1]
    threading.Thread(target=accept_loop, args=(srv,), daemon=True).start()

    # 客户端
    cli = socket.create_connection(("127.0.0.1", port), timeout=2)
    cli.sendall(b"hello")
    print("echo:", cli.recv(1024))
    cli.close()
    srv.close()


def accept_loop(srv):
    while True:
        try:
            conn, addr = srv.accept()
        except socket.timeout:
            continue
        threading.Thread(target=handle_client, args=(conn,), daemon=True).start()


if __name__ == "__main__":
    main()
```

**追问**:
- `send` 和 `sendall` 的区别?`send` 可能部分发送(受内核发送缓冲区限制),`sendall` 内部循环直到全部发送完成,业务代码应优先用它。
- 为什么服务端要 `SO_REUSEADDR`?避免 TIME_WAIT 状态下端口无法立即重绑,重启服务时常用。
