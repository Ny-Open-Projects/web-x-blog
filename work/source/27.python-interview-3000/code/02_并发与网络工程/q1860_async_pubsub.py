# -*- coding: utf-8 -*-
"""异步事件的发布订阅: 每个订阅者独立队列串行消费, 异常不越界。

- publish 把事件 put_nowait 进各订阅者的队列, 发布者永不被订阅者拖住;
- 每个订阅者一个 pump 任务, 严格按发布顺序串行处理, 顺序保证来自单队列;
- handler 抛异常只记录到自己的错误簿, 其他订阅者与后续事件不受影响。
"""
import asyncio


class AsyncBus:
    def __init__(self):
        self._subs = {}                        # topic -> [(name, q, task)]
        self.errors = []                       # (subscriber, exception)

    def subscribe(self, topic, name, handler):
        q = asyncio.Queue()
        task = asyncio.create_task(self._pump(name, q, handler))
        self._subs.setdefault(topic, []).append((name, q, task))
        return task

    async def _pump(self, name, q, handler):
        while True:
            event = await q.get()
            try:
                await handler(event)
            except Exception as e:
                self.errors.append((name, repr(e)))

    async def publish(self, topic, event):
        for _, q, _ in self._subs.get(topic, []):
            q.put_nowait(event)                # 永不阻塞发布者

    async def stop(self):
        tasks = [t for lst in self._subs.values() for _, _, t in lst]
        for t in tasks:
            t.cancel()
        await asyncio.gather(*tasks, return_exceptions=True)


async def main():
    bus = AsyncBus()
    processed_a = []
    topic_c_seen = []

    async def handler_a(ev):
        await asyncio.sleep(0.01)
        processed_a.append(ev)

    async def handler_b(ev):
        if ev % 2 == 0:
            raise ValueError("偶数事件我故意处理不了: %d" % ev)

    async def handler_c(ev):
        topic_c_seen.append(ev)

    bus.subscribe("orders", "A-审计", handler_a)
    bus.subscribe("orders", "B-风控", handler_b)
    bus.subscribe("payments", "C-对账", handler_c)

    for i in range(1, 7):
        await bus.publish("orders", i)
    await asyncio.sleep(0.25)

    print("A 收到:", processed_a)
    print("B 的异常簿:", bus.errors)
    print("C 收到:", topic_c_seen)
    assert processed_a == [1, 2, 3, 4, 5, 6], "A 严格按发布顺序串行"
    assert len(bus.errors) == 3, "B 只在偶数事件上失败三次"
    assert all(name == "B-风控" for name, _ in bus.errors), "异常不越界"
    assert topic_c_seen == [], "跨 topic 隔离"
    await bus.stop()
    print("结论: 订阅者互为防火墙, 顺序靠单队列, 故障靠 try/except 收纳")


if __name__ == "__main__":
    asyncio.run(main())
