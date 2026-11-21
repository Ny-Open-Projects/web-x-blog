---
title: [Q2385] tryLock 的忙等边界:省延迟还是烧 CPU
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2385 · tryLock 的忙等边界:省延迟还是烧 CPU

> 难度:★★☆ | 标签:tryLock, 自旋, 忙等

**问**:lock.acquire(blocking=False) 拿不到就返回 False,用它写自旋重试,什么时候划算?

**答**:自旋把"睡眠等待"换成"原地重试",换来的是零切换延迟和即时抢锁,代价是烧 CPU。

- 实测重争用场景:纯自旋的进程 CPU 消耗是阻塞等待的几十倍,墙钟还更慢;

- 自旋的收益窗口在锁的剩余持有时间极短时:一次尝试就拿到,省掉了睡与醒的往返;

- 折中配方是自旋加退避:失败若干次后 time.sleep 一小口,把 CPU 让给持有者,实测 CPU 消耗远低于纯自旋;

- 结论:临界区极短且核数富余才考虑自旋,默认用阻塞等待,别手痒。

```python
# file: code/02_并发与网络工程/q2385_tryacquire_spin.py
# -*- coding: utf-8 -*-
"""tryLock 的忙等边界: acquire(False) 自旋省的是延迟, 烧的是 CPU。

- 非阻塞 acquire 拿不到立即返回 False, 自旋重试把等待变成计算;
- 锁很快被释放时, 自旋省下线程切换, 可能更划算;
- 锁迟迟不释放时, 自旋白烧 CPU, 阻塞等待才是对的, 边界就在持锁时长。
"""
import threading
import time

lock = threading.Lock()


def hold_for(ms):
    """持锁做一小段工作, 用睡眠模拟, 不依赖机器快慢。"""
    lock.acquire()
    try:
        time.sleep(ms / 1000.0)
    finally:
        lock.release()


def run_strategy(name, spin, n_threads=4, iters=40):
    barrier = threading.Barrier(n_threads)
    cpu0 = time.process_time_ns()
    t0 = time.monotonic()

    def worker():
        barrier.wait()
        for _ in range(iters):
            if spin is None:
                lock.acquire()
                try:
                    time.sleep(0.0005)
                finally:
                    lock.release()
            else:
                spins = 0
                while not lock.acquire(blocking=False):
                    spins += 1
                    if spin and spins % spin == 0:
                        time.sleep(0.0005)   # 每自旋 spin 次小憩一下
                try:
                    time.sleep(0.0005)
                finally:
                    lock.release()

    threads = [threading.Thread(target=worker) for _ in range(n_threads)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    cpu_ms = (time.process_time_ns() - cpu0) / 1e6
    wall_ms = (time.monotonic() - t0) * 1000
    print("%-12s 墙钟 %6.1fms, 进程 CPU %6.1fms" % (name, wall_ms, cpu_ms))
    return cpu_ms


def main():
    print("场景: 无间隔连抢, 持锁 0.5ms, 4 线程争用")
    cpu_block = run_strategy("阻塞等待", spin=None)
    cpu_back = run_strategy("自旋+退避", spin=8)
    cpu_pure = run_strategy("纯自旋", spin=0)
    print("纯自旋 CPU 是阻塞等待的 %.1f 倍" % (cpu_pure / max(cpu_block, 0.1)))
    assert cpu_pure > 1.5 * cpu_block, "重争用下纯自旋的 CPU 消耗应显著更高"


if __name__ == "__main__":
    main()
```

**追问**:1) pthread_mutex_trylock 与这里的 acquire(False) 等价吗?——语义等价,但 CPython 之下自旋抢的还是 GIL 之后的锁,收益比原生线程更小。2) 自旋线程会拖慢持锁者吗?——会,自旋消耗 GIL 时间片,持锁者被切换推迟,临界区反而拉长,这就是自旋的反噬。3) 自旋的反噬机制?——自旋线程消耗 GIL 时间片,持锁者被切换推迟,临界区反而拉长,其他自旋者更加抢不到——「自旋拖慢持锁者」是正反馈恶化;重争用下墙钟更慢+CPU 几十倍(实测),这就是「默认阻塞等待」的依据。4) 自旋+退避的折中配方怎么调参?——先固定次数自旋(利用「临界区极短」的窗口),失败后指数退避让出 GIL;参数按持锁时长分布调:P99 持锁 < 切换开销时自旋才可能赢——「持锁时长分布」是唯一的选型依据(Q2388 的测量壳)。5) 生产陷阱?——纯自旋默认化(重争用 CPU 爆炸);自旋线程拖慢持锁者(见原问);把 acquire(False) 当 pthread trylock 宣传性能(GIL 下收益更小);自旋无上限(活锁);核数不足时自旋(没有空闲核,自旋纯亏)。

---
