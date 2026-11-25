---
title: "[Q5677] signal.set_wakeup_fd 的失败模式与 asyncio 冲突"
date: 2026-11-23
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5677 · signal.set_wakeup_fd 的失败模式与 asyncio 冲突

难度：P7 ｜ 标签：signal、set_wakeup_fd、self-pipe、asyncio、优雅停机

**问**：自研事件循环用 `signal.set_wakeup_fd(pipe_w)` 把 SIGTERM 从信号处理器"叫醒"阻塞在 `select` 的主循环。为什么接到 asyncio 之后，优雅停机偶尔完全没反应？`set_wakeup_fd` 对 fd 有什么硬性要求？信号处理函数里只写一个字节，写不进去会怎样？本题与 Q5639（self-pipe 原理）的边界在哪？`loop.add_signal_handler` 和它是什么关系？

**答**：
结论：Python 的 C 级信号处理器不能做复杂操作，只能把"信号编号"这一个字节写到 `set_wakeup_fd` 指定的 fd，从而唤醒阻塞在 `select/epoll` 上的主循环；真正的 Python handler 随后在主线程字节码间隙执行。硬性要求：必须在**主解释器的主线程**调用、fd 必须是**非阻塞**的写端（信号处理器不能阻塞）；否则 `ValueError`（`the fd N must be in non-blocking mode` / `only works in main thread`）。如果管道满了，Python 写不进去，会打印 `Exception ignored when trying to write to the signal wakeup fd`——信号本身仍会被处理，但你的 `select` 可能永远不被唤醒，表现为"停机信号丢了"。

取舍：一个进程只能有一个 wakeup fd，后设置会覆盖前一个（返回旧 fd）。asyncio 的 `loop.add_signal_handler` 内部就用了 self-pipe/wakeup fd（Q5639）；如果你在 asyncio 之外又 `set_wakeup_fd`，会把它覆盖掉，导致 asyncio 的信号回调不再被唤醒。要混用，必须保存旧 fd 并自己转发，或者干脆统一用 `loop.add_signal_handler`；多线程服务器则考虑 `pthread_sigmask` + `sigwait` 专用线程（Q5680）。fd 的生命周期也要管：设置 `-1` 恢复，关闭 fd 前先恢复，避免信号处理器写到已关闭的 fd。

实战：事故形态是"接入 asyncio 后 SIGTERM 十次有一次不触发 graceful shutdown，K8s 等到 SIGKILL 强杀，连接被 RST"。下面验证：主线程非阻塞 socketpair 能收到信号编号字节；阻塞 fd 和非主线程分别报 `ValueError`；并打印旧 fd，说明"覆盖"是真实存在的。

```python
import os
import signal
import socket
import threading
import time

r, w = socket.socketpair()
r.setblocking(False)
w.setblocking(False)
signal.signal(signal.SIGUSR1, lambda *args: None)

old = signal.set_wakeup_fd(w.fileno())
print("旧 wakeup fd:", old)
os.kill(os.getpid(), signal.SIGUSR1)
time.sleep(0.05)
data = r.recv(16)
print("wakeup 字节:", list(data), "等于信号编号:", list(data) == [signal.SIGUSR1])
signal.set_wakeup_fd(-1)
r.close()
w.close()

r2, w2 = socket.socketpair()
try:
    signal.set_wakeup_fd(w2.fileno())
except Exception as e:
    print("阻塞 fd ->", type(e).__name__, e)
r2.close()
w2.close()


def worker():
    r3, w3 = socket.socketpair()
    w3.setblocking(False)
    try:
        signal.set_wakeup_fd(w3.fileno())
    except Exception as e:
        print("非主线程 ->", type(e).__name__, e)
    r3.close()
    w3.close()


t = threading.Thread(target=worker)
t.start()
t.join()
```

**追问一**：为什么 fd 必须非阻塞？管道满了会怎样？——信号处理器运行在任意字节码间隙，不能睡眠/等待；如果 fd 是阻塞的且管道满，处理器会卡住整个进程（甚至死锁）。所以 CPython 强制非阻塞；写不进去时它只能放弃并打印 `Exception ignored ...`，这一条信号就不会唤醒事件循环。要降低风险：wakeup 管道只传信号编号（1 字节）、读端及时排空、不要用它传业务数据；高信号频率场景用 `signal.sigwait` 或 signalfd 更合适。

**追问二**：`loop.add_signal_handler` 能不能和自建 wakeup fd 共存？——不能简单共存：asyncio 在 loop 初始化时可能已经设置了 wakeup fd，你再 `set_wakeup_fd` 会覆盖它，导致 `call_soon_threadsafe`/信号回调的唤醒链断掉。正确做法是只用一个机制：要么全部用 `loop.add_signal_handler`（它在 Unix 上会把信号回调投递到 loop），要么自己在 loop 之外管理 wakeup fd 并把读端注册进 loop；混用时必须保存并转发旧 fd（读旧 fd 再写新 fd），且注意关闭顺序。

## 背诵要点
- `set_wakeup_fd` 在信号处理器里写 1 字节信号编号唤醒 `select`；要求主线程、非阻塞 fd，否则 `ValueError`。
- 管道满时写失败只打印 `Exception ignored...`，信号处理了但 loop 不被唤醒；进程只能有一个 wakeup fd，后设覆盖前设。
- asyncio 的 `add_signal_handler` 内部用 self-pipe；不要与自建 wakeup fd 混用，除非显式转发旧 fd。

## 复盘追问
- 接入 asyncio 后 SIGTERM 偶尔不触发优雅停机，如何用 wakeup fd 覆盖/管道满解释？（单一 wakeup fd、主线程/非阻塞约束、self-pipe）
- 为什么信号处理器里不能阻塞写，管道满时 CPython 怎么处理？（异步信号安全、丢弃并打印 ignored、loop 不醒）
