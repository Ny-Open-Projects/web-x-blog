---
title: "[Q5682] 可写事件水平触发：EPOLLOUT 不摘除导致 CPU 空转"
date: 2026-11-23
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5682 · 可写事件水平触发：EPOLLOUT 不摘除导致 CPU 空转

难度：P7 ｜ 标签：epoll、水平触发、EPOLLOUT、部分写、背压

**问**：一个自研网关用 epoll 管连接，压测时 CPU 100% 但 QPS 上不去，`strace` 里全是 `epoll_wait` 立即返回 + 少量 `write`。为什么"可写"会一直就绪？EPOLLOUT 什么时候该注册、什么时候必须注销？既然 epoll 说可写，为什么 `send` 还会 `EAGAIN`？

**答**：
结论：epoll 默认是**水平触发**（LT）：只要条件成立就一直通知。发送缓冲区没满 → 可写条件成立 → 每轮 `epoll_wait` 立刻返回；应用每次只写一小部分就回事件循环，下一轮又被立刻唤醒，形成"事件驱动空转"。正确姿势：只有在"有积压且写不动"时才注册 EPOLLOUT，积压写完立刻 `modify` 去掉（或临时注册、写完删）；读侧同理，必须读到 EAGAIN 或按帧消费，不能读一点就返回。

取舍：LT + 每次写一点，代码简单、不怕漏事件，但必须自己收敛关注集；ET（EPOLLET）事件更少、要求"一次读到 EAGAIN / 写到 EAGAIN"，漏读会永久丢事件，实现难度高。asyncio 走的是 LT + transport 层缓冲队列 + 按需注册可写，这也是为什么它不容易空转但需要 `drain()` 做背压。可写只保证"能写至少 1 字节"，不代表能一次写完你手里的大 buffer——TCP 还有拥塞窗口，应用层看不到。

实战：事故形态是"连接空闲时 CPU 也高"，因为注册了 EPOLLOUT 从不摘除；或"大响应发一半就卡"，因为忽略了部分写。下面用 `selectors`（macOS 上是 kqueue，语义与 epoll 一致）演示：数据留在缓冲区时 5 次 poll 全部立即就绪、逐字节读走同一份数据触发同阶事件数、写侧十几轮 poll→send 一次都不阻塞、写满后不再就绪、摘掉写关注后彻底安静。

```python
import selectors
import socket
import time

a, b = socket.socketpair()
a.setblocking(False)
sel = selectors.DefaultSelector()
print("后端:", type(sel).__name__)

# 1) 可读事件的水平触发：不读走就一直通知
sel.register(b, selectors.EVENT_READ)
a.send(b"hello")
hits = 0
for _ in range(5):
    if sel.select(0):
        hits += 1
print("[1] 数据一直在缓冲区里，5 次 select(0) 立即返回的次数:", hits)

# 2) 每次只读 1 字节：事件次数和字节数同阶，这就是"通知放大"
n = 0
while sel.select(0) and n < 100:
    b.recv(1)
    n += 1
print("[2] 逐字节读走同一份数据触发的事件数:", n, "| 读完后:", sel.select(0.05) == [])
sel.unregister(b)

# 3) 可写事件：缓冲区没满就一直就绪，每轮都要尝试写
sel.register(a, selectors.EVENT_WRITE)
cycles = 0
sent = 0
t0 = time.perf_counter()
while sel.select(0):
    cycles += 1
    try:
        sent += a.send(b"x" * 512)
    except BlockingIOError:
        break
elapsed = time.perf_counter() - t0
print(f"[3] 写了 {sent} 字节，用了 {cycles} 轮 poll->send，耗时 {elapsed * 1000:.2f} ms（没有一次真正阻塞）")
print("[4] 缓冲区写满后不再就绪:", sel.select(0.05) == [])

# 4) 摘掉写关注，避免"没数据可写却被反复唤醒"
sel.modify(a, selectors.EVENT_READ)
print("[5] 摘掉写关注后 a 不再就绪:", sel.select(0.05) == [])

sel.close()
a.close()
b.close()
```

**追问一**：为什么"可写"还会 `EAGAIN`？—— 可写是内核检查那一刻的结论（还有空闲空间），你在用户态组织数据、真正 `send` 时空间可能已被别的写者占掉，或者剩余空间小于你要写的量而 socket 又被设成非阻塞。所以必须把 `BlockingIOError` 当正常分支处理：把未写的部分留在应用缓冲里，等下一次可写事件再续。

**追问二**：怎么量化"写放大"，怎么优化？—— 事件次数 ≈ 数据量 / 单次成功写入量。本例 socketpair 缓冲约 8KB、每次 512B，十几轮就填满，每轮一次 `epoll_wait` + 一次 `write`；把单次写提升到 64KB 能把轮数压到常数级。但单次写太大会增加单连接占用时间、影响其他连接的公平性，常见的折中是 16-64KB 并配合 `sendmsg`/`writev` 合并小包。

## 背诵要点
- 水平触发 = 条件成立就一直通知；EPOLLOUT 不摘除会让空闲连接持续唤醒事件循环（CPU 空转）。
- 可写只保证"能写一点"：大响应必须处理部分写与 `EAGAIN`，未写部分留在应用缓冲。
- 关注集要收敛：有积压才注册写、写完立即摘；读侧读到 EAGAIN 或按帧消费。

## 复盘追问
- 网关 CPU 打满、QPS 不涨，strace 全是 epoll_wait 立即返回，如何定位并修复？（EPOLLOUT 未摘、部分写）
- 如何量化并降低写放大？大 buffer 一次写完有什么副作用？（事件数≈数据/单次写入量、公平性）
