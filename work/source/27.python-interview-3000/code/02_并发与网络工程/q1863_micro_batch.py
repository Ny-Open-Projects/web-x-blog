# -*- coding: utf-8 -*-
"""异步微批聚合: 攒批上限与最大延迟的权衡, 定时器兜底不满的批。

- 请求进 pending, 攒到 max_batch 立刻冲刷; 否则挂一个 max_delay 定时器兜底;
- 冲刷一次最多带走 max_batch 条, 剩余的留在队列等下一次机会;
- 每个请求用 Future 拿回自己那份结果, 批处理对调用方完全透明。
"""
import asyncio


class MicroBatcher:
    def __init__(self, handler, max_batch=5, max_delay=0.3):
        self._handler = handler
        self._max = max_batch
        self._delay = max_delay
        self._pending = []                     # [(item, fut)]
        self._lock = asyncio.Lock()
        self._timer = None
        self.batch_sizes = []

    async def submit(self, item):
        fut = asyncio.get_running_loop().create_future()
        flush_now = False
        async with self._lock:
            self._pending.append((item, fut))
            if len(self._pending) >= self._max:
                flush_now = True
            elif self._timer is None:
                self._timer = asyncio.get_running_loop().call_later(
                    self._delay, self._kick)
        if flush_now:
            await self._drain()
        return await fut

    def _kick(self):
        self._timer = None                     # 定时器已触发, 置空允许再挂新的
        asyncio.ensure_future(self._drain())

    async def _drain(self):
        while True:
            async with self._lock:
                if not self._pending:
                    return
                batch = self._pending[:self._max]   # 一次最多带走 max_batch
                self._pending = self._pending[self._max:]
                if self._pending and self._timer is None:
                    self._timer = asyncio.get_running_loop().call_later(
                        self._delay, self._kick)
            results = await self._handler([it for it, _ in batch])
            self.batch_sizes.append(len(batch))
            for (_, f), r in zip(batch, results):
                if not f.done():
                    f.set_result(r)


async def handler(batch):
    await asyncio.sleep(0.02)
    return ["v:%s" % x for x in batch]


async def main():
    batcher = MicroBatcher(handler, max_batch=5, max_delay=0.3)

    async def submitter(k):
        return await asyncio.gather(*[batcher.submit("k%d-%d" % (k, i))
                                      for i in range(4)])

    loop = asyncio.get_running_loop()
    t0 = loop.time()
    res = await asyncio.gather(*[submitter(k) for k in range(3)])   # 12 个请求
    cost = loop.time() - t0
    flat = [x for sub in res for x in sub]

    print("批尺寸序列:", batcher.batch_sizes, "总耗时 %.2fs" % cost)
    assert len(flat) == 12 and all(v.startswith("v:k") for v in flat), \
        "每个请求都拿到自己的结果"
    assert max(batcher.batch_sizes) <= 5, "批尺寸不得超过上限"
    assert len(batcher.batch_sizes) >= 3, "至少有三批"
    assert any(b < 5 for b in batcher.batch_sizes), "定时器兜底的批必然不满"
    assert cost < 0.5, "最大延迟 0.3s 兜底生效"
    print("结论: 吞吐靠攒批, 延迟靠定时器封顶, 二者的交点就是批尺寸序列")


if __name__ == "__main__":
    asyncio.run(main())
