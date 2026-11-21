---
title: [Q2124] fork 与线程的组合禁忌:继承来的死锁
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2124 · fork 与线程的组合禁忌:继承来的死锁

> 难度:★★★★ | 标签:fork, threading, 死锁, spawn

**问**:一个多线程进程里调用 fork,子进程会有什么定时炸弹?

**答**:fork 只复制调用它的那个线程,但复制整份内存——如果 fork 瞬间别的线程正持有互斥锁,子进程继承一把"永久锁":持有者线程不存在,谁也解不开。

- 实验里子进程对继承来的锁 acquire 超时,退出码 3 坐实死锁;

- 受影响的还包括条件变量、信号量、内存分配器的内部锁,stdlib 的 logging 也在列;

- 防线一:fork 前保证无其他线程持锁,实践中几乎无法保证;

- 防线二:混合场景一律 spawn 启动方式,不继承任何线程状态;

- 顺带规则:fork 后子进程只做 exec,别在复制的运行时里久留。

```python
# file: code/02_并发与网络工程/q2124_fork_with_threads.py
# -*- coding: utf-8 -*-
"""fork 与线程的组合禁忌: 子进程继承的是锁的瞬间状态。

- fork 只复制调用它的那个线程, 其他线程连同它们的栈一起消失;
- 但互斥锁是进程内存, 若 fork 瞬间别的线程正持锁, 子进程继承一把"永久锁";
- 子进程里没人能解锁, 一切等这把锁的代码全部死锁。
"""
import os
import sys
import threading
import time

lock = threading.Lock()
locked_evt = threading.Event()
release_evt = threading.Event()


def holder():
    lock.acquire()
    locked_evt.set()          # 通知主线程: 锁已被我持有, 可以 fork 了
    release_evt.wait()        # 模拟长临界区, 等 fork 实验做完
    lock.release()


def main():
    t = threading.Thread(target=holder, name="holder")
    t.start()
    locked_evt.wait()

    pid = os.fork()
    if pid == 0:
        # 子进程: 内存是拷贝, 锁处于 locked 状态, 持有者线程并不存在
        ok = lock.acquire(timeout=0.5)
        print("[child] 尝试拿锁:", "成功" if ok else "失败, 锁永久卡死",
              flush=True)
        os._exit(0 if ok else 3)

    # 父进程: 先让子进程跑完实验, 再放掉真正的持有者
    _, status = os.waitpid(pid, 0)
    code = os.waitstatus_to_exitcode(status)
    print("[parent] 子进程退出码:", code)
    if code == 3:
        print("[parent] 禁忌复现: fork 时别的线程持锁 -> 子进程死锁")
    release_evt.set()
    t.join()
    print("[parent] 父进程锁状态正常, 只有子进程继承了坏状态")

    # 正确姿势: fork 前保证没有其他线程持锁, 或改用 spawn 启动方式
    mp = __import__("multiprocessing")
    print("[parent] spawn 启动方式不继承任何线程状态, 是混合场景的安全选项",
          "| 平台默认:", mp.get_start_method())


if __name__ == "__main__":
    main()
```

**追问**:1) 为什么日志库在 fork 后会卡住?——logging 模块锁可能在 fork 瞬间被别的线程持有,子进程第一条日志就可能死锁。2) spawn 就完全安全吗?——它绕开继承问题,但要求可序列化的目标函数和 __main__ 保护,启动也慢;安全与开销是交易。3) 「子进程只做 exec」为什么是工程铁律?——fork 复制的运行时里满是死锁陷阱(锁/logging/分配器),exec 用全新进程镜像替换,继承问题一次性清空;Python 侧对应 multiprocessing 的 spawn/forkserver——「fork 后立即 exec 或干脆 spawn」。4) logging/内存分配器为什么在列?——logging 的模块级锁、malloc 的内部锁都可能在 fork 瞬间被其他线程持有;子进程第一条日志/第一次 malloc 就可能死锁——「看不见的锁」比业务锁更阴;forkserver 模式(池进程从干净 fork 服务器派生)是标准库给的解。5) 生产陷阱?——多线程服务 fork 子进程后继续跑 Python(继承死锁);fork 前不 stop 所有后台线程;子进程里用 logging(第一行就卡);macOS 3.8+ 默认 spawn 还手动改回 fork(埋雷);fork 后不 exec 还想「共享大状态」(用 mmap/管道替代)。

---
