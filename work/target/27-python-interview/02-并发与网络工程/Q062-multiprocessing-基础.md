---
title: [Q062] multiprocessing 基础
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q062 · multiprocessing 基础

> 难度:★★☆ | 标签:multiprocessing, 进程

**问**:multiprocessing 和 threading 的本质区别?为什么子进程代码要放在 if __name__ == "__main__" 里?

**答**:每个子进程有独立的解释器和内存空间,绕开 GIL 获得真并行,代价是创建开销大、数据要序列化传递。在 Windows/macOS 的 spawn 启动方式下,子进程会重新 import 主模块,不加 `if __name__ == "__main__":` 保护会无限递归创建进程。进程间共享状态需显式使用 Queue、Pipe 或共享内存。

```python
# file: code/02_并发与网络工程/q062_multiprocessing_basic.py
import multiprocessing
import os
import time


def worker(seconds: float) -> None:
    time.sleep(seconds)
    print(f"子进程 pid={os.getpid()} 完成耗时 {seconds}s 任务")


if __name__ == "__main__":
    print("主进程 pid =", os.getpid())
    procs = [multiprocessing.Process(target=worker, args=(0.3 + i * 0.1,)) for i in range(3)]
    for p in procs:
        p.start()
    for p in procs:
        p.join()
    print("所有子进程退出, exitcode:", [p.exitcode for p in procs])
```

**追问**:
- fork 和 spawn 启动方式有什么区别?——fork 复制父进程内存,快但仅 Unix 且与多线程程序不兼容;spawn 重启解释器并重新 import 主模块,慢但跨平台,macOS/Windows 默认 spawn。
- 子进程能「继承」全局变量吗?——fork 下是写时复制副本,修改互不可见;spawn 下变量要靠参数 pickle 传过去,共享状态一律走 Queue/Pipe/共享内存。
- 缺 `if __name__ == "__main__":` 会怎样?——spawn 模式下子进程 import 主模块,再次执行创建进程的代码,递归创建进程直至爆掉,入口必须保护。

---
