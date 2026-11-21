---
title: [Q051] Semaphore 限流
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q051 · Semaphore 限流

> 难度:★★☆ | 标签:threading, Semaphore, 限流

**问**:Semaphore 的典型用途是什么?举一个限制并发数的例子。

**答**:Semaphore 维护一个计数器,acquire 减一,release 加一,减到 0 就阻塞。最常见的用途是资源池/并发限流,比如最多同时 3 个线程访问下游服务。注意 `BoundedSemaphore` 在 release 超过初始值时报错,能捕获过度释放的 bug。

```python
# file: code/02_并发与网络工程/q051_semaphore.py
import threading
import time

sem = threading.BoundedSemaphore(3)  # 最多 3 个并发


def access(i: int) -> None:
    with sem:
        print(f"任务 {i} 获得名额, 当前并发上限内")
        time.sleep(0.2)
    print(f"任务 {i} 释放名额")


if __name__ == "__main__":
    threads = [threading.Thread(target=access, args=(i,)) for i in range(8)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("全部任务完成")
```

**追问**:
- Semaphore 和 BoundedSemaphore 怎么选?——优先 Bounded:release 超过初始值会抛 ValueError,能立刻暴露「多放令牌」的 bug;裸 Semaphore 会静默抬高并发上限。
- acquire 能带 timeout 吗?——可以,拿到许可返回 True、超时返回 False,适合「抢不到就走降级」的限流分支。
- 并发数设成多少合理?——按下游容量而不是本机,通常等于下游并发上限或连接池大小;设得比下游大等于没限流,下游先被打挂。

---
