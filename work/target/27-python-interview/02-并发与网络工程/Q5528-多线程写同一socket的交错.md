---
title: [Q5528] 多线程写同一个 socket：交错与写序列化
date: 2026-11-20
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5528 · 多线程写同一个 socket：交错与写序列化

> 难度:★★★★ | 标签:socket, 线程安全, 写交错

**问**：两个线程同时对同一个 socket `sendall` 会发生什么？"单次 send 是原子的"这句话哪里对哪里错？正确的写序列化方案是什么，SSL 连接为什么更严重？

**答**：`send/sendall` 在**单次系统调用层面**对小缓冲（≤ `PIPE_BUF` 语义对管道成立，socket 无此保证）通常原子，但 `sendall` 的语义是"循环 send 直到发完"——**大块数据会被内核切成多次 send**，两次 send 之间另一线程可以插队，接收方读到的就是交错字节流：协议帧互相嵌进对方的载荷里，表现为"偶发的解析错误、且无法复现"。所以"原子"只在单次 send 小块时近似成立，`sendall(大块)` 完全不保证。修复：1) **每连接写锁**：`with conn.lock: conn.sendall(frame)`——临界区只包 send，构造数据放锁外（Q2653 两段式）；2) **单写线程**：所有帧入队列由专属 writer 串行发出（半同步半异步），锁竞争为零；3) asyncio 下事件循环单线程天然串行，`transport.write` 在循环线程调用安全，但**跨线程**必须 `call_soon_threadsafe` 投递（Q600）。SSL 更严重：SSLObject/SSL socket 的握手状态机与记录层加密**不可重入**，并发 send 不仅交错还可能打乱 TLS 记录序列直接协议崩溃。

```python
# file: code/02_并发与网络工程/q5528_concurrent_write.py
import socket, threading

a, b = socket.socketpair()
N, CHUNK = 500, 10                     # 两个线程各发 50 个 10 字节小块

def sender(tag):
    for _ in range(N // CHUNK):
        a.sendall(tag * CHUNK)         # 无锁并发写同一 socket

t1 = threading.Thread(target=sender, args=(b"A",))
t2 = threading.Thread(target=sender, args=(b"B",))
t1.start(); t2.start()

got = b""
while len(got) < 2 * N:
    got += b.recv(4096)
t1.join(); t2.join(); a.close()

runs = 1 + sum(1 for i in range(1, len(got)) if got[i] != got[i - 1])
print("收到字节数:", len(got), "(应=1000)")
print("连续段数:", runs, "-> >2 即发生交错(顺序不定,本机复跑数值会变)")

# 正解: 每连接写锁,临界区只包 send
class LockedWriter:
    def __init__(self, sock):
        self.sock = sock
        self.lock = threading.Lock()
    def send_frame(self, frame: bytes):
        with self.lock:                # 构造在锁外,send 在锁内(Q2653 两段式)
            self.sock.sendall(frame)

w = LockedWriter(b)
print("写序列化后: 帧边界由锁保证,接收方按帧解析不再嵌花")
```

**追问**：1) 为什么小块 send "通常"不交错还要上锁？——"通常"依赖内核实现与缓冲状态（缓冲满时 sendall 内部循环、信号中断重试），把正确性押在实现细节上是事故源头；锁的纳秒级成本远低于交错故障的排查成本。2) `SO_SNDBUF` 满时的 sendall 行为与交错的关系？——缓冲满时 send 阻塞/重试，yield 窗口更大，交错概率剧增——高负载下才爆发正是该类事故"偶发"的原因（Q2144）。3) asyncio 混线程场景的正确姿势？——所有 `transport.write` 经 `loop.call_soon_threadsafe` 投递到循环线程，或干脆包一层队列写线程，禁止跨线程直接写。

## 背诵要点
1. sendall 大块会被切多次 send，两线程并发写必然可能交错；"单次小 send 原子"不是正确性依据。
2. 修复三式：每连接写锁（两段式临界区）、单写线程队列、asyncio 投递回循环线程。
3. SSL 连接并发写 = 记录层不可重入，比明文 socket 更致命，必须序列化。

## 复盘追问
1. "偶发解析错误且抓包正常"这类事故，怎么在不动协议的前提下快速止血？（提示：先上每连接写锁热修，再抓多线程 send 的调用栈采样确认交错源，最后按协议帧加序号自检（Q1875））
2. 写锁会不会成为吞吐瓶颈？怎么既序列化又高吞吐？（提示：单写线程 + 批量 coalesce（writev 合帧），把锁竞争换成立即返回的入队操作，参考 Q2655 写合并）
