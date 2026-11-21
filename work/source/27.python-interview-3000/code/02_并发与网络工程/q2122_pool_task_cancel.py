# -*- coding: utf-8 -*-
"""进程池任务的优雅取消: Future.cancel 的生效窗口。

- 未开始的 pending 任务可 cancel; 已在跑的任务 cancel 返回 False, 只能等待;
- cancel 后的 future 状态是 CANCELLED, result 会抛 CancelledError;
- 批量取消时先留出在途任务, 取消排队者, 是进程池唯一体面的刹车。
"""
import multiprocessing
import os
import time
import concurrent.futures as cf

ctx = multiprocessing.get_context("fork")


def work(n):
    time.sleep(0.3)
    return n * 2


def main():
    ex = cf.ProcessPoolExecutor(max_workers=2, mp_context=ctx)
    try:
        futs = [ex.submit(work, i) for i in range(8)]
        time.sleep(0.1)            # 头两个任务已进入执行
        cancelled, pending = [], []
        for f in futs[2:]:
            (cancelled if f.cancel() else pending).append(f)
        print("排队任务取消成功:", len(cancelled), "个")
        print("已在跑无法取消:", len(pending), "个, 状态:",
              [f.running() for f in futs[:2]])
        kept = [f.result() for f in futs[:2]] + \
               [p.result() for p in pending]
        print("实际拿到结果:", kept)
        try:
            cancelled[0].result()
            print("意外: 取消的任务居然有结果")
        except cf.CancelledError:
            print("取消任务的 result 抛 CancelledError, 符合预期")
    finally:
        ex.shutdown(wait=True)


if __name__ == "__main__":
    main()
