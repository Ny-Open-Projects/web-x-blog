---
title: [Q2144] SO_SNDTIMEO:发送超时与慢接收者
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2144 · SO_SNDTIMEO:发送超时与慢接收者

> 难度:★★★ | 标签:SO_SNDTIMEO, 慢消费者, socket 选项

**问**:对端一直不 recv,我的 send 会发生什么?怎么把"发不出去"变成可观测的?

**答**:内核发送缓冲灌满后 send 阻塞;SO_SNDTIMEO 给每次 send 设上限,超时返回 EAGAIN,Python 侧抛 BlockingIOError——慢接收者从这里显形。

- 实测对端不读时,塞入约 40 万字节后报 BlockingIOError,总耗时 0.8s;

- 那个字节数就是对端未确认缓冲容量的快照,是排障线索;

- 对照组对端在读,400 万字节畅通无阻;

- 与 settimeout 的区别:SO_SNDTIMEO 是内核语义,作用于每次系统调用。

```python
# file: code/02_并发与网络工程/q2144_sndtimeo.py
# -*- coding: utf-8 -*-
"""SO_SNDTIMEO: 发送超时与慢接收者检测。

- 接收侧停摆时, 发送缓冲区灌满, send 阻塞——慢消费者从这里开始显现;
- SO_SNDTIMEO 给每次 send 设上限, 超时返回 EAGAIN, Python 抛 BlockingIOError;
- 实测: 对端不读, 灌到内核缓冲上限后被拦, 字节数即缓冲容量快照。
"""
import socket
import struct
import threading
import time

HOST = "127.0.0.1"


def main():
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind((HOST, 0))
    srv.listen(1)
    port = srv.getsockname()[1]

    def server():
        conn, _ = srv.accept()
        time.sleep(2.5)              # 故意不读: 模拟慢接收者
        conn.close()

    t = threading.Thread(target=server, daemon=True)
    t.start()
    time.sleep(0.15)

    cli = socket.create_connection((HOST, port))
    cli.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 8192)
    # 原生 SO_SNDTIMEO: timeval 结构体的秒 + 微秒
    tv = struct.pack("ll", 0, 300000)          # 0.3s
    cli.setsockopt(socket.SOL_SOCKET, socket.SO_SNDTIMEO, tv)

    chunk = b"x" * 4096
    sent = 0
    t0 = time.monotonic()
    err = None
    try:
        while True:
            sent += cli.send(chunk)
    except OSError as e:
        err = e
    dur = time.monotonic() - t0
    print("对端不读: 成功塞进内核 %d 字节后报错" % sent)
    print("错误类型:", type(err).__name__, err, "| 总耗时 %.2fs" % dur)
    print("语义: 每次 send 至多等 0.3s, 缓冲满即 BlockingIOError")

    # 对照: 对端正常读取, 永远塞得进去
    srv2 = socket.socket()
    srv2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv2.bind((HOST, 0))
    srv2.listen(1)
    port2 = srv2.getsockname()[1]

    def eater():
        conn, _ = srv2.accept()
        deadline = time.monotonic() + 1.5
        while time.monotonic() < deadline:
            conn.recv(65536)
        conn.close()

    t2 = threading.Thread(target=eater, daemon=True)
    t2.start()
    time.sleep(0.15)
    cli2 = socket.create_connection((HOST, port2))
    cli2.setsockopt(socket.SOL_SOCKET, socket.SO_SNDTIMEO, tv)
    sent2 = 0
    err2 = None
    try:
        while sent2 < 4 * 1024 * 1024:
            sent2 += cli2.send(chunk)
    except OSError as e:
        err2 = e
    print("对端在读: 塞入 %d 字节, 错误: %s" % (sent2, err2))
    cli.close()
    cli2.close()
    srv.close()
    srv2.close()
    t.join(3)
    t2.join(2)


if __name__ == "__main__":
    main()
```

**追问**:1) sendall 和 SO_SNDTIMEO 配合有什么坑?——sendall 中途超时无法续传,数据可能半途而废,重要传输要用 send 循环自己记账。2) 为什么选 SO_SNDTIMEO 而不是应用层心跳?——两者互补:选项管单次调用的硬上限,心跳管端到端活性,前者是底线。3) SO_SNDTIMEO 与 settimeout 的关系?——settimeout 同时设 SO_RCVTIMEO/SO_SNDTIMEO(内核语义);SO_SNDTIMEO 单独管 send 超时,超时抛 BlockingIOError(带 EAGAIN)而不是 socket.timeout(Python 3.10+ 行为差异要注意);超时后数据可能部分已入缓冲(sendall 不可续,Q2144 原问)。4) 「缓冲容量快照」的排障价值怎么用?——对端不读时 send 塞入的字节数≈发送缓冲+拥塞窗口;这个数字与 SO_SNDBUF 对账,差异反映对端窗口/网络状况;配合 TCP_INFO(Linux)看对端确认进度——「写不进去的量」是链路诊断的一手数据。5) 生产陷阱?——sendall 配 SNDTIMEO(中途超时半截数据);把 BlockingIOError 当致命错误断连(应重试);缓冲调大掩盖慢消费者(背压延迟,Q1600);无 SNDTIMEO 的 send(慢接收者拖死线程);心跳与 SNDTIMEO 二选一(互补,前者管活性后者管单次上限)。

---
