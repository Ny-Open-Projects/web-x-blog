# -*- coding: utf-8 -*-
"""BoundedSemaphore 的超额归还防线: 普通 Semaphore 的计数会漂。

- 普通 Semaphore 只是个计数器, release 多调一次计数就涨上去;
- 计数从 1 漂到 2 后, 两个线程能同时进入"单槽"临界区, 不变量被打破;
- BoundedSemaphore 在 release 超过初始值时抛 ValueError, 把 bug 挡在原地。
"""
import threading
import time


def hammer(sem, barrier, conc, peak, lock):
    barrier.wait()
    sem.acquire()
    with lock:
        conc[0] += 1
        peak[0] = max(peak[0], conc[0])
    time.sleep(0.05)                 # 临界区有点工作量, 让并发重叠可观测
    with lock:
        conc[0] -= 1
    sem.release()


def run_two_workers(sem):
    """两个 worker 同时进临界区, 返回观测到的最大并发数。"""
    barrier = threading.Barrier(2)
    conc, peak, lock = [0], [0], threading.Lock()
    ts = [threading.Thread(target=hammer, args=(sem, barrier, conc, peak, lock))
          for _ in range(2)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    return peak[0]


if __name__ == "__main__":
    # 阶段一: 健康 Semaphore, 单槽同一时刻只放一人
    healthy = threading.Semaphore(1)
    print("健康 Semaphore(1) 的最大并发:", run_two_workers(healthy))

    # 阶段二: 普通 Semaphore 被多 release 一次, 计数漂到 2
    plain = threading.Semaphore(1)
    plain.release()                  # 多余的一次归还: 计数 1 -> 2
    peak = run_two_workers(plain)
    print("超额 release 后, '单槽'临界区最大并发:", peak)
    print("不变量是否被打破:", peak > 1)

    # 阶段三: BoundedSemaphore 拒绝超额归还
    bounded = threading.BoundedSemaphore(1)
    try:
        bounded.release()            # 多余的一次归还
        print("BoundedSemaphore 竟然放行了超额 release")
    except ValueError as e:
        print("BoundedSemaphore 抓到超额归还:", e)
    print("BoundedSemaphore 保护下最大并发:", run_two_workers(bounded))
