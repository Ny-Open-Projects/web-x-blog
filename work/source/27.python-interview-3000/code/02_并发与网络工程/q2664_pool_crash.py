# -*- coding: utf-8 -*-
"""池内崩溃毒化全池: 一个 worker 被杀, 整个池进入残局。

- 任务抛异常只毒化自己: 异常回传, 池继续可用;
- worker 进程被 SIGKILL 杀掉(退出码 -9): 池被判 broken;
- broken 池对在途与后续所有提交一律 BrokenProcessPool, 只能重建。
"""
import os
import signal
import time
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures.process import BrokenProcessPool


def slow_good(x):
    time.sleep(0.4)                      # 慢任务, 保证崩溃时在途
    return x * 2


def suicide(_):
    """模拟 worker 被外部 kill -9: 进程直接消失, 没有异常回传。"""
    os.kill(os.getpid(), signal.SIGKILL)


def status(f):
    if f.cancelled():
        return "cancelled"
    if f.done():
        exc = f.exception()
        return type(exc).__name__ if exc else "ok"
    return "pending"


if __name__ == "__main__":
    ex = ProcessPoolExecutor(max_workers=2)
    print("崩溃前正常任务:", ex.submit(slow_good, 1).result())

    pending = [ex.submit(slow_good, i) for i in (2, 3, 4, 5)]
    boom = ex.submit(suicide, 0)
    try:
        boom.result()
        print("竟然没炸")
    except BrokenProcessPool as e:
        print("崩溃任务:", type(e).__name__, "->", str(e)[:52])

    for f in pending:
        try:
            f.result(timeout=10)
        except (BrokenProcessPool, Exception) as e:
            pass                         # 在途与排队的任务一并被毒化
    print("在途 4 个任务的结局:", [status(f) for f in pending])

    try:
        ex.submit(slow_good, 9).result(timeout=10)
        print("崩溃后旧池竟然还能用")
    except BrokenProcessPool:
        print("崩溃后旧池: 继续提交也是 BrokenProcessPool -> 池已毒化")

    ex.shutdown(wait=False, cancel_futures=True)

    with ProcessPoolExecutor(max_workers=2) as ex2:   # 重建才是出路
        print("重建新池后:", ex2.submit(slow_good, 42).result())
