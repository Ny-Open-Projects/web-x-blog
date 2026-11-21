---
title: [Q2408] 半包聚合的 read_exact
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2408 · 半包聚合的 read_exact

> 难度:★★★ | 标签:read_exact, 半包, recv

**问**:recv(1024) 为什么不能当“读一帧”用?

**答**:recv 的返回量只取决于内核此刻有什么,与协议帧边界无关;网络一慢,一帧被拆成几段先后到达,单次 recv 只能拿到前半截。

- 实测服务端把 11 字节帧分三段、段间 0.2s 发出,客户端立即 recv 只拿到第一段 3 字节;

- read_exact 的骨架:循环 recv 直到凑满 n 字节,对端先关闭则抛 ConnectionError 报告 EOF 位点;

- 实测剩余 8 字节跨两次 recv 凑齐,拼出完整帧 HELLO-WORLD;

- 所有定长帧、长度前缀帧的解析器,底层都是这个原语;它同时定义了 EOF 语义:凑不满且对端关闭就是协议级错误。

```python
# file: code/02_并发与网络工程/q2408_read_exact.py
# -*- coding: utf-8 -*-
"""半包聚合的 read_exact: recv 给多少算多少, 凑够 n 字节才算完。

- recv 的返回量只取决于内核此刻有什么, 与协议帧边界无关;
- 网络一慢, 一帧被拆成几段先后到达, 单次 recv 只能拿到前半截;
- read_exact 循环recv 直到凑满 n 字节或 EOF, 是所有定长帧解析的地基。
"""
import socket
import threading
import time


def recv_exact(sock, n):
    """凑满 n 字节才返回, 对端先关则抛 ConnectionError。"""
    buf = bytearray()
    while len(buf) < n:
        chunk = sock.recv(n - len(buf))
        if not chunk:
            raise ConnectionError("EOF at %d/%d bytes" % (len(buf), n))
        buf.extend(chunk)
    return bytes(buf)


def serve(port_ready, chunks):
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    srv.listen(1)
    port_ready.append(srv.getsockname()[1])
    conn, _ = srv.accept()
    for ch, gap in chunks:
        conn.sendall(ch)             # 一段一段发, 模拟网络分段到达
        time.sleep(gap)
    conn.shutdown(socket.SHUT_WR)
    conn.close()
    srv.close()


def main():
    port_ready = []
    # 一帧 11 字节, 分三段到达, 段间有 0.2s 的网络延迟
    threading.Thread(target=serve, daemon=True,
                     args=(port_ready, [(b"HEL", 0.2), (b"LO-WO", 0.2), (b"RLD", 0)])).start()
    deadline = time.monotonic() + 2.0
    while not port_ready and time.monotonic() < deadline:
        time.sleep(0.01)
    port = port_ready[0]

    sock = socket.create_connection(("127.0.0.1", port), timeout=3)
    time.sleep(0.05)                 # 客户端此刻只有第一段已经到达

    naive = sock.recv(1024)
    print("裸 recv 一次拿到: %r (%d 字节)" % (naive, len(naive)))
    assert len(naive) == 3, "半包场景下裸 recv 只能拿到已到达的第一段"

    sock.settimeout(3)
    rest = recv_exact(sock, 11 - len(naive))     # 只补剩下的部分
    frame = naive + rest
    print("read_exact 补齐: %r -> 完整帧 %r" % (rest, frame))
    assert frame == b"HELLO-WORLD", "read_exact 必须跨多次 recv 凑满整帧"

    try:
        recv_exact(sock, 5)          # 服务端已 shutdown, EOF 到来
        raise AssertionError("EOF 必须被识别")
    except ConnectionError as e:
        print("EOF 语义正确:", e)
    sock.close()


if __name__ == "__main__":
    main()
```

**追问**:1) read_exact 会不会永远阻塞?——调用前设 socket 超时,阻塞被 SO_RCVTIMEO 转成 timeout 异常,层与层之间的超时责任要交接清楚。2) UDP 需要它吗?——不需要,UDP 有报文边界,recv 一次至多拿一个报文,半包是 TCP 流式的专属烦恼。3) read_exact 的 EOF 语义与超时责任交接?——凑不满且对端关闭=协议级错误(报告 EOF 位点);调用前设 socket 超时,SO_RCVTIMEO 把阻塞转 timeout——「层与层的超时责任」:socket 层管单次调用,协议层管帧级 deadline(Q2417 预算),别混。4) 为什么 UDP 不需要 read_exact?——UDP 有报文边界,recv 一次至多一个报文(半包不存在),但会丢包/乱序(Q1867/Q1868)——「流式才有半包,数据报才有丢失」是两种传输模型的分工。5) 生产陷阱?——recv(n) 当「读一帧」(只拿到内核现有);read_exact 无超时(慢对端钉死);EOF 当异常处理(是正常关闭,Q2148 矩阵);剩余字节跨多次 recv 的拼接 bug(缓冲管理);把 read_exact 用在 UDP 上(语义不存在)。

---
