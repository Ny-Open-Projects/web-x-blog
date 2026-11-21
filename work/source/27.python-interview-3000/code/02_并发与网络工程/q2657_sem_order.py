# -*- coding: utf-8 -*-
"""Semaphore 的唤醒顺序实测: 等待者按什么顺序拿到票。

- threading.Semaphore 内部是 Condition + 计数器, 唤醒走 waiters 队列;
- 实测: 全员先在栅栏前列队睡在 acquire 上, 再放票, 记录获票顺序;
- 多轮统计: CPython 下接近 FIFO, 但这是实现细节, 不是语言承诺。
"""
import threading
import time

ROUNDS = 12
N = 6


def run_round():
    sem = threading.Semaphore(0)         # 票仓先清零
    order = []
    order_lock = threading.Lock()

    def waiter(idx):
        sem.acquire()                    # 全员睡在票仓上
        with order_lock:
            order.append(idx)

    ts = [threading.Thread(target=waiter, args=(i,), daemon=True)
          for i in range(N)]
    for t in ts:
        t.start()
    time.sleep(0.1)                      # 确保都睡在 acquire 里
    t0 = time.perf_counter()
    sem.release()                        # 先放一张票: 看谁最先醒
    time.sleep(0.05)
    for _ in range(N - 1):               # 补齐余票, 让全员都能通过
        sem.release()
    for t in ts:
        t.join()
    return order, time.perf_counter() - t0


if __name__ == "__main__":
    results = [run_round() for _ in range(ROUNDS)]
    for i, (order, dt) in enumerate(results):
        print("第 %2d 轮获票顺序: %s (耗时 %.0f ms)" % (i + 1, order, dt * 1000))
    first_is_zero = sum(1 for o, _ in results if o and o[0] == 0)
    print("第 0 个等待者拿第一张票的轮数: %d/%d" % (first_is_zero, ROUNDS))
    print("结论: 顺序接近 FIFO, 依赖 CPython 实现细节, 跨解释器不可依赖")
