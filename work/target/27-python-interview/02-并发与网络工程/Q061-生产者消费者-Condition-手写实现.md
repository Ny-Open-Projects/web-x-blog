---
title: [Q061] 生产者消费者:Condition 手写实现
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q061 · 生产者消费者:Condition 手写实现

> 难度:★★★ | 标签:Condition, 生产者消费者

**问**:不使用 queue,用 Condition 手写一个有界缓冲的生产者消费者,考察对底层机制的理解。

**答**:核心是两个条件:缓冲区不满(生产者可放)和不空(消费者可取)。用一个 Condition 和 while 循环分别 wait/notify,放完 notify 消费者,取完 notify 生产者。这题面试官想看 while 判断条件、notify 对象是否正确。

```python
# file: code/02_并发与网络工程/q061_producer_consumer_cond.py
import threading
import time

buffer: list[int] = []
MAX_SIZE = 3
cond = threading.Condition()


def producer(pid: int, count: int) -> None:
    for i in range(count):
        with cond:
            while len(buffer) >= MAX_SIZE:
                cond.wait()  # 缓冲区满, 等消费者
            item = pid * 100 + i
            buffer.append(item)
            print(f"生产者 {pid} 放入 {item}, 缓冲区 {buffer}")
            cond.notify_all()
        time.sleep(0.05)


def consumer(cid: int, total: int) -> None:
    consumed = 0
    while consumed < total:
        with cond:
            while not buffer:
                cond.wait()  # 缓冲区空, 等生产者
            item = buffer.pop(0)
            consumed += 1
            print(f"消费者 {cid} 取出 {item}, 缓冲区 {buffer}")
            cond.notify_all()


if __name__ == "__main__":
    ps = [threading.Thread(target=producer, args=(p, 3)) for p in range(2)]
    cs = [threading.Thread(target=consumer, args=(c, 3)) for c in range(2)]
    for t in ps + cs:
        t.start()
    for t in ps + cs:
        t.join()
    print("完成, 缓冲区剩余:", buffer)
```

**追问**:
- 为什么条件判断必须用 while 而不是 if?——notify 后条件可能被其他线程抢先改变,或存在虚假唤醒;while 保证醒来后复查谓词。
- notify 应该在持锁时还是释放后调用?——标准做法持锁 notify;先释放再 notify 有丢失唤醒窗口,是初学者高频错误。
- 缓冲区选 list 还是 deque?——deque 的 append/popleft 是 O(1) 且单操作线程安全;list 的 pop(0) 是 O(n),数据量大时性能差一个量级。

---
