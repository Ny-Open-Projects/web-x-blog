---
title: [Q5626] socket close 与 shutdown 的语义差异原理
date: 2026-11-21
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5626 · socket close 与 shutdown 的语义差异原理

> 难度:★★★★☆ | 标签:原理深挖, socket, TCP 终止

**问**:优雅断开一个 TCP 连接，`shutdown(SHUT_WR)` 和 `close()` 差在哪？"对端还有数据没读完就 close"为什么会发 RST？SO_LINGER 的两个参数组合各是什么行为？

**答**:结论：`close()` 是**引用计数式的资源释放**——fd 引用归零才真正终止连接（半关闭语义由引用决定），而 `shutdown()` 是**直接对连接下操作**，不问引用：`SHUT_WR` 发 FIN 进入"我不再写、但我还能读对方数据"的半关闭，这是文件上传/协议应答的标准收尾（客户端发完数据 → shutdown(WR) → 一直 read 到 EOF → 再 close）。危险场景：**对端缓冲里还有数据时本端 close**，内核默认直接发 RST——对端"未读数据"被丢弃且读到 "connection reset" 而不是 EOF，日志里大量 `ConnectionResetError` 的常见来源就是这里。SO_LINGER 三种组合：`on=0`（close 立即 RST，强杀，防 TIME_WAIT）、`on=1,timeout>0`（close 阻塞到数据发完或超时，超时 RST）、默认 `off`（close 立即返回，内核后台尽力发完——"尽力"没有保证）。实战顺序：应用层确认收尾 → `shutdown(SHUT_WR)` → 读到 EOF → `close()`；服务端反向同理。这也是 Q5552/SIGTERM 排空与 Q6074 停机窗口的底层细节。

```python
import socket, struct

# ---- 1) 半关闭演示：shutdown(WR) 后仍可收对方数据，收到 EOF ----
a, b = socket.socketpair()          # 全双工管道，行为与 TCP 半关闭同构
a.shutdown(socket.SHUT_WR)          # a 声明"不再写"
try:
    a.sendall(b"x")
except OSError as e:
    print("shutdown(WR) 后再写:", type(e).__name__, "-", e.strerror)
b.sendall(b"still alive")           # b 仍可写给 a
print("a 仍能读对端:", a.recv(64))
print("b 读到 EOF:", b.recv(64))     # FIN -> 空 bytes 即 EOF
a.close(); b.close()

# ---- 2) 对端已关闭后的行为（RST/BrokenPipe 家族） ----
a, b = socket.socketpair()
a.close()                            # a 直接关闭，无 shutdown 收尾
try:
    b.sendall(b"write to dead peer") # 第一次写可能成功（进了内核缓冲）
    b.sendall(b"second write")       # 内核回 RST 后再写 -> BrokenPipeError
except OSError as e:
    print("对端已死再写:", type(e).__name__, "-", e.strerror)
try:
    b.recv(64)                       # 收到 RST -> ConnectionResetError
except OSError as e:
    print("对端已死再读:", type(e).__name__)
b.close()

# ---- 3) SO_LINGER 三种组合 ----
def linger(fd, onoff, sec):
    fd.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, struct.pack("ii", onoff, sec))

a, b = socket.socketpair()
linger(a, 1, 5)                      # on=1, timeout=5s: close 阻塞至数据发完或超时
print("SO_LINGER (1,5):", struct.unpack("ii", a.getsockopt(socket.SOL_SOCKET, socket.SO_LINGER, 8)))
a.close(); b.close()

a, b = socket.socketpair()
linger(a, 0, 0)                      # on=0: 立即 RST，跳过 TIME_WAIT（强杀，慎用）
print("SO_LINGER (0,0): RST 模式 —— 丢弃未发数据并立即释放，对端收到 reset")
a.close(); b.close()
print("默认(不设): close 立即返回，内核后台尽力发完 —— '尽力'无保证，靠 SO_SNDBUF/对端窗口")

# ---- 4) 优雅断开模板 ----
print("模板: 发完 -> shutdown(SHUT_WR) -> recv 到 EOF -> close()；对端则 read 到 EOF 后反向 shutdown")
```

**追问一层**:为什么"close 时本端接收缓冲里有未读数据"也会 RST？（内核认为应用不关心这些数据，直接 RST 快速回收；所以服务端断开前要把请求读干净，否则客户端收到 reset 而非正常 FIN）。
**追问二层**:`shutdown(SHUT_RD)` 有什么坑？（本端后续读永远 EOF，且部分平台会把未读数据丢弃并确认掉——对端继续写会填满缓冲触发其写阻塞，用在"忽略请求体"场景要配合丢弃读循环）。
**追问三层**:长连接网关的连接回收，close 与 shutdown 怎么编排？（先 shutdown(WR) 给对端收尾窗口 → 超时未 EOF 再 close；配合应用层 goaway 帧，避免 RST 打爆对端重连）。

## 背诵要点
- close = 引用计数资源释放；shutdown = 直接操作连接，SHUT_WR 发 FIN 实现半关闭（发完数据仍可收）。
- 未读未发数据遇 close 默认可能 RST：对端收到 reset 而非 EOF，是 ConnectionResetError 高发根因。
- SO_LINGER：(0,0) 立即 RST、(1,t) 阻塞到发完或超时、默认后台尽力发；优雅断开 = shutdown(WR)→read EOF→close。

## 复盘追问
- 客户端上报里一半 ConnectionResetError，如何区分"服务端未读完就 close"与"LB 超时强断"两类根因？
- 设计文件上传服务的断开协议：什么时候 shutdown(WR)、什么时候直接 close，给出状态机。
