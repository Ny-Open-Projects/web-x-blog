---
title: "[Q5688] 非阻塞 send 的部分写与 sendall 的半途失败"
date: 2026-11-23
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5688 · 非阻塞 send 的部分写与 sendall 的半途失败

难度：P6 ｜ 标签：socket、send、sendall、BlockingIOError、部分写、背压

**问**：非阻塞 socket 上 `send(b"x" * 65536)` 只返回 8192，剩下的 57KB 去哪了，是丢了吗？为什么 `sendall` 在非阻塞模式下也会抛 `BlockingIOError`，而且抛了之后根本不知道已经写进去多少？自己实现写循环要注意什么？

**答**：
结论：`send` 返回的是"这次真正拷进内核发送缓冲的字节数"，返回值小于 `len(data)` 叫**部分写**，剩下的没丢，但必须由应用自己重发（推进偏移）。内核只保证已写部分交给了协议栈，能不能送到对端是另一回事。`sendall` 在阻塞模式下内部循环直到写完；在非阻塞模式下遇到 `EAGAIN` 会抛 `BlockingIOError`，而**已经成功写入的字节数不会通过异常返回**，所以非阻塞 + sendall 是错误组合——正确做法是 `send` + 应用层待发缓冲（这就是 asyncio transport 干的事）。

取舍：阻塞 + sendall 最简单，但一个慢客户端就能卡住整个线程；非阻塞必须自己管"待发队列 + 可写事件"，事件来了写一点、写不动就留着等下次可写（Q5682 的注销逻辑）。折中是给 socket 设 `settimeout()`（本质是非阻塞 + 轮询），简单但仍会占用线程时间。

实战：事故形态是"自研 HTTP 客户端偶发响应截断，日志显示已发送 2MB 但服务端只收到 1.98MB"，根因就是拿到部分写返回值后直接当成功。另一个是"发送大响应时 CPU 高"，因为每轮只写 8KB 却不停轮询。下面实测：请求 64KB 只接受 8KB、非阻塞 sendall 半途抛错、阻塞模式配 drain 线程才能写完 1MB。

```python
import socket
import threading

a, b = socket.socketpair()
a.setblocking(False)

lens = []
total = 0
for _ in range(1000):
    try:
        n = a.send(b"x" * 65536)
    except BlockingIOError:
        break
    lens.append(n)
    total += n
print("[1] send 每次返回的字节数集合:", sorted(set(lens)), "| 累计:", total)

try:
    a.sendall(b"y" * 1_000_000)
except BlockingIOError as e:
    print("[2] 非阻塞 sendall 半途失败 ->", type(e).__name__, "| 已写多少字节不可知")

got = []


def drain():
    while sum(got) < 1_000_000:
        chunk = b.recv(65536)
        if not chunk:
            break
        got.append(len(chunk))


th = threading.Thread(target=drain)
th.start()
a.setblocking(True)
a.sendall(b"z" * 1_000_000)         # 阻塞模式内部循环直到写完
th.join(5)
print("[3] 阻塞模式 sendall 写完，对端累计收到:", sum(got), "字节（含前面残留的 8192）")

a.close()
b.close()
```

**追问一**：为什么只接受 8KB？—— 取三者最小：对端接收窗口、本机发送缓冲区剩余空间、TCP 拥塞窗口。socketpair 没有真实网络，瓶颈就是内核缓冲。真实 TCP 上还会因为接收端慢、RTT 大、拥塞控制把可用窗口压得更小，所以"部分写"是常态而不是异常。

**追问二**：部分写之后直接 `close()` 会怎样？—— 已经交给协议栈的字节会尝试发送（除非 `SO_LINGER` 置 0 触发 RST），没写进去的直接丢；表现为"响应截断但状态码正常"。所以关闭前必须把待发缓冲排空（asyncio 里就是 `await writer.drain()`），或者协商一个"发送完成"的应用层信号再关。

## 背诵要点
- `send` 返回实际写入字节数，小于请求长度 = 部分写，必须自己推进偏移重发，数据不丢。
- 非阻塞 `sendall` 会半途抛 `BlockingIOError` 且不告诉已写量 → 非阻塞永远用 send + 待发缓冲。
- 可写只代表"能写一点"，关闭前必须排空（drain），否则响应会被截断。

## 复盘追问
- 客户端偶发"响应截断但 200"，如何用部分写解释并修复？（返回值 < 长度、重发、drain）
- 为什么 `sendall` 在非阻塞下不可用？阻塞 sendall 的代价是什么？（已写量不可知、慢客户端占线程）
