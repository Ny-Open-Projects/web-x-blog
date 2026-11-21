---
title: [Q063] 进程池 multiprocessing.Pool
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q063 · 进程池 multiprocessing.Pool

> 难度:★★☆ | 标签:multiprocessing, Pool

**问**:multiprocessing.Pool 的 map/apply_async 有什么区别?进程池大小怎么定?

**答**:`map` 是批量阻塞式,语义贴近内置 map;`apply_async` 提交单个任务返回 AsyncResult,可用回调,配合 close+join 收尾。池大小经验值:CPU 密集聚到 CPU 核数,IO 密集可放宽。注意传入子进程的参数和返回值必须可 pickle。

```python
# file: code/02_并发与网络工程/q063_pool.py
import multiprocessing
import os
import time


def square(n: int) -> int:
    return n * n


def slow_square(n: int) -> int:
    time.sleep(0.1)
    print(f"子进程 {os.getpid()} 处理 {n}")
    return n * n


if __name__ == "__main__":
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(square, range(10))
        print("map 结果:", results)

        async_results = [pool.apply_async(slow_square, (i,)) for i in (3, 5, 7)]
        print("异步提交后可先做别的事")
        print("apply_async 结果:", [r.get() for r in async_results])
    print("with 退出即 pool.close + join")
```

**追问**:
- map、imap、imap_unordered 的区别?——map 阻塞返回全量有序结果;imap 惰性按提交序产出,imap_unordered 按完成序,大任务流用后者控内存、先到先处理。
- Pool 的回调在哪个线程执行?——结果处理线程,回调里抛异常只会打印不影响任务;回调里不要做重活或再碰池。
- 池内任务抛异常在哪里暴露?——`apply_async(...).get()` 与 map 迭代时重新抛出;不取结果就无人知晓,收尾必须统一 get。

---
