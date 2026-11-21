---
title: [Q412] fork vs exec:多线程进程 fork 后为什么死锁?
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q412 · fork vs exec:多线程进程 fork 后为什么死锁?

> 难度:★★★★★ | 标签:multiprocessing, fork, 线程

**问**:一个跑了 10 个线程、持有锁的进程 `fork()` 之后,子进程为什么可能永远卡死?`multiprocessing` 各 start method 的默认值是什么?为什么官方推荐 spawn?

**答**:fork 只复制**调用它的那个线程**,其他线程(连同它们持有的锁)凭空消失,但锁的内存状态被原样复制——如果 fork 瞬间某线程正持有 `logging` 的锁或 malloc arena 锁,子进程里这把锁永远无人释放,子进程第一个申请它的线程就永久阻塞。这是"fork + threads"的经典死锁,也是 `os.fork()` 文档警告"多线程程序中 fork 只有 spawn 式安全子集"的原因。`multiprocessing` 的 start method:Linux 默认 `fork`(3.14 起默认改为 `forkserver`,3.12 起对多线程进程 fork 已发 DeprecationWarning),macOS 默认 `spawn`(因为 macOS 的 fork+exec 混合运行时本就不安全),Windows 只有 `spawn`。spawn 重新 import 主模块、开销大但语义干净;forkserver 由单线程桩进程统一 fork,兼顾速度与安全。

```python
# file: code/01_语言核心与底层/q412_fork_threads.py
import os
import sys
import threading
import time

lock = threading.Lock()

def locker():
    while True:
        with lock:            # 后台线程反复短暂持锁
            time.sleep(0.001)

threading.Thread(target=locker, daemon=True).start()
time.sleep(0.05)              # 大概率 fork 时锁恰被后台线程持有

pid = os.fork()               # 仅当前线程被复制,锁状态被复制
if pid == 0:
    # 子进程:尝试获取一把可能"已死"的锁 —— 竞争窗口内会永久阻塞
    got = lock.acquire(timeout=1)
    print("child acquired:", got)
    os._exit(0)
else:
    _, status = os.waitpid(pid, 0)
    print("child exit status:", status)
    print("start methods available:", __import__("multiprocessing").get_all_start_methods())
```

**追问**:1) 为什么 fork 后子进程要尽快 `os._exit` 而不是 `sys.exit`?——`sys.exit` 会触发 atexit/flush 等清理路径,可能再次触碰复制来的死锁资源;`_exit` 直接系统调用退出。2) daemon 线程在 fork 后的状态?——fork 复制不了任何线程,daemon 属性无从谈起;但 `multiprocessing` 的 fork 模式会伪造"父进程 daemon 线程已死"的表象,这是子进程内再创建进程报错的原因之一。
