---
title: [Q047] 守护线程 daemon 的行为
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q047 · 守护线程 daemon 的行为

> 难度:★★☆ | 标签:threading, daemon

**问**:什么是守护线程?主线程退出时守护线程和非守护线程分别是什么命运?

**答**:设置 `daemon=True` 的线程是后台线程,主进程退出时不等待它们,直接终止(相当于被强行截断);非守护线程则会被主线程 join,进程必须等它们全部结束才退出。因此守护线程里不要持有文件、数据库连接等需要干净释放的资源。

```python
# file: code/02_并发与网络工程/q047_daemon_thread.py
import threading
import time


def heartbeat() -> None:
    while True:
        print("心跳...")
        time.sleep(0.1)


def task() -> None:
    time.sleep(0.5)
    print("task 完成")


if __name__ == "__main__":
    d = threading.Thread(target=heartbeat, daemon=True)
    t = threading.Thread(target=task, daemon=False)
    d.start()
    t.start()
    time.sleep(0.2)
    print("主线程即将退出, 守护线程被丢弃, 非守护线程会被 join")
    # 主线程结束时: task 线程会跑完, heartbeat 循环被直接终止
```

**追问**:
- 如何在主线程退出前优雅停掉守护线程?——用 `threading.Event`,`event.wait(timeout)` 作为循环条件,退出前 `event.set()`。
- 守护线程被截断时会发生什么?——finally 不保证执行、缓冲可能未刷盘;涉及事务与文件收尾的线程不要设 daemon。
- daemon 能中途修改吗?——必须在 start() 之前设置,启动后再改抛 RuntimeError。
- 不用守护线程怎么实现「主退出子也退」?——Event 通知 + 子线程定期检查,或把工作放队列由消费者感知哨兵退出。
