# -*- coding: utf-8 -*-
"""异步优先级队列的饥饿治理: 老化提权 + 饥饿地板, 让低优先级也能出头。

- 纯 PriorityQueue: 高优先级流持续到来时, 低优先级永远排在堆底, 饿死;
- 陷阱: 若全体条目同步老化, 相对顺序不变, 低优先级照样追不上;
- 正解: 老化提权设地板封底, 到达地板后按先到先赢, 等待时间成为硬通货。
"""
import asyncio
import time

AGING_STEP = 0.1                              # 每等待 0.1 秒提权一级
STARVATION_FLOOR = -1                         # 优先级地板: 封住老化下限


class AgingPriorityQueue:
    def __init__(self):
        self._pq = asyncio.PriorityQueue()
        self._meta = {}                        # seq -> [base, t_in, payload]
        self._seq = 0
        self.boost_log = []

    async def put(self, payload, base_prio):
        now = asyncio.get_running_loop().time()
        seq = self._seq
        self._seq += 1
        self._meta[seq] = [base_prio, now, payload]
        self._pq.put_nowait((base_prio, seq))

    async def reheap_loop(self):
        while True:
            await asyncio.sleep(0.1)
            now = asyncio.get_running_loop().time()
            entries = []
            while not self._pq.empty():        # 整堆取出重算有效优先级
                entries.append(self._pq.get_nowait())
            for eff, seq in entries:
                base, t_in, _ = self._meta[seq]
                new_eff = max(base - int((now - t_in) / AGING_STEP),
                              STARVATION_FLOOR)
                if new_eff != eff:
                    self.boost_log.append((seq, eff, new_eff))
                self._pq.put_nowait((new_eff, seq))

    async def get(self):
        _, seq = await self._pq.get()
        return self._meta.pop(seq)[2]


async def scenario(aging, duration):
    q = AgingPriorityQueue()
    low_served = []
    high_served = {"n": 0}

    async def consumer():
        end = asyncio.get_running_loop().time() + duration
        while asyncio.get_running_loop().time() < end:
            payload = await q.get()
            if payload == "LOW":
                low_served.append(asyncio.get_running_loop().time())
            else:
                high_served["n"] += 1
            await asyncio.sleep(0.02)          # 消费速率 50 条/s

    async def high_stream():
        for _ in range(100):                   # 高优先级流 100 条/s, 持续 1 秒
            await q.put("HIGH", 0)
            await asyncio.sleep(0.01)

    reheap_task = asyncio.create_task(q.reheap_loop()) if aging else None
    c_task = asyncio.create_task(consumer())
    await asyncio.sleep(0.05)
    for _ in range(3):
        await q.put("LOW", 9)                  # 三条低优先级任务
    await high_stream()
    await asyncio.sleep(max(0.0, duration - 1.05))
    c_task.cancel()
    if reheap_task:
        reheap_task.cancel()
    await asyncio.gather(c_task, reheap_task if reheap_task else c_task,
                         return_exceptions=True)
    return low_served, high_served["n"], q.boost_log


async def main():
    low0, high0, _ = await scenario(aging=False, duration=1.0)
    print("无老化: 低优先级执行 %d 条, 高优先级执行 %d 条" % (len(low0), high0))
    assert len(low0) == 0, "高优先级流不停止, 低优先级必然饿死"

    low1, high1, boosts = await scenario(aging=True, duration=1.5)
    print("有老化: 低优先级执行 %d 条, 高优先级执行 %d 条, 提权事件 %d 次"
          % (len(low1), high1, len(boosts)))
    assert len(low1) == 3, "老化后三条低优先级任务都应被执行"
    assert high1 > 30, "高优先级吞吐不应被老化机制摧毁"
    print("结论: 老化把 '先来后到' 折算进优先级, 饥饿是调度策略的 bug 不是宿命")


if __name__ == "__main__":
    asyncio.run(main())
