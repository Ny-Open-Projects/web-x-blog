---
title: "[Q5722] SIGIO 信号驱动 IO：注册机制、坑点与 Python 现状"
date: 2026-11-24
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5722 · SIGIO 信号驱动 IO：注册机制、坑点与 Python 现状

难度：P7 ｜ 标签：SIGIO、O_ASYNC、F_SETOWN、信号驱动 IO、事件驱动演进、异步通知

**问**：信号驱动 IO 的注册流程是什么——内核在 fd 就绪时做什么？SIGIO 相比 select/epoll 省了什么、又丢了什么？为什么多 fd 场景下 SIGIO 几乎不可用？Python 的 asyncio 为什么完全不采用它？

**答**：
结论：信号驱动 IO（POSIX 异步 IO 通知模型）的注册三步：①`fcntl(fd, F_SETFL, flags | O_ASYNC)` 开启异步通知；②`fcntl(fd, F_SETOWN, getpid())` 告诉内核"这个 fd 的事件发给我的进程"；③注册 SIGIO 处理器。之后内核在 fd 就绪（有连接到达/有数据可读）时向该进程投递 SIGIO，处理器内再做真正的 read/accept。它省掉的是**阻塞等待本身**（select 的 O(n) 扫描或 epoll_wait 的系统调用挂起），换来的是"推"模型。但丢了三样致命的东西：①**不知来源**——SIGIO 只说"你的进程有 fd 就绪"，多个 fd 共享一个信号时无法分辨是谁（除非用 SIGRTMIN+序号为每个 fd 单独注册实时信号，POSIX 扩展且 fd 数受限）；②**不排队**——普通信号是计数合并的，两个事件到达只收到一次 SIGIO，处理器必须循环 drain 才不丢；③**不知事件类型**——读就绪、写就绪、错误都可能是同一个 SIGIO。这三点叠加，SIGIO 只适合"单 fd + 低频事件"的玩具场景。

取舍：a) Python 现状：asyncio/selectors 全部基于 select/poll/epoll/kqueue 轮询（Q653 的后端选择），没有任何框架用 SIGIO——正确性难题远大于省下的一次系统调用；b) 相邻技术：信号与 IO 的结合点是 **self-pipe/socketpair 唤醒**（Q5639）——用管道 fd 的可读性替代信号，把"事件通知"拉回多路复用的可控世界；signal.set_wakeup_fd（Q5677）是标准库给的半成品方案，其失败模式正说明信号不可靠；c) 信号处理器上下文的限制：Python 的信号处理器只在主线程字节码间隙执行（Q551），处理器里不能做复杂 IO——即使收到 SIGIO 也要回主 loop 处理，等于白忙；d) 对比维度：epoll 的优势不只是性能，而是**每个 fd 独立的事件掩码 + 返回事件列表**，把"是谁、什么事"都交代清楚；SIGIO 的信息量为零，这是它被淘汰的根本原因；e) 教学价值：理解 SIGIO 才能理解 why epoll——事件模型的演进史（阻塞→select→SIGIO→epoll/kqueue）里每一环都在补上一环的洞。

实战：事故形态是"面试造轮子题：候选人用 SIGIO 写单连接 echo，局域网测试通过，上线后连接数涨到 20 时丢事件——普通 SIGIO 合并导致 accept 漏接；正确答案是用 selectors 抽象，SIGIO 只作为'讲清事件模型缺陷'的反面教材"。下面在 macOS/Linux 上完整走一遍注册与触达（本机可复现信号到达）。

```python
# SIGIO 信号驱动 IO: 注册机制、坑点与 Python 现状
import fcntl
import os
import signal
import socket

print("[1] 信号驱动 IO 的三步注册: O_ASYNC + F_SETOWN + SIGIO 处理器")
srv = socket.socket()
srv.bind(("127.0.0.1", 0))
srv.listen(5)
print("    signal.SIGIO 可用:", hasattr(signal, "SIGIO"), "| 本进程 PID:", os.getpid())

flags = fcntl.fcntl(srv, fcntl.F_GETFL)
fcntl.fcntl(srv, fcntl.F_SETFL, flags | os.O_ASYNC)   # fd 就绪就发信号
fcntl.fcntl(srv, fcntl.F_SETOWN, os.getpid())          # 信号发给本进程
print("    O_ASYNC + F_SETOWN 注册成功 (内核承诺: fd 就绪时投递 SIGIO)")

got = []
def handler(signum, frame):
    got.append(signum)

prev = signal.signal(signal.SIGIO, handler)
import time
c = socket.create_connection(srv.getsockname())
time.sleep(0.05)                       # 等内核投递
print("[2] 有连接到达后收到 SIGIO:", got, "(信号只说'有事', 不说是哪个 fd/什么事件)")

print("[3] 三个致命坑: 多 fd 共享一个信号分不清来源; 信号不排队会合并丢失; 处理器里必须循环 accept")
signal.signal(signal.SIGIO, prev)
c.close()
srv.close()

print("[4] Python 现状: asyncio/selectors 全部走 select/epoll/kqueue 轮询, 不用 SIGIO")
print("    信号驱动只是'省一次空轮询'的优化, 正确性难题(来源/丢失)让它不适合通用框架")
```

**追问一**：SIGIO 与实时信号（SIGRTMIN）的队列化有什么区别？—— 普通信号（SIGIO 是其中一个）**不排队**：同一信号多次投递只保留一个 pending 位，处理器必须 drain 到底（循环 accept/读直到 EAGAIN）；POSIX 实时信号（SIGRTMIN 到 SIGRTMAX）**排队**且有编号顺序，还支持 `sigqueue` 附带值——理论上可以"每个 fd 绑定一个实时信号"来区分来源，但实时信号数量有限（通常 30 个上下），fd 规模上不去，且 Python 标准库对实时信号的注册支持有限。所以即使在 POSIX 层面，SIGIO 路线也修不到 epoll 的可用性，这是模型缺陷不是参数问题。

**追问二**：为什么说 set_wakeup_fd 是"半成品方案"？—— signal.set_wakeup_fd(fd) 把信号号写进一个 fd（通常配 self-pipe），让主 loop 的 select 把"有信号"纳入统一轮询——它解决了"信号与 IO 两套等待"的整合问题（Q5639/Q5570 的信号处理演进）。但半成品在于：写入的只是信号号，**真正的信号处理器还是在主线程字节码间隙执行**，wake fd 只保证 select 能醒来；写失败（缓冲满）时 set_wakeup_fd 会直接把处理器重置为默认行为（Q5677 的失败模式）——在事件风暴下通知通道本身会失效。这再次印证：信号模型的不可靠性是结构性的，任何"打补丁"都到不了 epoll 的正确性水位。

## 背诵要点
- SIGIO 三步：O_ASYNC + F_SETOWN + 处理器；内核"推"事件但零信息（谁/何事都不知道）。
- 三缺陷：多 fd 无法分辨来源、普通信号合并不排队（必须 drain）、处理器在主线程字节码间隙执行。
- 演进逻辑：SIGIO → self-pipe 唤醒（Q5639）→ epoll/kqueue；Python 全家桶不用 SIGIO，正确性>省一次调用。

## 复盘追问
- 为什么 asyncio 不用 SIGIO 做事件通知？（来源不可辨+信号合并丢失+主线程限制；epoll 返回事件列表信息完整）
- set_wakeup_fd 解决了什么、没解决什么？（把信号纳入 select 等待；但处理器仍主线程执行且缓冲满会重置处理器）
