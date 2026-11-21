---
title: [Q057] IO 密集与 CPU 密集的选型
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q057 · IO 密集与 CPU 密集的选型

> 难度:★★★ | 标签:GIL, 架构选型

**问**:CPU 密集和 IO 密集任务分别选什么并发模型?

**答**:CPU 密集:用 multiprocessing 或 ProcessPoolExecutor,绕开 GIL 获得真并行;也优先检查 NumPy/Pandas 这类能释放 GIL 的 C 扩展。IO 密集:线程(threading/ThreadPoolExecutor)或协程(asyncio)都行,连接量大(成百上千)时协程内存和切换开销远小于线程。混合型任务可拆分:CPU 部分进进程池,IO 部分进线程或协程。

```python
# file: code/02_并发与网络工程/q057_io_cpu.py
import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor


def io_task(i: int) -> int:
    time.sleep(0.2)  # 模拟网络 IO
    return i


def cpu_task(n: int) -> int:
    return sum(i * i for i in range(n))


if __name__ == "__main__":
    start = time.perf_counter()
    with ThreadPoolExecutor(max_workers=8) as pool:
        list(pool.map(io_task, range(8)))
    print(f"IO 密集 + 线程池: {time.perf_counter() - start:.2f}s")

    start = time.perf_counter()
    with ThreadPoolExecutor(max_workers=4) as pool:
        list(pool.map(lambda n: cpu_task(n), [2_000_000] * 4))
    print(f"CPU 密集 + 线程池: {time.perf_counter() - start:.2f}s (GIL 下串行)")

    start = time.perf_counter()
    with ProcessPoolExecutor(max_workers=4) as pool:
        list(pool.map(cpu_task, [2_000_000] * 4))
    print(f"CPU 密集 + 进程池: {time.perf_counter() - start:.2f}s (真并行)")
```

**追问**:
- 怎么判断瓶颈到底是 CPU 还是 IO?——看 CPU 利用率、iowait、上下文切换次数,再用 profile 定位;先测量后选模型,不凭感觉。
- 进程池开多大?——CPU 密集约等于物理核数,IO 混合可到 2 倍核;再大只增加调度和序列化开销。
- 协程里跑 CPU 密集会发生什么?——事件循环被占住,所有协程停摆;要么拆分让出(`await asyncio.sleep(0)`),要么丢进程池。

---
