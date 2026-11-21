---
title: [Q653] selectors 模块:自动选择最佳后端
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q653 · selectors 模块:自动选择最佳后端

> 难度:★★☆ | 标签:selectors, DefaultSelector, 适配层

**问**:标准库 selectors 是怎么做到"同一份代码跑遍三大平台"的?

**答**:selectors 按平台能力自动挑后端:Linux 用 EpollSelector,macOS/BSD 用 KqueueSelector,Windows 用 DevpollSelector/SelectSelector,统一暴露 register/unregister/select(timeout 秒级)+ Key(fileobj, data, events) 抽象。data 字段让你把"这个连接的状态对象"直接挂在注册项上,回传时随身携带——这就是迷你事件循环(Q579)的原材料。注意 select timeout 单位是秒(浮点),返回的 events 是 (Key, 事件掩码) 列表;文件对象 close 后必须 unregister,否则 fd 复用会导致幽灵事件。

```python
# file: code/02_并发与网络工程/q653_selectors_mux.py
import selectors
import socket
import threading
import time


def echo_server(stop: threading.Event, port_box: list) -> None:
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    srv.listen(8)
    port_box.append(srv.getsockname()[1])
    srv.settimeout(0.2)
    sel = selectors.DefaultSelector()
    sel.register(srv, selectors.EVENT_READ, data="listener")
    conns = {}
    while not stop.is_set():
        for key, events in sel.select(timeout=0.2):
            if key.data == "listener":
                conn, addr = key.fileobj.accept()
                conn.setblocking(False)
                conns[conn.fileno()] = conn
                sel.register(conn, selectors.EVENT_READ, data="client")
                print(f"[mux] 新连接 fd={conn.fileno()}, 后端={type(sel).__name__}")
            else:
                conn = key.fileobj
                try:
                    data = conn.recv(1024)
                    if not data:
                        raise ConnectionError
                    conn.sendall(b"mux-echo:" + data)
                except (ConnectionError, OSError):
                    sel.unregister(conn)
                    conns.pop(conn.fileno(), None)
                    conn.close()
                    print("[mux] 连接关闭并注销")
    for c in conns.values():
        c.close()
    srv.close()


if __name__ == "__main__":
    stop = threading.Event()
    box: list = []
    t = threading.Thread(target=echo_server, args=(stop, box), daemon=True)
    t.start()
    while not box:
        time.sleep(0.01)

    clients = [socket.create_connection(("127.0.0.1", box[0]), timeout=2) for _ in range(3)]
    for i, c in enumerate(clients):
        c.sendall(f"msg-{i}".encode())
        c.settimeout(1)
        print(f"client{i} 收到:", c.recv(64).decode())
    for c in clients:
        c.close()
    time.sleep(0.3)
    stop.set()
    print("单个线程 + 单个多路复用器服务了 3 个客户端连接")
```

**追问**:1) 为什么 close 前要 unregister?——fd 会被系统复用,旧注册项还挂在 selector 里时,新连接拿到同一 fd 会收到张冠李戴的就绪事件,这是手写事件循环最阴的 bug。2) data 字段怎么用?——register(fileobj, events, data) 把连接状态对象(缓冲、状态机、地址)挂在注册项,就绪返回的 Key.data 直接带走,免自己维护 fd→对象映射——迷你事件循环(Q579)的脚手架。3) close 后忘 unregister 为什么是幽灵事件?——fd 被内核复用,新连接拿到同一编号,旧注册还挂在 selector 里,新连接的读写事件被派给旧对象的处理逻辑——张冠李戴且不报错,是手写事件循环最阴的 bug;惯例 finally: selector.unregister(conn)。4) 生产陷阱?——DefaultSelector 平台差异(开发 macOS 生产 Linux)被当 bug 追;重复 unregister 抛 KeyError;每轮遍历 selector.get_map() 清理的 O(n) 开销;register 的 data 里放了不可 pickle/循环引用的大对象。

---
