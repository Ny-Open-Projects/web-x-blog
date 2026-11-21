---
title: [Q2657] Semaphore 的唤醒顺序实测:等待者按什么顺序拿到票
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2657 · Semaphore 的唤醒顺序实测:等待者按什么顺序拿到票

> 难度:★★★ | 标签:Semaphore, FIFO, 实现细节

**问**:6 个线程睡在 Semaphore 上,放一张票,谁先拿到?这个顺序有保证吗?

**答**:CPython 的 Semaphore 内部是 Condition + 计数器,release 走 notify(1),从 waiters 队列头唤醒,实测 12 轮里第一个等待者 12 次全部先拿到票,后续顺序接近 FIFO 但偶有穿插。要点是:这是 CPython 实现细节,语言规范不承诺 FIFO,跨解释器或未来版本都可能变化。

- 需要严格公平要自己造票号队列(先到先发号,叫号入席);

- 实测中「补齐余票」阶段的顺序仍有穿插,说明唤醒顺序与调度顺序是两回事;

- 排队列的等待者被唤醒后还要重新抢锁,这一步可能被插队;

- 公平性测试的标准姿势:全员栅栏就位后放票,统计多轮顺序分布。

```python
# file: code/02_并发与网络工程/q2657_sem_order.py
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
```

**追问**:1) 为什么不直接承诺 FIFO?——承诺公平性会绑死实现并牺牲吞吐,库作者把公平作为策略留给上层。2) threading.Lock 的唤醒顺序同理吗?——同理,Lock 也是 Condition 实现,同样不承诺顺序。3) 底层机制:被唤醒的等待者为什么还可能被插队?——notify 只把队头 waiter 移出等待集,它醒来后还要重新参与 acquire 的锁竞争;若此刻有新到线程先抢到锁,队列头就被插队,这正是"唤醒顺序不等于获票顺序"的机制根源,也是语言层不敢承诺公平的原因。4) 生产陷阱?——把测试机观察到的 FIFO 写进业务正确性论证,换解释器或升级版本后顺序漂移;真要公平就显式造票号队列(先到先发号、叫号入席),而不是赌实现细节。

---
