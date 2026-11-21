---
title: [Q580] call_later 与定时器堆的实现
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q580 · call_later 与定时器堆的实现

> 难度:★★★☆ | 标签:asyncio, 定时器, heapq

**问**:asyncio 的 call_later 是怎么组织上千个定时器的?取消一个定时器是 O(1) 还是 O(n)?

**答**:所有定时器放在一个最小堆里,元素是 `(deadline, 序号, TimerHandle)`,序号保证同时到期的按插入顺序弹出(FIFO),取堆顶 O(1)、插入 O(log n)。取消并不从堆里物理移除,而是把 TimerHandle 标记 `_cancelled=True`,事件循环弹堆时跳过已取消的句柄——所以取消是 O(1),垃圾留在堆里直到到期被弹出丢弃,这是典型的惰性删除。到期判断用单调时钟 `loop.time()`,不受系统时间回拨影响。

```python
# file: code/02_并发与网络工程/q580_timer_heap.py
import asyncio
import heapq


class TimerHeap:
    """复刻 asyncio 定时器堆: 惰性删除 + seq 保证同时到期 FIFO。"""

    def __init__(self) -> None:
        self._heap = []
        self._seq = 0

    def call_later(self, delay: float, callback, *args):
        deadline = asyncio.get_running_loop().time() + delay
        self._seq += 1
        handle = {"cancelled": False, "cb": callback, "args": args}
        heapq.heappush(self._heap, (deadline, self._seq, handle))
        return handle

    def cancel(self, handle) -> bool:
        if handle["cancelled"]:
            return False
        handle["cancelled"] = True  # 惰性删除: 只标记
        return True

    def fire_due(self, now: float) -> int:
        fired = 0
        while self._heap and self._heap[0][0] <= now:
            deadline, _seq, handle = heapq.heappop(self._heap)
            if not handle["cancelled"]:  # 已取消的直接丢弃
                handle["cb"](*handle["args"])
                fired += 1
        return fired


async def main() -> None:
    loop = asyncio.get_running_loop()
    fired = []

    heap = TimerHeap()
    # 乱序注册: 0.15 最晚注册却最先到期
    h1 = heap.call_later(0.15, lambda: fired.append("0.15s"))
    heap.call_later(0.05, lambda: fired.append("0.05s-a"))
    heap.call_later(0.05, lambda: fired.append("0.05s-b"))
    heap.call_later(0.10, lambda: fired.append("0.10s"))
    heap.cancel(h1)  # 取消 0.15 那个

    start = loop.time()
    while heap._heap:
        loop_time = loop.time()
        if heap._heap[0][0] > loop_time:
            await asyncio.sleep(heap._heap[0][0] - loop_time)
        heap.fire_due(loop.time())
    print("手写堆触发顺序:", fired)
    assert fired == ["0.05s-a", "0.05s-b", "0.10s"], "同时到期应 FIFO, 已取消应跳过"

    # 对照: 真实 loop.call_later 行为一致
    order = []
    loop.call_later(0.05, lambda: order.append("a"))
    loop.call_later(0.05, lambda: order.append("b"))
    cancel_me = loop.call_later(0.01, lambda: order.append("never"))
    cancel_me.cancel()
    await asyncio.sleep(0.1)
    print("asyncio.call_later 顺序:", order)
    assert order == ["a", "b"]


asyncio.run(main())
```

**追问**:1) 为什么 deadline 相同时需要 seq?——堆比较元组时若 deadline 相等会继续比较第二个元素,没有 seq 就会比较 handle dict 直接 TypeError,同时它保证了同刻定时器的 FIFO 语义。2) 定时器堆的工程细节?——(deadline, seq, handle) 元组;取消用「标志位 + 惰性弹出」(取消不物理删除);heapq 不支持线程安全,跨线程要锁(Q581 层次)。3) 与 call_at 的关系?——call_later(delay) = call_at(now + delay);loop.time() 是单调钟(Q505);最小堆顶 = 最近到期。4) 生产陷阱?——比较元组含不可比对象 TypeError;取消不惰性让堆退化;用墙钟 time.time() 算 deadline 被回拨坑(Q505)。

---
