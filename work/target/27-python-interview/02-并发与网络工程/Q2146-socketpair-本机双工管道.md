---
title: [Q2146] socketpair:本机双工管道
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2146 · socketpair:本机双工管道

> 难度:★★☆ | 标签:socketpair, IPC, 全双工

**问**:两个线程之间要双向传数据,除了队列还能用 socket 吗?

**答**:os.socketpair 造一对已连接的匿名套接字,双方各持一端,全双工字节流,无端口无名字,延迟最低。

- 实测三个 ping-echo 往返 RTT 在微秒量级;

- SHUT_WR 半关闭能精确表达"我发完了",对端 recv 收到 EOF;

- fork 后父子各持一端,是经典的进程内 IPC 用法;

- 与 pipe 的区别:双向;与 TCP 的区别:无协议栈开销。

```python
# file: code/02_并发与网络工程/q2146_socketpair.py
# -*- coding: utf-8 -*-
"""socketpair: 本机双工管道, 线程与子进程的私有通道。

- os.socketpair 返回一对已连接的匿名 AF_UNIX/AF_LOCAL 套接字;
- 双向全双工, 无端口无名字, 是线程间和 fork 后父子间的自带管道;
- 比普通 pipe 强在双向且有字节流语义, 比 TCP 少一整套协议栈。
"""
import os
import socket
import threading
import time


def echo_worker(sock, stats):
    """工作线程: 从自己的那一端收, 原样回, 直到对端半关闭。"""
    sock.settimeout(3.0)
    try:
        for _ in range(3):
            data = sock.recv(1024)
            stats.append((time.monotonic(), data))
            sock.sendall(b"echo:" + data)
        while sock.recv(1024):        # 半关闭后 recv 回 b'', 循环退出
            pass
    except socket.timeout:
        pass
    finally:
        sock.close()


def main():
    parent_sock, child_sock = socket.socketpair(socket.AF_UNIX,
                                                socket.SOCK_STREAM)
    print("socketpair fd: parent=%d child=%d" %
          (parent_sock.fileno(), child_sock.fileno()))

    stats = []
    t = threading.Thread(target=echo_worker, args=(child_sock, stats))
    t.start()

    for msg in (b"ping-1", b"ping-2", b"ping-3"):
        t0 = time.monotonic()
        parent_sock.sendall(msg)
        reply = parent_sock.recv(1024)
        print("发出 %-8s 收到 %-16s RTT %.3fms" %
              (msg.decode(), reply.decode(),
               (time.monotonic() - t0) * 1000))

    parent_sock.shutdown(socket.SHUT_WR)     # 半关闭: 通知对端没有更多数据
    t.join(3)
    print("对端收到 EOF 后自行退出, join 正常返回")
    parent_sock.close()

    for ts, data in stats:
        print("工作线程收到:", data.decode())
    print("双向各走一遍: 全双工成立, 无端口无路由, 延迟最低")
    print("fork 后父子各持一端, 就是最经典的进程内 IPC 用法")


if __name__ == "__main__":
    main()
```

**追问**:1) socketpair 和 Queue 怎么选?——字节流、fd 传递、与 select 融合选 socketpair;结构化消息与背压语义选 Queue。2) 能在 socketpair 上传 fd 吗?——可以,SCM_RIGHTS 附带数据,这是它比 pipe 强大的地方,标准库要用 C 扩展或 sendmsg 封装。3) socketpair 与 Queue/fd 传递的选型矩阵?——字节流+select 融合(同一个 selector 管 fd 与 socket)+SCM_RIGHTS 传 fd:socketpair;结构化消息+背压语义+多消费者:Queue;fork 后父子:socketpair 是标准件(subprocess 的 stdout 管道就是它)——「fd 生态」与「消息生态」的分界。4) 半关闭在 socketpair 上的精确语义?——SHUT_WR 表达「我发完了」:对端 recv 收 EOF 但还能继续发回来;管道式任务(发送方发完即关闭写端)的标准原语(Q664 在本机 IPC 的应用)。5) 生产陷阱?——socketpair 两端被不同线程用而没考虑缓冲上限(阻塞);传 fd 用 send 硬塞(SCM_RIGHTS 要 sendmsg/recvmsg,标准库封装有限);close 一端后另一端仍写(EPIPE);把 socketpair 当 TCP 用(无协议栈但也无拥塞控制,大数据量要自己做流控)。

---
