---
title: [Q576] GIL 的切换时机:setswitchinterval 实验
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q576 · GIL 的切换时机:setswitchinterval 实验

> 难度:★★★☆ | 标签:GIL, 调度, 性能

**问**:GIL 什么时候释放?sys.setswitchinterval 调大调小会怎样?

**答**:GIL 在三种时机让出:IO 调用(文件、socket、sleep)前主动释放;每执行约 `sys.getswitchinterval()`(默认 5ms)后由当前线程检查并强制让出;C 扩展显式释放。调小 switchinterval,线程切换更频繁,"响应性"更好但上下文切换开销上升,竞态窗口变多;调大则单线程跑得更久、吞吐略升,但其他线程延迟变大。纯 CPU 多线程在 GIL 下总吞吐不会提升,实验里还能直观看到丢失更新随切换频率变化。

```python
# file: code/02_并发与网络工程/q576_switch_interval.py
import sys
import threading
import time

counter = 0


def spin(n: int) -> None:
    global counter
    for _ in range(n):
        counter += 1  # 读-改-写, 依赖 GIL 切换时机决定竞态程度


def run(n_iter: int) -> tuple:
    global counter
    counter = 0
    ts = [threading.Thread(target=spin, args=(n_iter,)) for _ in range(4)]
    t0 = time.perf_counter()
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    dt = time.perf_counter() - t0
    return counter, dt


if __name__ == "__main__":
    n = 100000
    for interval in (0.005, 0.001, 0.00005):
        sys.setswitchinterval(interval)
        got, dt = run(n)
        expected = 4 * n
        print(f"switchinterval={interval:<8} 结果 {got}/{expected} "
              f"丢失 {expected - got:>6} 耗时 {dt:.3f}s")
    sys.setswitchinterval(0.005)  # 恢复默认
```

**追问**:1) 为什么 IO 密集多线程仍然有效?——线程在执行 IO 调用时释放 GIL,其他线程立刻可以拿到 GIL 执行,"等待"被并行化了,这正是 IO 密集场景多线程能提速的原因。2) setswitchinterval 的实验能告诉我们什么?——默认 5ms 切换间隔影响「纯 Python 轮转」的公平性与粒度;调大让 CPU 密集线程少切换、调小让 IO 线程响应更快;但它是全局权衡,不是调优旋钮。3) 释放 GIL 的三类点?——IO 系统调用、C 扩展显式释放(Py_BEGIN_ALLOW_THREADS)、部分大整数运算;纯 Python 计算不释放(Q577)。4) 生产陷阱?——按「GIL 存在」否定一切多线程;CPU 密集硬塞线程池(Q599 选型);调 switchinterval 掩盖设计问题。

---
