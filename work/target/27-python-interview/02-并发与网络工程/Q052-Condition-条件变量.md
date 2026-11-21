---
title: [Q052] Condition 条件变量
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q052 · Condition 条件变量

> 难度:★★★ | 标签:threading, Condition, 等待通知

**问**:Condition 解决什么问题?wait 和 notify 为什么必须持有锁?

**答**:Condition 用于线程间等待"某条件成立",经典模型是生产者消费者。`wait()` 会先释放锁再挂起,被 notify 唤醒后重新抢锁,因此调用 wait/notify 前必须持有同一把锁;条件判断要用 while 而不是 if,防止虚假唤醒和唤醒后条件又失效。

```python
# file: code/02_并发与网络工程/q052_condition.py
import threading
import time

items: list[int] = []
cond = threading.Condition()


def consumer() -> None:
    with cond:
        while not items:
            print("consumer 无数据, 等待")
            cond.wait()
        print("consumer 取到", items.pop())


def producer() -> None:
    time.sleep(0.3)
    with cond:
        items.append(42)
        print("producer 放入 42")
        cond.notify()


if __name__ == "__main__":
    c = threading.Thread(target=consumer)
    p = threading.Thread(target=producer)
    c.start()
    p.start()
    c.join()
    p.join()
```

**追问**:
- notify 和 notify_all 的区别?——notify 只随机唤醒一个等待者,条件对所有线程都成立时用 notify_all,否则可能漏唤醒。
- 虚假唤醒是什么,while 怎么防?——等待者可能在未 notify 时醒来或条件又被改变;while 复查谓词,不满足继续 wait。
- Condition 能复用外部锁吗?——可以,`Condition(lock)` 传入已有 Lock/RLock,多条件共享一把锁协调。
- wait(timeout) 的返回值有什么用?——True 被通知、False 超时;超时分支同样要复查条件再决定行动。
