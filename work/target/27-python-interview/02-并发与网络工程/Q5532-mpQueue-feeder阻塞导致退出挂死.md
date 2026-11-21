---
title: [Q5532] mp.Queue feeder 阻塞：进程退出挂死事故复盘
date: 2026-11-20
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5532 · mp.Queue feeder 阻塞：进程退出挂死事故复盘

> 难度:★★★★ | 标签:事故复盘, multiprocessing, Queue, feeder

**问**：子进程把任务结果 `put` 进 `multiprocessing.Queue` 后主进程再也不 take，程序退出时为什么可能永久挂死？feeder 线程是什么角色？`cancel_join_thread` 的代价是什么？

**答**：`mp.Queue` 的写端有个**后台 feeder 线程**：`put()` 只是把对象丢进进程内缓冲队列就返回（所以 put 几乎不阻塞），真正写管道的是 feeder。事故链：1) 主进程不消费，缓冲越积越大直到管道满，feeder 阻塞在 write；2) 进程退出时，非守护的 feeder 线程使 `Queue.close()` 后的解释器退出流程（join_thread）**永久等待**——进程挂着不退、 zombie 资源不释放；3) 表面现象是"任务都做完了，进程不退出"。修复矩阵：a) **治本**：修背压——put 前检查 `qsize`（不可靠但可用作告警）或改用有界信号（`semaphore`），确保消费速率 ≥ 生产速率（Q593/Q564 的通用背压）；b) **退出兜底**：`q.cancel_join_thread()` + `q.close()`，放弃未写出数据让进程立即退——**代价是缓冲区数据静默丢失**，只允许在"结果可丢（进度上报/日志）"的队列上用；c) 主进程侧保证 join 前先排空队列。取舍核心：cancel_join_thread 把"挂死"换成"丢数据"，必须按队列语义分类决策，写进代码注释。

```python
# file: code/02_并发与网络工程/q5532_feeder_hang.py
"""feeder 阻塞的演示(缩短版)与两种退出策略. macOS spawn 需 __main__ 守卫."""
import multiprocessing as mp
import os
import time

def producer(q, item_size: int, n: int) -> None:
    for i in range(n):
        q.put(bytes(item_size))      # put 立即返回, 实际写出在 feeder 线程
    print(f"[producer pid={os.getpid()}] put 完毕, feeder 可能仍在写")

def consumer(q, n: int) -> None:
    got = 0
    while got < n:
        q.get()
        got += 1

if __name__ == "__main__":           # macOS(spawn) 必需
    ctx = mp.get_context("spawn")

    # --- 场景 A: 正常背压(有消费者) -> 干净退出 ---
    q1 = ctx.Queue(maxsize=8)        # 有界: put 自带背压, feeder 不会无限积压
    p = ctx.Process(target=producer, args=(q1, 1024, 16))
    c = ctx.Process(target=consumer, args=(q1, 16))
    p.start(); c.start()
    c.join(timeout=10); p.join(timeout=10)
    print("场景A(有界+消费): p alive=", p.is_alive(), "c alive=", c.is_alive())
    c.terminate(); p.terminate()

    # --- 场景 B: 无消费者 + cancel_join_thread 退出兜底 ---
    q2 = ctx.Queue()
    p2 = ctx.Process(target=producer, args=(q2, 65536, 200))
    p2.start()
    time.sleep(0.3)
    # 若主进程此时退出且从不消费: feeder 阻塞在满管道上 -> join_thread 永久等
    # 兜底: 生产者侧对"可丢数据"队列声明放弃 join
    p2.terminate()                   # 演示用直接杀掉(真实事故是退出挂死)
    p2.join(timeout=3)
    print("场景B(无消费): terminated, alive=", p2.is_alive())
    print("结论: 可丢数据队列 -> cancel_join_thread(); 结果队列 -> 有界+消费速率保障")
```

**追问**：1) feeder 为什么要异步化写出？——把序列化+写管道的成本从业务线程挪到后台，put 调用方 O(1) 返回；代价正是"写成功与否不可见"，背压只能靠有界队列（put 在 maxsize 满时真阻塞）重建。2) `join_thread()`/`cancel_join_thread()` 与进程退出的顺序？——解释器退出时 Queue 的 finalize 会 join feeder（除非 cancel）；cancel 后 feeder 可能被中途杀死，半写的对象造成管道损坏，**读端可能读到坏数据**——所以 cancel 只配可丢语义。3) 为什么 mp.Queue 的 qsize()/empty() 不可靠？——sem_getvalue 平台差异与读端竞态，监控用途可以，逻辑判断不行。

## 背诵要点
- mp.Queue.put 只进本地缓冲，feeder 线程负责写管道；无消费时 feeder 阻塞，退出 join_thread 永久挂死。
- 治本=有界队列+消费速率保障；cancel_join_thread 是"可丢数据"队列的退出兜底，会静默丢数据。
- qsize/empty 不可靠，只用于监控不用作逻辑判断。

## 复盘追问
- 线上出现"任务跑完进程不退"，你的取证顺序是什么（feeder 栈、管道水位、队列句柄数）？
- 设计一个混合场景：进度上报可丢、结果不可丢，两类队列的退出协议分别怎么写？
