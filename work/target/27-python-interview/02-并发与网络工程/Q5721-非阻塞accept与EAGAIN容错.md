---
title: "[Q5721] 非阻塞 accept 与 EAGAIN：事件与竞态的容错边界"
date: 2026-11-24
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5721 · 非阻塞 accept 与 EAGAIN：事件与竞态的容错边界

难度：P6 ｜ 标签：accept、EAGAIN、EWOULDBLOCK、BlockingIOError、非阻塞、selectors、惊群

**问**：非阻塞 socket 上无连接可 accept 时发生什么？select/selectors 报告"可读"之后再 accept，为什么仍可能拿到 EAGAIN？多 worker（SO_REUSEPORT/共享监听）场景下这个容错为什么是标配？Python 里 EAGAIN 对应哪个异常？

**答**：
结论：非阻塞监听 socket 在无 pending 连接时，`accept()` 立即返回 EAGAIN/EWOULDBLOCK（errno 35/11），Python 层映射为 `BlockingIOError`。关键进阶点是**事件与取件之间的竞态**：selectors 报告可读 ≠ accept 一定能拿到连接——①多 worker 场景下另一个 worker 可能"抢"走了这个连接（内核就绪队列里的事件副本已发给两个 worker）；②某些实现里连接在事件产生后又被回滚（如客户端在完成三次握手前发 RST，BSD 系会把 pending 连接从队列移除）。所以正确写法是"select 就绪 → try accept → 容忍 BlockingIOError → 继续轮询"，把 EAGAIN 当**正常路径**处理而不是错误。这与非阻塞 send/recv 的 EAGAIN 是同一族（Q5688 的部分写、Q5598 的管道缓冲），区别在 accept 的竞态窗口主要由多 worker 引入，单线程 asyncio loop 里基本见不到。Python 的 `selectors.DefaultSelector` 在 macOS 选 kqueue、Linux 选 epoll（Q653/Q5558），上层语义一致，但这个 accept 竞态在不同内核上的触发频率不同——macOS/BSD 更容易遇到 RST 回滚。

取舍：a) 单线程事件循环（asyncio）：loop 内部已处理，业务层无需容错；b) 自研多 worker reactor：accept 处必须 try/except BlockingIOError，这是正确性前提而不是性能优化；c) 惊群治理：SO_REUSEPORT 让内核按四元组分发连接（Q5507），每个 worker 独立监听队列，天然减少抢夺；共享同一监听 fd + LT 模式的方案则要靠 oneshot（Q5720）；d) accept 后立刻处理监听 socket 属性问题：accept 出的连接**不继承**监听 socket 的超时/阻塞属性（Q5728 专卡），必须显式 settimeout/setblocking；e) errno 分诊：EAGAIN(35)/EWOULDBLOCK 同值、EINTR 已被 PEP 475 自动重试（Q5607/Q5121），accept 层真正要处理的只剩 EAGAIN 与 ECONNABORTED。

实战：事故形态是"自研 reactor 四个 worker 共享监听 socket，压测下偶发 'BlockingIOError: accept' 未捕获导致 worker 退出；修复为 accept 路径容忍 EAGAIN 并继续 loop，同时把 accept 改为循环取空（一次就绪可能有多个 pending 连接，LT 模式下轮询会再来，ET 模式必须取空）"。下面演示 EAGAIN 的直接表现与 selectors 的正确轮询。

```python
# 非阻塞 accept 与 EAGAIN: 竞态窗口与容错
import selectors
import socket
import time

srv = socket.socket()
srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
srv.bind(("127.0.0.1", 0))
srv.listen(16)
port = srv.getsockname()[1]
srv.setblocking(False)                      # 监听 socket 也非阻塞

print("[1] 非阻塞 accept 在无连接时立刻返回 EAGAIN (Python 里是 BlockingIOError)")
try:
    srv.accept()
except BlockingIOError as exc:
    print("    BlockingIOError:", exc.errno, "(EAGAIN/EWOULDBLOCK)")

print("[2] 正确姿势: select 就绪后再 accept, 但仍要容忍 EAGAIN -- 就绪与可取之间有竞态")
sel = selectors.DefaultSelector()
sel.register(srv, selectors.EVENT_READ)
clients = [socket.create_connection(("127.0.0.1", port)) for _ in range(3)]
time.sleep(0.05)
accepted = 0
for _ in range(3):
    for key, _ in sel.select(timeout=0.1):
        try:
            conn, addr = key.fileobj.accept()
            accepted += 1
        except BlockingIOError:
            print("    竞态: 事件已就绪但 accept 拿不到连接, 继续轮询而不是报错")
print("[3] 共 accept", accepted, "个连接; 容忍 EAGAIN 是多 worker reactor 的标配")
for c in clients:
    c.close()
srv.close()
print("[4] 注意: accept 出的连接不继承监听 socket 的超时/阻塞属性, 接手后必须显式设置 -> Q5728")
```

**追问一**：客户端在三次握手完成后立刻发 RST，服务端 accept 会怎样？—— BSD/macOS 内核会把该 pending 连接从完成队列**移除**，且标准 accept 是阻塞的会继续等下一个连接；但**非阻塞**路径上，select 已上报的事件与队列被清空之间没有同步——accept 直接拿 EAGAIN。Linux 的行为不同：accept 会返回一个已死连接（后续 read 得 ECONNRESET）。这是"事件≠取件"竞态的内核层来源，也是 POSIX 未定案的知名分歧。结论一致：accept 的 EAGAIN 必须容错，且 accept 到的连接首帧读取要处理 ConnectionResetError（Q1311 的 errno 分诊）。

**追问二**：一次 select 就绪后要 accept 几次？—— 看**触发模式与设计目标**：ET（边缘触发）模式下事件只通知一次，必须 `while True: accept()` 循环取空，否则剩余 pending 连接要等下一个新事件才被发现——高并发短连接场景会显著延迟接客；LT（水平触发）模式下一轮不取空，下轮 select 会继续上报，取一次也正确，只是多一轮轮询开销。单 worker 高吞吐服务器（Q654 的 C10K 思路）通常取空 + 非阻塞容错；worker 数多时取空循环与 REUSEPORT 分发叠加，注意循环上限（如每轮最多 accept N 条）防止某个 worker 被突发长队占死（Q2914 的最大连接保护同理）。

## 背诵要点
- 非阻塞 accept 无连接 → EAGAIN/EWOULDBLOCK → Python 的 BlockingIOError；容错后继续轮询，不当错误处理。
- select 就绪 ≠ accept 成功：多 worker 抢夺 + RST 回滚是竞态来源；ET 模式必须循环取空。
- accept 出的连接不继承监听 socket 属性；EINTR 已被 PEP 475 自动重试，accept 层只防 EAGAIN/ECONNABORTED。

## 复盘追问
- 四 worker reactor 压测偶发 BlockingIOError 崩溃，根因与修复？（事件与取件竞态；accept 容忍 EAGAIN + 循环取空）
- macOS 与 Linux 上 RST 后的 accept 行为差异？（BSD 移除队列返回 EAGAIN；Linux 返回死连接读出 ECONNRESET）
