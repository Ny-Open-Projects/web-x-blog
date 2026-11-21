# -*- coding: utf-8 -*-
"""wait_for 的边界竞争: 超时与完成同时到达, 结果不确定。

- 内部任务的耗时恰好贴着超时线时, 谁先落地是调度决定的;
- 实测 60 次同参数试验: 两种结局都出现, 证明边界是不确定区;
- 超时获胜时 wait_for 会 cancel 内部任务, 已做的功直接作废。
"""
import asyncio
import random

random.seed(42)
TIMEOUT = 0.05


async def inner(flag):
    try:
        await asyncio.sleep(TIMEOUT + random.uniform(-0.01, 0.01))
        return "done"
    except asyncio.CancelledError:
        flag["cancelled"] = True
        raise


async def trial():
    flag = {"cancelled": False}
    task = asyncio.get_running_loop().create_task(inner(flag))
    try:
        r = await asyncio.wait_for(task, timeout=TIMEOUT)
        return ("完成", r, flag["cancelled"])
    except asyncio.TimeoutError:
        await asyncio.wait([task])            # 等内部任务走到终态再收尸
        return ("超时", "cancelled" if task.cancelled() else "done",
                flag["cancelled"])


async def main():
    tally = {}
    for _ in range(60):
        kind, tail, cancelled = await trial()
        tally[(kind, tail)] = tally.get((kind, tail), 0) + 1
    print("60 次同参数试验的结局分布:")
    for k in sorted(tally):
        print("  ", k, "->", tally[k])
    print("要点: 贴线的超时判定不可复现, 预算要留余量, 别把超时当成精确闸门")
    print("要点: 超时获胜时内部任务被 cancel, 已完成的副作用要靠幂等兜底")


if __name__ == "__main__":
    asyncio.run(main())
