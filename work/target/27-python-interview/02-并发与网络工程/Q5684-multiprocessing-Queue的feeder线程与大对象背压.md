---
title: "[Q5684] multiprocessing.Queue 的 feeder 线程与大对象背压"
date: 2026-11-23
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5684 · multiprocessing.Queue 的 feeder 线程与大对象背压

难度：P7 ｜ 标签：multiprocessing、Queue、feeder、pickle、背压、共享内存

**问**：`q.put(b"...50MB...")` 为什么毫秒级就返回了，数据到底存哪、谁在写管道？为什么 `close()` + `join_thread()` 会卡死？什么时候 `cancel_join_thread()` 会丢数据？大对象跨进程传输，除了 Queue 还有什么更合适的路子？

**答**：
结论：`multiprocessing.Queue.put` 只做两件事——pickle 序列化后 append 进进程内的 deque，然后通知后台的 **feeder 线程**去写管道。真正的传输在 feeder 里，受管道容量（本机 64KiB）和读端消费速度约束，所以 put 的耗时不随对象大小增长（5MB 约 3-5ms，实测）。没有读端时 feeder 阻塞在 `write`，`join_thread()` 就在等这个线程，于是永久卡住；`cancel_join_thread()` 让进程退出时**不等** feeder，未写完的数据直接丢——它是"我知道会丢，但我要立刻退出"的逃生门。

取舍：Queue 传大对象有三重税：pickle（CPU）、父进程内存里同时存在原对象和序列化副本（峰值）、以及不可见的背压（put 不阻塞，内存却在涨）。替代方案：a) `shared_memory` 传 numpy/bytes 块，只传句柄；b) 写临时文件/对象存储传路径；c) 有时间就用 `multiprocessing.Pipe` + 自己的帧协议（仍然受背压）。选择标准是"数据量 × 频率"：小消息用 Queue，大块用共享内存。

实战：事故形态是"跑批进程 put 了 200 个 10MB 结果后调用 join_thread 收尾，任务永远不结束"，或者"父进程被 kill 后子进程拿到的结果少了一半"。下面演示三件事：有读者时 put/close/join_thread 全部流畅；无读者时 put 依然瞬间返回但 join_thread 卡住；`cancel_join_thread()` 的语义。

```python
import multiprocessing as mp
import threading
import time

SIZE = 5_000_000


def consume(q, out):
    out.value = len(q.get())


if __name__ == "__main__":
    # A) 有人读：put/close/join_thread 全都不阻塞
    q = mp.Queue()
    out = mp.Value("l", 0)
    p = mp.Process(target=consume, args=(q, out))
    p.start()
    t0 = time.perf_counter()
    q.put(b"y" * SIZE)
    put_ms = (time.perf_counter() - t0) * 1000
    q.close()
    t1 = time.perf_counter()
    q.join_thread()
    flush_ms = (time.perf_counter() - t1) * 1000
    p.join()
    print(f"[A] 有读者: put={put_ms:.2f}ms flush={flush_ms:.1f}ms 收到={out.value}B")

    # B) 没有读者：put 仍然瞬间返回，但 close+join_thread 卡在管道背压
    q2 = mp.Queue()
    t0 = time.perf_counter()
    q2.put(b"z" * SIZE)
    put_ms = (time.perf_counter() - t0) * 1000
    q2.close()
    th = threading.Thread(target=q2.join_thread, daemon=True)
    th.start()
    th.join(0.5)
    print(f"[B] 无读者: put={put_ms:.2f}ms join_thread 0.5s 仍未返回={th.is_alive()}")

    q2.cancel_join_thread()   # 退出时不等 feeder：管道里没写完的数据直接丢
    print("[C] cancel_join_thread：进程可立刻退出，代价是可能丢数据")
```

**追问一**：为什么 `qsize()` 不可靠？—— 它返回的是"已 put 未 get"的近似值，读写分属不同进程、没有全局一致性；macOS 上 SemLock 的 `sem_getvalue` 不可用，直接 `NotImplementedError`。要监控积压就用应用层计数器（put/get 各打点）或 `shared_memory` 里的原子计数。

**追问二**：为什么 feeder 线程是 daemon，还会有 join_thread？—— daemon 保证"父进程不会被它阻塞退出"，join_thread 提供"显式等待落盘"的手段。两者组合的语义是：默认不丢数据（退出时 join），想立刻退出就显式放弃（cancel）。这也解释了为什么在 `Pool`/`ProcessPoolExecutor` 里 panic 退出经常丢任务——父进程没机会 join。

## 背诵要点
- `Queue.put` 只入本地 deque + pickle，由 feeder 线程异步写管道；put 耗时与对象大小无关。
- 无读端时 feeder 卡在 64KiB 管道上，`join_thread()` 永久等待；`cancel_join_thread()` 用丢数据换立即退出。
- 大对象走 Queue 有三重税（pickle、内存副本、隐形背压），优先 shared_memory / 传路径。

## 复盘追问
- put 50MB 立刻返回但收尾卡死，如何解释 feeder 与管道背压？（deque、feeder、64KiB、join_thread）
- 什么时候可以接受 cancel_join_thread 的丢数据？如何设计"至少一次"语义？（无消费者确认、ack 机制）
