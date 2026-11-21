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
