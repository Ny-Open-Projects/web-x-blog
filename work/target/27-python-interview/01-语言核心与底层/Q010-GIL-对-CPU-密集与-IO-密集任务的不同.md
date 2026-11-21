---
title: [Q010] GIL 对 CPU 密集与 IO 密集任务的不同影响
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q010 · GIL 对 CPU 密集与 IO 密集任务的不同影响

> 难度:★★★ | 标签:GIL, 并发

**问**:同样是多线程,为什么 IO 密集场景有效而 CPU 密集场景反而更慢?

**答**:IO 密集任务大部分时间在等待,线程在进入阻塞 IO 前会释放 GIL,其他线程得以运行,多线程能显著提高吞吐。CPU 密集任务始终需要解释器执行字节码,GIL 把多线程串行化,还叠加了锁竞争和上下文切换开销,通常比单线程更慢,应改用 multiprocessing 或把热点交给释放 GIL 的 C 扩展(如 NumPy)。

```python
# file: code/01_语言核心与底层/q010_gil_cpu_vs_io.py
import threading
import time

def cpu_bound(n):
    total = 0
    for i in range(n):
        total += i * i
    return total

def io_like(duration):
    time.sleep(duration)   # sleep 会释放 GIL,模拟阻塞 IO

if __name__ == "__main__":
    N = 1_000_000    # 演示规模缩小,保证脚本秒级跑完

    t0 = time.perf_counter()
    cpu_bound(N)
    cpu_bound(N)
    print("CPU 串行:", round(time.perf_counter() - t0, 3), "s")

    t0 = time.perf_counter()
    threads = [threading.Thread(target=cpu_bound, args=(N,)) for _ in range(2)]
    for t in threads: t.start()
    for t in threads: t.join()
    print("CPU 多线程,通常更慢:", round(time.perf_counter() - t0, 3), "s")

    t0 = time.perf_counter()
    threads = [threading.Thread(target=io_like, args=(0.3,)) for _ in range(4)]
    for t in threads: t.start()
    for t in threads: t.join()
    print("IO 多线程,约等于单个耗时:", round(time.perf_counter() - t0, 3), "s")
```

**追问**:1) 有没有去掉 GIL 的官方努力?——有,PEP 703 的 free-threaded 构建,CPython 3.13 起提供实验版本,可在编译期去掉 GIL,但生态兼容仍在推进中。2) Python 3.2 的 GIL 切换机制改了什么?——从「每 100 条字节码强制切换」改为当前线程每 5ms 主动让出,消除了 CPU 线程长期霸占 GIL 导致 IO 线程饿死的 convoy effect。3) 多进程一定比多线程快吗?——不一定:进程有启动、pickle 序列化和 IPC 成本,小任务 fan-out 的开销可能吃掉并行收益;先测量任务粒度再选模型。
