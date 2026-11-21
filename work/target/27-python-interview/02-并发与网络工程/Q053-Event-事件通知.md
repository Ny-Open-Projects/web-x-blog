---
title: [Q053] Event 事件通知
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q053 · Event 事件通知

> 难度:★☆☆ | 标签:threading, Event

**问**:Event 和 Condition 的区别?举一个 Event 的典型用法。

**答**:Event 是一个全局布尔开关:`set()` 置位、`clear()` 复位、`wait()` 阻塞到置位。它比 Condition 简单,适合"一次性广播"场景,如优雅停机信号、初始化完成通知;需要复杂条件判断时才用 Condition。

```python
# file: code/02_并发与网络工程/q053_event.py
import threading
import time

stop_event = threading.Event()
ready_event = threading.Event()


def worker() -> None:
    print("worker 启动, 等待就绪信号")
    ready_event.wait(timeout=2)
    print("worker 收到就绪信号, 开始干活")
    while not stop_event.is_set():
        time.sleep(0.1)
    print("worker 收到停止信号, 退出")


if __name__ == "__main__":
    t = threading.Thread(target=worker)
    t.start()
    time.sleep(0.2)
    ready_event.set()
    time.sleep(0.5)
    stop_event.set()
    t.join()
```

**追问**:
- Event 和 Condition 的本质区别?——Event 只有一个布尔状态、面向「发生了没」;Condition 管理任意条件谓词和等待队列。一次性广播用 Event,复杂条件用 Condition。
- `event.wait(timeout)` 的返回值怎么用?——True 表示被置位,False 表示超时;循环体里用它实现「等退出信号 + 周期巡检」。
- Event 自身线程安全,业务还用加锁吗?——加不加取决于业务:单次读写状态安全,但「检查 Event 再修改共享数据」的复合逻辑仍要锁。

---
