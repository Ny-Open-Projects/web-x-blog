---
title: [Q551] signal 的执行时机:主线程与字节码间隙
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q551 · signal 的执行时机:主线程与字节码间隙

> 难度:★★★★★ | 标签:signal, 线程

**问**:信号处理函数什么时候真正执行?为什么工作线程里注册 handler 会直接报错?

**答**:CPython 把 Python 层的 signal handler 注册进内核,但**执行**在主线程:内核中断到达后只设置标志,主线程在两条字节码之间(解释器的 eval breaker 检查点)才运行处理函数——所以信号响应粒度是字节码级,长 C 调用(大矩阵乘、阻塞的系统调用)会显著推迟;处理函数里再 sleep 还会拖慢主线程。signal.signal 只能在主线程调用(否则 ValueError),这是设计而非限制失误:信号本来是进程级控制流,统一在主线程处理才能与解释器状态协调。子进程/线程的「可中断等待」行为也由这一机制决定。

```python
# file: code/01_语言核心与底层/q551_signal_timing.py
import os
import signal
import threading
import time

received = []

def handler(signum, frame):
    received.append(signum)

if __name__ == "__main__":
    old = signal.signal(signal.SIGUSR1, handler)

    worker = threading.Thread(target=lambda: time.sleep(0.1))
    worker.start()
    worker.join()
    os.kill(os.getpid(), signal.SIGUSR1)   # 发给进程:由主线程执行 handler
    time.sleep(0.2)                        # 主线程跑字节码,处理函数才有机会运行
    print("handler saw:", received)
    signal.signal(signal.SIGUSR1, old)

    def try_register():
        try:
            signal.signal(signal.SIGUSR1, handler)
        except ValueError as e:
            print("worker thread:", e)

    t = threading.Thread(target=try_register)
    t.start()
    t.join()
```

**追问**:1) 怎么让「主线程卡在 C 调用」也能响应 SIGTERM?——约定俗成的方案:把长 C 调用切片、或用 setitimer/alarm 配合、或在另一个线程用 self-pipe 把信号转成事件循环可读的 fd(asyncio 的信号处理就是这个思路)。2) handler 到底什么时候执行?——信号到达只置标志,解释器在主线程下一条字节码边界检查并执行;C 扩展长时间运行期间不检查;handler 必须在主线程注册(非主线程注册抛 ValueError)。3) 底层机制?——eval breaker:每次字节码边界测 pending signals;signal.set_wakeup_fd 把信号写到 fd,事件循环 select 到即感知——这是「信号转 IO」的官方通道。4) 生产陷阱?——优雅停机的清理逻辑放 handler 里风险大(handler 重入、与主流程并发);多线程程序信号只投递主线程;超时强杀兜底(supervisor)必须有,不能全指望优雅退出。
