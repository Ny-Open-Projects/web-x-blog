---
title: [Q064] 进程间通信:Queue
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q064 · 进程间通信:Queue

> 难度:★★★ | 标签:multiprocessing, Queue, IPC

**问**:multiprocessing.Queue 和 queue.Queue 的区别?为什么它能在进程间传数据?

**答**:multiprocessing.Queue 底层通过管道 + pickle + 一个 feeder 线程把对象序列化后在进程间搬运,是进程安全的;queue.Queue 只在进程内的线程间共享。注意子进程里 get 到的是父进程数据的深拷贝(经 pickle),修改不会回传;大量数据用共享内存更高效。

```python
# file: code/02_并发与网络工程/q064_mp_queue.py
import multiprocessing


def producer(q: multiprocessing.Queue) -> None:
    for i in range(5):
        q.put(f"item-{i}")
    q.put(None)


def consumer(q: multiprocessing.Queue) -> None:
    while True:
        item = q.get()
        if item is None:
            break
        print(f"消费 {item}")


if __name__ == "__main__":
    q: multiprocessing.Queue = multiprocessing.Queue()
    p = multiprocessing.Process(target=producer, args=(q,))
    c = multiprocessing.Process(target=consumer, args=(q,))
    p.start()
    c.start()
    p.join()
    c.join()
    print("IPC 完成")
```

**追问**:
- 子进程修改从 Queue 拿到的对象,父进程能看到吗?——看不到,pickle 反序列化是副本;需要回传就 put 回去,或用 shared_memory。
- feeder 线程是什么,有什么坑?——put 的对象先进内部缓冲,由 feeder 线程序列化写管道;put 后立即 join 子进程可能因缓冲未刷而死锁,需先处理缓冲或 cancel_join_thread。
- 大对象走 Queue 的瓶颈在哪?——pickle 序列化加管道带宽;大数组改 shared_memory 或写文件传路径。
- qsize() 可靠吗?——macOS 上 NotImplementedError,Unix 上也只是近似值;不能拿它做同步与背压判断。
