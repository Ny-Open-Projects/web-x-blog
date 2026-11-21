---
title: [Q577] C 扩展与释放 GIL:ctypes 实验
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q577 · C 扩展与释放 GIL:ctypes 实验

> 难度:★★★★ | 标签:GIL, ctypes, C 扩展

**问**:都说"用 C 扩展绕过 GIL",到底什么才算绕过?

**答**:关键不是"用 C 写",而是 C 代码在执行期间是否释放 GIL。ctypes 的默认调用约定是 `release_gil=True`(CDLL),调用 libc 的阻塞函数时其他 Python 线程可以继续跑;而 PyDLL 则持有 GIL。所以:包一层 release GIL 的 C 计算(如 numpy 的 BLAS、zlib 压缩大块数据)能真并行;调一个不释放 GIL 的 C 函数再快也帮不了并发。验证方法很直接:一个线程跑长 C 调用,主线程同时跑纯 Python 循环,看循环是否推进。

```python
# file: code/02_并发与网络工程/q577_release_gil.py
import ctypes
import ctypes.util
import threading
import time

path = ctypes.util.find_library("c") or ("libc.so.6" if sys.platform != "darwin" else "libc.dylib")
libc = ctypes.CDLL(path or "libc.so.6")  # CDLL: 调用期间释放 GIL
libc.usleep.argtypes = [ctypes.c_uint]

SPIN_SECONDS = 0.5
iterations = [0]
stop = threading.Event()


def python_spin() -> None:
    """纯 Python 忙循环, 用来探测 GIL 是否可用。"""
    while not stop.is_set():
        iterations[0] += 1


if __name__ == "__main__":
    import sys
    if sys.platform == "darwin":
        path = ctypes.util.find_library("libc.dylib") or "/usr/lib/libc.dylib"
    else:
        path = ctypes.util.find_library("c") or "libc.so.6"
    libc = ctypes.CDLL(path)
    libc.usleep.argtypes = [ctypes.c_uint]

    spinner = threading.Thread(target=python_spin, daemon=True)
    spinner.start()

    iterations[0] = 0
    t0 = time.perf_counter()
    libc.usleep(300000)  # 0.3s 的 C 阻塞调用: 释放 GIL
    c_blocking = iterations[0] / (time.perf_counter() - t0)

    iterations[0] = 0
    t0 = time.perf_counter()
    n = 3000000
    libc.rand.restype = ctypes.c_int
    for _ in range(n):  # 大量微小 C 调用: 每次调用都要抢 GIL
        libc.rand()
    c_many = iterations[0] / (time.perf_counter() - t0)

    stop.set()
    spinner.join()
    print(f"C 阻塞调用期间 Python 循环推进率: {c_blocking:,.0f} 次/秒")
    print(f"海量微小 C 调用期间推进率:      {c_many:,.0f} 次/秒")
    print("结论: 单次长 C 调用释放 GIL, 频繁短调用反而加剧 GIL 争抢")
```

**追问**:1) 那 CPU 密集任务正确的并行姿势是什么?——multiprocessing/ProcessPoolExecutor 每个进程一份 GIL,或选 numpy/BLAS 这类在 C 层已释放 GIL 的库,或等 free-threaded 构建成熟。2) 释放 GIL 的边界?——只有包装了 Py_BEGIN_ALLOW_THREADS 的 C 代码释放;ctypes 调用默认释放(这是 ctypes 快的关键);numpy 多数运算释放但小数组开销可能反噬。3) 验证方法?——ctypes time.sleep 实验(Q577 本题)、对比纯 Python 等价循环的墙钟时间;用 time.process_time 分辨 CPU 等待。4) 生产陷阱?——期望「C 扩展自动并行」;进程池数据序列化成本吃掉收益(Q565);free-threaded 实验版当生产默认(3.13 实验期,3.14 PEP 779 后仍非默认)。

---
