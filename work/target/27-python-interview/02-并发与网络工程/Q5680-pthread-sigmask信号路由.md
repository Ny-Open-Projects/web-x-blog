---
title: "[Q5680] pthread_sigmask 与信号路由：专用线程收信号"
date: 2026-11-23
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5680 · pthread_sigmask 与信号路由：专用线程收信号

难度：P7 ｜ 标签：signal、pthread_sigmask、sigwait、多线程、事件循环

**问**：多线程服务里主线程跑 asyncio loop，另有 8 个 worker 线程。SIGTERM 来了，为什么有时优雅停机完全没执行、进程被 SIGKILL？Python 的信号处理器只能在主线程跑，但信号是"进程级"的——内核到底把它投递给哪个线程？`pthread_sigmask` 阻塞信号后，`sigwait` 和 `signal.signal` 是什么关系？这套机制和 asyncio 的 `add_signal_handler` 怎么配合？

**答**：
结论：进程级信号由内核投递给**任意一个没有阻塞该信号的线程**，具体哪个不确定；而 Python 层 `signal.signal()` 注册的 handler 只会在**主线程**的字节码间隙执行。如果信号被投递到某个 worker 线程，而该线程正卡在 C 扩展/阻塞调用里，Python handler 可能迟迟不跑；如果主线程当时在 `epoll_wait`，则要靠 self-pipe 唤醒。工程上的标准解法是：在创建任何线程**之前**，主线程用 `signal.pthread_sigmask(SIG_BLOCK, {...})` 把要接管的信号全部阻塞（新线程继承这个掩码），然后启动一个专用线程调用 `signal.sigwait({...})` 同步取信号；取到后通过 `loop.call_soon_threadsafe` 把"停机"投递回事件循环。这样信号路由是确定的，handler 不依赖"主线程恰好被调度"。

取舍：`sigwait` 是同步阻塞的，专用线程只做"接信号 + 投递"，不要在里面做重活；它要求信号处于 blocked 状态，否则行为未定义/信号可能被默认处置。`pthread_sigmask` 是**每线程**掩码，不是进程级 `sigprocmask` 的替代；子线程会继承创建时的掩码，所以必须在 `threading.Thread.start()` 之前设置。asyncio 的 `add_signal_handler` 在 Unix 上内部也是 self-pipe + 主线程回调，单 loop 服务用它更简单；多 loop/多线程或需要"信号处理与 loop 解耦"时，用 sigwait 线程更可控。

实战：事故形态是"压测时 SIGTERM 十次有三次不 graceful，日志没有 'shutting down'，K8s 60 秒后 SIGKILL"。根因往往是信号被投递到 worker 线程，主线程的 handler 没及时跑，或自定义 handler 里做了阻塞操作。下面验证：主线程阻塞 SIGUSR1 后，`os.kill` 让信号保持 pending，专用线程 `sigwait` 能取到；解除阻塞后主线程恢复处理。注意 `sigwait` 返回的是 `Signals` 枚举。

```python
import os
import signal
import threading
import time

got = []

signal.pthread_sigmask(signal.SIG_BLOCK, {signal.SIGUSR1})


def sig_waiter():
    sig = signal.sigwait({signal.SIGUSR1})      # 专用线程同步取信号
    got.append(sig)


t = threading.Thread(target=sig_waiter)
t.start()
time.sleep(0.1)
os.kill(os.getpid(), signal.SIGUSR1)            # 主线程已阻塞，信号保持 pending
t.join(2)
print("sigwait 收到:", got, " 正确:", got == [signal.SIGUSR1])

signal.pthread_sigmask(signal.SIG_UNBLOCK, {signal.SIGUSR1})
print("主线程掩码已恢复")

signal.signal(signal.SIGUSR1, lambda *a: None)
os.kill(os.getpid(), signal.SIGUSR1)
print("解除阻塞后主线程可处理")
```

**追问一**：为什么 `signal.signal()` 只能在主线程注册？子线程注册会怎样？——CPython 把 Python 级信号处理器统一放在主解释器的主线程执行（`PyErr_CheckSignals` 在主线程字节码循环里跑），子线程调用 `signal.signal` 会抛 `ValueError: signal only works in main thread`。这是语言层约束，不是内核限制。因此多线程下要么把信号处理集中到主线程（asyncio 的做法），要么用 `sigwait` 在专用线程同步收取，绕开 Python handler。

**追问二**：`pthread_sigmask` 阻塞信号后，信号会不会丢？——不会丢，会保持 **pending**，直到该信号被解除阻塞或被 `sigwait/sigtimedwait/sigwaitinfo` 取走；但同类标准信号如果不支持排队，多个相同信号可能合并成一个。实时信号（SIGRTMIN~）支持排队，标准信号不保证。所以"停机信号"这种低频事件没问题，但不要用标准信号做计数器/消息队列。

## 背诵要点
- 进程级信号投递给任意未阻塞它的线程；Python handler 只在主线程跑，投递到 worker 会延迟/丢失停机。
- 标准模式：创建线程前 `pthread_sigmask(SIG_BLOCK)`，专用线程 `sigwait` 收取，再 `call_soon_threadsafe` 投回 loop。
- `sigwait` 要求信号已阻塞；标准信号可能合并、不排队；asyncio `add_signal_handler` 只适合主线程单 loop。

## 复盘追问
- SIGTERM 偶尔不触发优雅停机、最终被 SIGKILL，如何用信号路由解释并重构？（任意线程投递、主线程 handler、sigwait 专用线程）
- `pthread_sigmask` 阻塞后信号会丢吗？标准信号与实时信号有什么区别？（pending、合并 vs 排队）
