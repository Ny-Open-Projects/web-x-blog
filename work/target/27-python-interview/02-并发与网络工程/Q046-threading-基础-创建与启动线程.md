---
title: [Q046] threading 基础:创建与启动线程
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q046 · threading 基础:创建与启动线程

> 难度:★☆☆ | 标签:threading, 基础

**问**:Python 里如何创建并启动一个线程?Thread 的 start 和直接调用 run 有什么区别?

**答**:两种常用方式:传入 target 函数,或继承 Thread 重写 run。`start()` 会向操作系统申请新线程并由其执行 run;直接调用 `run()` 只是在当前线程里执行普通函数,没有任何并发。主线程结束默认不等子线程,需要 `join()` 等待。

```python
# file: code/02_并发与网络工程/q046_thread_basic.py
import threading
import time


def worker(name: str) -> None:
    print(f"线程 {name} 启动, thread_id={threading.get_ident()}")
    time.sleep(0.2)
    print(f"线程 {name} 结束")


class MyThread(threading.Thread):
    def run(self) -> None:
        worker(self.name)


if __name__ == "__main__":
    t1 = threading.Thread(target=worker, args=("t1",), name="worker-1")
    t2 = MyThread(name="worker-2")
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(f"活跃线程数: {threading.active_count()}")
```

**追问**:
- 子线程抛出的异常会影响主线程吗?——不会直接让主线程退出,异常只在子线程内打印 traceback;可用 `threading.excepthook` 全局接管。
- `start()` 和直接调用 `run()` 差在哪?——start 请求操作系统创建线程并异步执行 run;直接调 run 是当前线程里的普通函数调用,毫无并发。
- threading.excepthook 怎么用?——接收 (args) 含 exc_type/exc_value/thread,统一打日志上报,替代在每个线程里手写 try/except。
- 线程启动顺序可控吗?——不可控,start 之后由 OS 调度;需要顺序就靠 join、Event 或队列编排。
