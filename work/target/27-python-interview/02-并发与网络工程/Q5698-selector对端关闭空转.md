---
title: "[Q5698] 对端关闭后 selector 持续可读：不注销就空转烧 CPU"
date: 2026-11-24
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5698 · 对端关闭后 selector 持续可读：不注销就空转烧 CPU

难度：P7 ｜ 标签：selectors、EPOLLHUP、空转、事件循环、连接回收

**问**：自研 selector 服务器里，客户端断开后某个 fd 一直"可读"，`select()` 立刻返回，但 `recv()` 拿到 `b""`，循环里既没数据可处理又不阻塞，一个核直接跑满。为什么关闭的连接会一直报可读？`recv()` 返回空串意味着什么？什么条件下必须 `unregister`？

**答**：
结论：对端关闭（FIN）或连接被重置（RST）后，内核把该 fd 标记为"可读"，因为 `read()` 会立即返回 0/错误，不会阻塞。更关键的是，在 epoll/kqueue 上，挂断状态（`EPOLLHUP`/`EV_EOF`）是**水平触发**的：只要 fd 还注册着且没被关闭，每次 `select()` 都会报告它可读。所以正确的收尾是：读到 `b""`（或捕获 `ConnectionResetError`）→ `unregister(fd)` → `close(fd)`；少任何一步，事件循环就会在这个 fd 上永久空转。

取舍：a) 读到 `b""` 就把连接标记为"半关闭"，若业务还要写（如 HTTP 响应未发完）可以 `shutdown(SHUT_WR)` 后继续写，写完再彻底注销；b) 用 `selectors.EVENT_READ` 时同时处理 `EVENT_WRITE` 的连接，写失败（`BrokenPipeError`）也要走同一套清理；c) 边沿触发（`EPOLLET`）能减少重复通知，但要求一次读到 `EAGAIN`，漏读会永久丢事件，自研服务器不建议一上来就用。核心原则：**事件通知不是状态，fd 的生命周期必须由应用显式结束**。

实战：事故形态是"长连接网关运行几小时后 CPU 100%，`strace` 看到某个 fd 上无限 `epoll_wait` 立即返回 + `recv` 返回 0；原因是客户端异常断开走了异常分支，只 `close` 了业务对象没 `unregister`"。下面演示对端关闭后 selector 连续返回、`recv` 为空，以及注销后恢复阻塞。

```python
import selectors
import socket

a, b = socket.socketpair()
sel = selectors.DefaultSelector()
sel.register(a, selectors.EVENT_READ, data="peer")
b.close()                       # 对端关闭 -> a 变为"永久可读"

spins = 0
empty = 0
for _ in range(3):
    events = sel.select(timeout=0.2)
    if events:
        spins += 1
        key, mask = events[0]
        if key.fileobj is a and a.recv(16) == b"":
            empty += 1

print("[1] 对端已关闭，select 立即返回次数:", spins)
print("[2] recv 返回空串次数:", empty)
print("[3] 未注销时每次 select 都会命中（水平触发）")

sel.unregister(a)
print("[4] 注销后 select 超时返回:", len(sel.select(timeout=0.2)))
sel.close()
a.close()

# 正确清理顺序
s1, s2 = socket.socketpair()
sel2 = selectors.DefaultSelector()
sel2.register(s1, selectors.EVENT_READ)
s2.close()
while True:
    ev = sel2.select(timeout=1)
    if not ev:
        break
    if s1.recv(16) == b"":
        sel2.unregister(s1)     # 先注销
        s1.close()              # 再关闭
        break
print("[5] 读到 EOF 后注销并关闭，循环退出")
sel2.close()
```

**追问一**：`close()` 会自动从 selector 里移除吗？—— 不会。`selectors` 只是在内部维护 fd → key 的映射，`close(fd)` 后 fd 可能被系统复用，selector 里残留的旧注册会让新 fd"莫名其妙"收到事件（fd 复用是经典事故：A 连接关闭未注销，新连接拿到同一个 fd 号，事件被派发给旧回调）。所以顺序必须是 `unregister` → `close`，且关闭后不要再持有 fd 号做判断。

**追问二**：`EPOLLHUP` 与 `EPOLLRDHUP` 有什么区别？—— `EPOLLRDHUP` 表示"对端关闭了写方向"（半关闭），`EPOLLHUP` 表示"挂断"，通常读写都不可用；两者都可能水平触发。Python 的 `selectors` 把它们折叠成 `EVENT_READ`，所以应用层看到的就是"可读"，唯一可靠的判断仍然是 `recv()` 的返回值：`b""` = 对端有序关闭，`ConnectionResetError` = RST。不要靠 mask 猜连接状态。

## 背诵要点
- 对端关闭后 fd 在 epoll/kqueue 上水平触发"可读"，不注销就永久空转。
- `recv()` 返回 `b""` 是优雅关闭，`ConnectionResetError` 是 RST；两者都要走清理。
- 清理顺序 `unregister` → `close`；`close` 不会自动注销，fd 复用会让旧回调误触发。

## 复盘追问
- 网关 CPU 100% 且某个 fd 上 `recv` 恒为 0，如何定位与修复？（HUP 水平触发、未注销）
- 为什么先 `close` 后 `unregister` 有风险？（fd 复用、selector 内部映射）
