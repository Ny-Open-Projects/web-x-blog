---
title: [Q5607] PEP475 EINTR 自动重试演进
date: 2026-11-21
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5607 · PEP 475 与 EINTR 自动重试的演进

> 难度:★★★★☆ | 标签:版本演进, EINTR, 系统调用

**问**:3.5 之后你几乎看不到 `InterruptedError`，这是怎么做到的？还有哪些地方会"漏"出来？

**答**:结论：信号到达慢系统调用时内核返回 `EINTR`，历史代码必须在每个 IO 处理它（或被 `select.select` 突然返回炸掉）。PEP 475（Python 3.5）把语义改成：系统调用层捕获 `InterruptedError` 后**自动重试**，并先让 Python 信号处理器跑完（用 `clock_gettime` 等"可中断"调用垫时机）。这是"把正确性下沉到运行时"的典型版本演进——应用代码从此默认免疫 EINTR，代价是"信号打断超时"这类依赖被打断的行为消失了（`socket.timeout` 不再因信号提前触发）。仍会漏出的位置：① 自己写 C 扩展直接调系统调用；② 某些绕过 `socket` 封装的底层调用；③ 信号处理器里抛出的异常在重试边界处的语义变化。`signal.set_wakeup_fd` 与 asyncio 信号路径（Q5570）都建立在 PEP 475 之上。

```python
import os, signal, socket, time

# 复现 EINTR：给自己发信号，同时做一个会被打断的慢调用
def handler(sig, frame):
    pass                                   # 空处理器：只为打断系统调用

old = signal.signal(signal.SIGUSR1, handler)

s1, s2 = socket.socketpair()
s1.settimeout(2.0)
os.kill(os.getpid(), signal.SIGUSR1)
t0 = time.perf_counter()
try:
    # 3.5+：recv 被 EINTR 打断后自动重试，整体等到超时才抛 timeout
    s1.recv(1024)
except socket.timeout as e:
    print(f"3.5+ 语义：EINTR 自动重试，最终 {time.perf_counter()-t0:.2f}s 后才 timeout")
finally:
    signal.signal(signal.SIGUSR1, old)
    s1.close(); s2.close()

# 粗算自动重试的账：信号频率 vs 调用时长，被打断 N 次就重试 N 次
print("PEP 475 前：每处 IO 都要 except InterruptedError: continue")
```

**追问一层**:为什么自动重试前要先执行 Python 层的信号处理器？如果不执行会出什么问题？
**追二层**:`select()` 在 3.5 前后的行为差异？PEP 475 如何让 asyncio 的信号唤醒（self-pipe）成为可能？

**背诵要点**
- 3.5 起 EINTR 在系统调用层自动重试，应用默认免疫 InterruptedError。
- 重试前先跑 Python 信号处理器，保证 handler 有序执行。
- 副作用：依赖"信号打断超时"的代码语义变了；C 扩展仍会漏。

**复盘追问**
- 一个自研 C 扩展偶发 InterruptedError，修复应该在哪层？提示：扩展内 retry 循环或向 Python 抛 OSError 让其重试。
- "信号打断 sleep 提前醒"的旧代码升级 3.5+ 后行为如何变？提示：sleep 会重试补满时长。
