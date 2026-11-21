# -*- coding: utf-8 -*-
"""无锁计数的尝试与实测: GIL 下的真相。

- counter += 1 是读改写三步, GIL 只保证单字节码原子, 丢更新照样发生;
- list.append 这类单调用在 CPython 里是原子的, 可以当事件台账用;
- 纯 Python 没有真正的无锁原子自增: 要么加锁, 要么分片, 要么换成原子单调用。
"""
import sys
import threading
import time


def bump_naive(counter, n):
    for _ in range(n):
        counter["v"] += 1     # dict 读改写: 非原子


def bump_atomic_append(tally, n):
    for _ in range(n):
        tally.append(1)       # CPython 单调用原子: 一次事件一次 append


def bump_sharded(shards, idx, n):
    for _ in range(n):
        shards[idx] += 1      # 每线程写自己的槽位: 无争用


def run(fn, args_list):
    ts = [threading.Thread(target=fn, args=a) for a in args_list]
    t0 = time.monotonic()
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    return time.monotonic() - t0


def main():
    sys.setswitchinterval(0.000001)   # 放大线程切换频率, 复现竞态窗口
    NT, PER = 8, 50000
    total = NT * PER

    counter = {"v": 0}
    dur1 = run(bump_naive, [(counter, PER)] * NT)
    print("naive +=  : 期望 %d 实得 %d, 丢失 %d (%.2fs)" %
          (total, counter["v"], total - counter["v"], dur1))

    tally = []
    dur2 = run(bump_atomic_append, [(tally, PER)] * NT)
    print("append 台账: 期望 %d 实得 %d, 丢失 %d (%.2fs)" %
          (total, len(tally), total - len(tally), dur2))

    shards = [0] * NT
    dur3 = run(bump_sharded, [(shards, i, PER) for i in range(NT)])
    print("分片聚合 : 期望 %d 实得 %d, 丢失 %d (%.2fs)" %
          (total, sum(shards), total - sum(shards), dur3))

    print("结论: += 丢更新, append 原子可当计数, 分片无争用且正确")


if __name__ == "__main__":
    main()
