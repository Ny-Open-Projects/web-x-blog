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
