# -*- coding: utf-8 -*-
"""慢订阅者隔离: 有界队列 + 丢最老策略, 发布者永不被拖死。

- 每个订阅者一条有界队列, 快订阅者全量收到, 慢订阅者被限流;
- 慢订阅者队列满时丢最老事件并计数, 事件总量守恒: 收到 + 丢弃 = 发布;
- 事件总线的关键抉择不是 "要不要丢", 而是 "丢谁、记不记账"。
"""
import asyncio
import time

N_EVENTS = 20


class Subscriber:
    def __init__(self, name, maxsize=None, delay=0.0):
        self.name = name
        self.q = asyncio.Queue(maxsize) if maxsize else asyncio.Queue()
        self.delay = delay
        self.received = []
        self.dropped = 0
        self.task = None

    def offer(self, event):
        try:
            self.q.put_nowait(event)
        except asyncio.QueueFull:
            self.q.get_nowait()                # 丢最老的
            self.q.put_nowait(event)
            self.dropped += 1

    async def run(self):
        while True:
            ev = await self.q.get()
            if self.delay:
                await asyncio.sleep(self.delay)
            self.received.append(ev)


async def main():
    fast = Subscriber("fast")
    slow = Subscriber("slow", maxsize=3, delay=0.05)
    fast.task = asyncio.create_task(fast.run())
    slow.task = asyncio.create_task(slow.run())
    await asyncio.sleep(0.05)                  # 让消费任务先跑起来

    t0 = time.monotonic()
    for i in range(N_EVENTS):
        fast.offer(i)
        slow.offer(i)                          # 慢订阅者在这里大量溢出
    publish_cost = time.monotonic() - t0

    await asyncio.sleep(1.2)                   # 留足时间让慢订阅者清完队列
    fast.task.cancel()
    slow.task.cancel()
    await asyncio.gather(fast.task, slow.task, return_exceptions=True)

    print("发布 %d 条耗时 %.4fs(发布者无阻塞)"
          % (N_EVENTS, publish_cost))
    print("fast: 收到 %d 条" % len(fast.received))
    print("slow: 收到 %d 条, 丢弃 %d 条, 守恒=%s"
          % (len(slow.received), slow.dropped,
             len(slow.received) + slow.dropped == N_EVENTS))
    assert publish_cost < 0.05, "发布者必须瞬时完成, 不被慢订阅者拖住"
    assert len(fast.received) == N_EVENTS, "快订阅者全量收到"
    assert len(slow.received) + slow.dropped == N_EVENTS, "事件总量守恒"
    assert slow.dropped >= 15, "慢订阅者必然大量溢出"
    print("结论: 隔离慢订阅者的代价是丢弃, 诚实记账才能对账")


if __name__ == "__main__":
    asyncio.run(main())
