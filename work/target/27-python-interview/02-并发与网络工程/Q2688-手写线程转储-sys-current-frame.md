---
title: [Q2688] 手写线程转储:sys._current_frames 的糙版 py-spy
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2688 · 手写线程转储:sys._current_frames 的糙版 py-spy

> 难度:★★★ | 标签:线程转储, sys._current_frames, 排障

**问**:不发信号、不装工具,能不能用纯 Python 打一份线程转储?

**答**:能:sys._current_frames() 一次性给出所有线程此刻的栈顶帧,配合 threading.enumerate 对上线程名,每个线程打印它正停在哪一行。实测三个线程分别停在持锁睡眠、定时睡眠与忙等上,转储一目了然。局限也说清楚:只有 Python 帧、快照有微秒级时差、看不到 C 扩展内部——定位"卡在哪"足够,深挖要 py-spy。

- 转储是"现在进行时"的证据,定期转储对比才能看出卡死趋势;

- 读别的线程的 frame 是只读操作,安全;

- 忙等线程的栈顶在判断条件上,睡眠线程的栈顶在 sleep 里,模式要熟;

- faulthandler 是信号版转储,这个是进程内主动版,两者互补。

```python
# file: code/02_并发与网络工程/q2688_thread_dump.py
# -*- coding: utf-8 -*-
"""手写线程转储: sys._current_frames 的糙版 py-spy。

- sys._current_frames 给出所有线程"此刻"的栈顶帧快照;
- 配合 threading.enumerate 对上名字, 每个线程打印它正停在哪一行;
- 局限: 只有 Python 帧, 快照有微秒级时差, 但足够定位"卡在哪"。
"""
import os
import sys
import threading
import time
import traceback

done = threading.Event()


def stuck_on_lock():
    lock = threading.Lock()
    lock.acquire()
    time.sleep(3.0)                      # 持着锁睡觉: 现场最经典的病灶


def sleeping():
    while not done.is_set():
        time.sleep(0.1)


def spinning():
    x = 0
    while not done.is_set():
        x = (x + 7) % 1000003            # 忙等: 连让步都懒得让


def dump_threads():
    frames = sys._current_frames()       # 一次性取全体线程的栈顶帧
    print("=== Thread dump (%d threads) ===" % threading.active_count())
    for t in threading.enumerate():
        f = frames.get(t.ident)
        if f is None:
            continue
        stack = traceback.extract_stack(f)
        top = stack[-1]
        print("  %-14s daemon=%-5s -> %s:%d in %s"
              % (t.name, t.daemon, os.path.basename(top.filename),
                 top.lineno, top.name))
        for fr in stack[-3:-1]:         # 再带两帧上下文
            print("      ^ %s:%d in %s"
                  % (os.path.basename(fr.filename), fr.lineno, fr.name))


if __name__ == "__main__":
    ts = [threading.Thread(target=stuck_on_lock, name="lock-holder", daemon=True),
          threading.Thread(target=sleeping, name="idle-worker", daemon=True),
          threading.Thread(target=spinning, name="busy-worker", daemon=True)]
    for t in ts:
        t.start()
    time.sleep(0.3)                      # 让各线程进入典型状态
    dump_threads()
    done.set()
    for t in ts:
        t.join(timeout=1.0)
    print("要点: 转储是'现在进行时'的证据, 定期转储对比才能看出卡死趋势")
```

**追问**:1) 为什么栈顶偶尔指向奇怪的地方?——快照与打印之间线程在跑,帧是某一瞬间的,多打几份对齐看。2) GIL 会让转储卡住吗?——_current_frames 是 C 层原子操作,不需要拿 GIL 太久,线程再多也是毫秒级。3) 底层机制:快照能读到什么、读不到什么?——能读 Python 帧的 f_code/f_lineno/f_back 并还原调用链;读不到 C 扩展内部栈与原生 mutex 的持有者;线程恰在 C 调用(锁等待)里时,栈顶停在该 Python 调用行,提示"卡在这行附近"而非真正病灶。4) 生产陷阱?——单次快照当定论,要在时间轴上多打几份对比趋势;把 f_lineno 当精确卡点(它是字节码当前行,多语句行会偏移);私有 API 没做兜底,线程恰好退出时 ident 缺失直接炸监控。

---
