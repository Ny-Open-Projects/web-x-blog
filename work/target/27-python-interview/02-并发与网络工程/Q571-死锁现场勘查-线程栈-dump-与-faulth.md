---
title: [Q571] 死锁现场勘查:线程栈 dump 与 faulthandler
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q571 · 死锁现场勘查:线程栈 dump 与 faulthandler

> 难度:★★★★ | 标签:死锁排查, faulthandler, 运维

**问**:线上程序卡死了,怀疑死锁,怎么在不重启的情况下拿到证据?

**答**:向进程发 `SIGABRT` 之外的首选是 faulthandler:启动时注册 `faulthandler.register(signal.SIGUSR1)`,卡死时 `kill -USR1 <pid>` 就会把所有线程的 Python 栈打到日志,能看到每个线程停在哪个 acquire 上;配合 py-spy dump 可以看到 C 层。没有预留信号处理时,`faulthandler.dump_traceback_later(timeout, exit=True)` 当兜底保险丝。拿到栈后按"两个线程互相持有对方需要的锁"的模式比对即可定位锁对。预防端:锁排序 + acquire 超时 + 全局锁注册表。

```python
# file: code/02_并发与网络工程/q571_deadlock_dump.py
import faulthandler
import threading
import time

lock_a = threading.Lock()
lock_b = threading.Lock()


def t1() -> None:
    with lock_a:
        time.sleep(0.2)      # 给 t2 时间拿到 lock_b
        with lock_b:         # 死锁点
            print("t1 不可能到这里")


def t2() -> None:
    with lock_b:
        time.sleep(0.2)
        with lock_a:
            print("t2 不可能到这里")


if __name__ == "__main__":
    faulthandler.enable()
    a = threading.Thread(target=t1, name="T1")
    b = threading.Thread(target=t2, name="T2")
    a.start()
    b.start()
    time.sleep(1.0)  # 此刻两个线程已互相卡死
    print("=== 模拟 kill -USR1: dump 所有线程栈 ===")
    with open("/tmp/q571_dump.txt", "w") as f:
        faulthandler.dump_traceback(file=f, all_threads=True)
    print(open("/tmp/q571_dump.txt").read())
    print("栈里能看到 T1 停在 lock_b.acquire, T2 停在 lock_a.acquire")
    import os
    os._exit(0)  # 演示结束, 真实场景这一步由运维强制重启替代
```

**追问**:1) dump 里两把锁名字一样怎么区分?——栈帧会显示 acquire 的调用行号,结合锁 ID(threading.Lock 对象地址)与代码行对照即可分清是哪一对锁构成的环。2) 现场勘查工具链?——faulthandler.dump_traceback_later 定时(Q1836)/SIGUSR1 触发;py-spy dump 无侵入;sys._current_frames 编程式抓取;每帧的锁持有信息结合日志。3) 死锁的四要素与对应解?——互斥/持有等待/不可剥夺/循环等待;破坏「持有等待」(一次性拿全)或「循环等待」(全局锁序,Q572)。4) 生产陷阱?——死锁只重启不归因;锁对象无名字(日志不可读);等待无超时让死锁变成「卡死」而不是「报错」。

---
