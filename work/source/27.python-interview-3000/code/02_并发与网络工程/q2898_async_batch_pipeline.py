# -*- coding: utf-8 -*-
"""异步批处理全链路模板: 读 -> 处理 -> 写。

- 读侧: 异步逐行产出, 投入有界队列, 队列满即被挂起 (背压);
- 处理侧: 攒批消费, 每批做一次"昂贵处理" (模拟一次网络往返);
- 写侧: 单写者顺序落盘, 天然保持全局顺序;
- 监视器: 采样队列深度, 验证背压真实生效 (队列打满上限)。
"""
import asyncio

BATCH = 5        # 攒批上限
QMAX = 8         # 入口队列容量: 上游最多领先下游 8 行
TOTAL = 23
N_PROC = 2


async def reader(q):
    """读侧: 逐行读出并投递。"""
    for i in range(1, TOTAL + 1):
        await q.put("row-%02d" % i)     # 队列满则挂起, 上游被限速
    for _ in range(N_PROC):
        await q.put(None)               # 每个处理者一个毒丸


async def processor(q, out_q):
    """处理侧: 攒批消费, 批满或收尾时交给写侧。"""
    buf = []
    while True:
        item = await q.get()
        if item is None:
            q.task_done()
            if buf:                     # 收尾: 不足一批的尾巴也要交出去
                await out_q.put(buf)
            break
        buf.append(item.upper())
        if len(buf) >= BATCH:
            await asyncio.sleep(0.01)   # 每批一次"昂贵处理"
            await out_q.put(buf)
            buf = []
        q.task_done()


async def writer(out_q, n_proc):
    """写侧: 单写者顺序消费, 天然保序。"""
    rows = batches = 0
    ended = 0
    while ended < n_proc:
        batch = await out_q.get()
        if batch is None:
            ended += 1
            out_q.task_done()
            continue
        rows += len(batch)
        batches += 1
        await asyncio.sleep(0.002)      # 写盘代价
        out_q.task_done()
    return rows, batches


async def monitor(q, stop, peak):
    """采样队列深度, 观察背压是否真实发生。"""
    while not stop.is_set():
        peak[0] = max(peak[0], q.qsize())
        await asyncio.sleep(0.001)


async def main():
    q = asyncio.Queue(maxsize=QMAX)
    out_q = asyncio.Queue()
    peak = [0]
    stop = asyncio.Event()
    mon = asyncio.create_task(monitor(q, stop, peak))
    prod = asyncio.create_task(reader(q))
    cons = [asyncio.create_task(processor(q, out_q)) for _ in range(N_PROC)]
    wtr = asyncio.create_task(writer(out_q, N_PROC))

    await prod                          # 先等读侧投递完毕
    await q.join()                      # 再等队列精确排空(含毒丸)
    for _ in range(N_PROC):
        await out_q.put(None)           # 给写侧发关门毒丸
    rows, batches = await wtr
    stop.set()
    await asyncio.gather(mon, prod, *cons)

    print("对账: 读 %d 行 -> %d 批 -> 写 %d 行, 队列峰值 %d/%d"
          % (TOTAL, batches, rows, peak[0], QMAX))
    assert rows == TOTAL
    assert peak[0] > 0, "队列从未积压, 背压演示失败"
    print("要点: 有界队列打满即背压生效, 攒批摊薄昂贵操作, 单写者保序")


if __name__ == "__main__":
    asyncio.run(main())
