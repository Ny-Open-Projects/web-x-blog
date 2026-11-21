---
title: [Q049] Lock 与互斥
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q049 · Lock 与互斥

> 难度:★★☆ | 标签:threading, Lock, 竞态条件

**问**:演示一个没有加锁导致的竞态条件,并说明 Lock 如何解决。

**答**:如 `counter += 1` 并非原子操作,包含读、加、写三步,多线程交错执行会丢失更新。用 `threading.Lock` 把临界区包起来,同一时刻只有一个线程能进入。注意必须用 `with lock` 或 try/finally 保证释放。

```python
# file: code/02_并发与网络工程/q049_lock.py
import threading

counter = 0
N_THREADS = 8
N_INCR = 100_000


def unsafe_increment() -> None:
    global counter
    for _ in range(N_INCR):
        counter += 1  # 非原子: 读-加-写


lock = threading.Lock()


def safe_increment() -> None:
    global counter
    for _ in range(N_INCR):
        with lock:
            counter += 1


if __name__ == "__main__":
    threads = [threading.Thread(target=unsafe_increment) for _ in range(N_THREADS)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("无锁结果(通常小于期望值):", counter)

    counter = 0
    threads = [threading.Thread(target=safe_increment) for _ in range(N_THREADS)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("加锁结果:", counter)
```

**追问**:
- 为什么推荐 `with lock:` 而不是手动 acquire/release?——异常路径也能保证释放,等价 try/finally;手动 release 一旦临界区抛异常,锁永远不释放,后面所有线程饿死。
- Lock 能解决所有竞态吗?——只解决互斥;check-then-act 这类跨调用的复合逻辑即使每段都加锁,两段之间仍可能被插队,要把整个判断包进同一临界区。
- `acquire(timeout=1)` 用在什么场景?——有限等待后走降级/上报,是防「锁挂起拖垮整组线程」的最小手段。

---
