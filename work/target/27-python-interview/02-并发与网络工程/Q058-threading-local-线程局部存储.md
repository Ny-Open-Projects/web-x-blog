---
title: [Q058] threading.local 线程局部存储
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q058 · threading.local 线程局部存储

> 难度:★★☆ | 标签:threading, threading.local

**问**:threading.local 的作用是什么?典型使用场景?

**答**:threading.local 为每个线程提供独立的变量副本,写入互不可见,天然线程安全。典型场景是每线程复用一个数据库连接、请求上下文。注意它不隔离协程——asyncio 里所有任务共享同一线程,需要用 contextvars.ContextVar。

```python
# file: code/02_并发与网络工程/q058_thread_local.py
import threading
import time

local_data = threading.local()


def worker(name: str) -> None:
    local_data.value = name  # 每个线程写自己的副本
    time.sleep(0.1)
    print(f"{threading.current_thread().name} 读到自己的 value: {local_data.value}")


if __name__ == "__main__":
    threads = [threading.Thread(target=worker, args=(f"worker-{i}",)) for i in range(3)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
```

**追问**:
- threading.local 的实现原理?——内部以线程为 key 的字典,每个线程首次访问时初始化自己的副本,访问互不可见。
- 为什么协程下要换 ContextVar?——asyncio 所有任务在同一线程轮转,threading.local 变成全体共享;`contextvars.ContextVar` 按上下文隔离,任务切换时正确生效。
- threading.local 有什么内存坑?——副本随线程存活,线程池里长期存放大对象会驻留整个池生命周期;只放连接、请求上下文这类轻量资源。

---
