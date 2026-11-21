---
title: [Q2360] deque 的线程安全边界
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2360 · deque 的线程安全边界

> 难度:★★★★☆ | 标签:deque, 线程安全, 并发

**问**:都说 deque 线程安全,那迭代中修改为什么还会 RuntimeError?边界到底在哪?

**答**:准确的表述是:deque 的单个 append/appendleft/popleft/pop 操作是原子的(C 层加 GIL 保证),多生产者多消费者各自调用这些方法不会丢数据,所以它能当轻量任务队列;但「安全」到此为止——组合操作(先检查再操作)、rotate、remove 没有原子性,迭代过程中另一线程修改队列会让迭代器当场失效抛 RuntimeError: deque mutated during iteration。这个边界决定了选型:单方法收发用 deque 够了;需要「非空才取」「带超时等待」「任务完成通知」这类复合语义,用 queue.Queue,它为并发而生,锁、条件变量、统计都内置。还有一点容易忽略:用 while True 配 try popleft 消费,空队列靠 IndexError 收尾,是 deque 队列的标准退出姿势。

```python
# file: code/01_语言核心与底层/q2360_deque_thread_safety.py
"""deque 的线程安全边界:单端操作原子,组合操作与迭代不保。"""
import threading
from collections import deque

if __name__ == "__main__":
    q = deque()

    def producer():
        for i in range(1000):
            q.append(i)

    threads = [threading.Thread(target=producer) for _ in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("4 线程并发 append 无丢失:", len(q) == 4000)

    task_q = deque(range(600))

    def worker():
        while True:
            try:
                task_q.popleft()
            except IndexError:
                return

    workers = [threading.Thread(target=worker) for _ in range(3)]
    for w in workers:
        w.start()
    for w in workers:
        w.join()
    print("并发消费后清空:", len(task_q) == 0)

    d = deque(range(3))
    try:
        for v in d:
            d.append(v)
    except RuntimeError as exc:
        print("迭代中被修改:", exc)
```

**追问**:1) 为什么官方文档说 deque 的 append/popleft 原子却仍建议 queue.Queue?——deque 只提供「操作原子」,没有阻塞等待与优雅关闭;生产者消费者模型需要「等活干」的语义,Queue 的 get(block=True) 与 task_done/join 才是完整方案。2) 原子性的来源?——GIL 下 deque 两端操作是单条 C 调用,不被字节码边界打断;但「检查再操作」复合操作仍要自己加锁(Q2360 级别的心智)。3) 完整方案要素?——阻塞等待(get 阻塞省轮询)、容量背压(put 阻塞)、task_done/join 排空、哨兵关闭(Q1282 哨兵);Queue 全有。4) 生产陷阱?——自建「锁 + deque」轮询烧 CPU;忘 join 排空丢任务;无限 deque 当无界队列内存爆。
