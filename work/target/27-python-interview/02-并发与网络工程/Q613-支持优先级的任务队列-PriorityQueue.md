---
title: [Q613] 支持优先级的任务队列:PriorityQueue 防比较坑
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q613 · 支持优先级的任务队列:PriorityQueue 防比较坑

> 难度:★★☆ | 标签:优先级队列, 线程池, heapq

**问**:线程池想让"VIP 任务插队",PriorityQueue 直接放函数为什么不行?

**答**:PriorityQueue 内部用堆比较元素,如果元素是 (priority, fn),两个 fn 无法比较会 TypeError;标准解法是三元组 (priority, seq, item),seq 是单调递增序号,既打破比较又提供同优先级 FIFO。进阶:支持优先级抢占的"工作 stealing"或动态优先级(等待越久优先级越高,防饿死 VIP 之外的普通任务)。注意优先级队列解决的是"未入队的先来后到",不能抢占正在执行的任务——要抢占只能协作式(检查取消标志),所以 demo 里 VIP 只能插到"还在队列里"的任务之前。另外关停顺序是高频竞态点:必须先 `q.join()` 排空、再 set 停止标志;反过来 worker 会留下未处理任务直接退出,`q.join()` 等不到 task_done 永久阻塞。

```python
# file: code/02_并发与网络工程/q613_priority_pool.py
import itertools
import queue
import threading
import time

results: list = []
executed_order: list = []


class PriorityWorkerPool:
    def __init__(self, workers: int = 2) -> None:
        self._q: queue.PriorityQueue = queue.PriorityQueue()
        self._seq = itertools.count()
        self._stop = threading.Event()
        self._workers = [
            threading.Thread(target=self._run, daemon=True) for _ in range(workers)
        ]
        for w in self._workers:
            w.start()

    def submit(self, priority: int, name: str, fn) -> None:
        self._q.put((priority, next(self._seq), name, fn))  # seq 防函数比较

    def _run(self) -> None:
        while not self._stop.is_set():
            try:
                prio, seq, name, fn = self._q.get(timeout=0.5)
            except queue.Empty:
                continue
            executed_order.append(name)
            fn()
            self._q.task_done()

    def shutdown(self) -> None:
        # 先排空队列再停机: 若先 set stop, worker 可能在两次 get 之间
        # 直接退出, 队列里留下未处理任务, join() 永久阻塞(经典关停竞态)
        self._q.join()
        self._stop.set()


def job(name: str) -> None:
    time.sleep(0.05)
    results.append(name)


if __name__ == "__main__":
    pool = PriorityWorkerPool(workers=1)  # 单 worker 顺序清晰
    # 先提交低优先级, 再提交 VIP: VIP 只能插队"还在队列里"的任务
    for i in range(5):
        pool.submit(priority=10, name=f"normal-{i}", fn=lambda n=f"normal-{i}": job(n))
    # 等 worker 取走第一个任务(取走即脱离队列, VIP 抢不过它)
    deadline = time.monotonic() + 2
    while len(executed_order) < 1 and time.monotonic() < deadline:
        time.sleep(0.001)
    pool.submit(priority=1, name="vip", fn=lambda: job("vip"))
    pool.shutdown()
    print("执行顺序:", executed_order)
    assert executed_order[0] == "normal-0", "已被 worker 取走的任务无法被抢占"
    assert executed_order[1] == "vip", "VIP 应插队到队列中剩余任务之前"
    assert executed_order[2:] == [f"normal-{i}" for i in range(1, 5)]
    print("PriorityQueue 语义验证通过")
```

**追问**:1) 怎么防止低优先级任务被永久饿死?——老化(aging):入队时间越久优先级值越小,定期给等待任务提权;或按比例保留配额(每 N 个 VIP 插 1 个普通)。2) 防比较坑的完整姿势?——(priority, count, item) 三元组:count 自增保证 FIFO 平局且挡住 dict 不可比(Q495/2095);item 不可比时 count 必须先拦住;PriorityQueue 线程安全版供生产者消费者。3) 优先级反转?——低优持锁高优等;缓解:锁内不做重活、优先级继承(内核级)或拆锁;Python 层主要是「锁内任务拆小」。4) 生产陷阱?——元组第二元素不可比 TypeError;动态改已入队优先级(堆不变式破坏,Q495);饿死无监控。

---
