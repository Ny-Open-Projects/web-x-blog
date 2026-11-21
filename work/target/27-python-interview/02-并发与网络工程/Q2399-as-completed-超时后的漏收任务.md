---
title: [Q2399] as_completed 超时后的漏收任务
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2399 · as_completed 超时后的漏收任务

> 难度:★★★ | 标签:as_completed, 超时, 任务取消

**问**:as_completed(fs, timeout=0.25) 超时之后,没跑完的任务去哪了?

**答**:超时让迭代器抛 TimeoutError 终止,但任务本体还挂在事件循环里继续跑,既不出结果也不退出,放任不管就是任务泄漏。

- 实测四个任务两快两慢:预算内只收到两个快结果,两个慢任务被遗留在循环中;

- 纪律动作:用原始 Future 列表筛出未完成者,逐个 cancel,再 gather(return_exceptions=True) 等取消落实;

- 实测收尸结果全部是 CancelledError,慢任务没有真的跑完 5 秒;

- 记住 as_completed 的超时只约束"迭代",不约束"任务",收尸责任在调用方。

```python
# file: code/02_并发与网络工程/q2399_as_completed_timeout.py
# -*- coding: utf-8 -*-
"""as_completed 超时后的漏收任务: 预算耗尽, 慢任务要显式收尸。

- as_completed(timeout) 超时抛 TimeoutError, 迭代直接终止;
- 没被迭代到的任务不会消失, 还在事件循环里默默跑着;
- 纪律: 捕获超时后, 用原 Future 列表找出未完成者, 取消并 await 收尸。
"""
import asyncio

TIMEOUT = 0.25


async def quick(name):
    await asyncio.sleep(0.05)
    return name + "-ok"


async def slow(name):
    await asyncio.sleep(5.0)
    return name + "-ok"          # 注定等不到


async def main():
    fs = [asyncio.ensure_future(quick("快1")),
          asyncio.ensure_future(slow("慢1")),
          asyncio.ensure_future(quick("快2")),
          asyncio.ensure_future(slow("慢2"))]
    got = []
    timed_out = False
    try:
        for fut in asyncio.as_completed(fs, timeout=TIMEOUT):
            got.append(await fut)
    except asyncio.TimeoutError:
        timed_out = True
    print("预算内拿到:", got)
    assert timed_out and sorted(got) == ["快1-ok", "快2-ok"]

    stragglers = [f for f in fs if not f.done()]
    print("预算外遗留:", [f.get_name() for f in stragglers])
    for f in stragglers:
        f.cancel()
    results = await asyncio.gather(*stragglers, return_exceptions=True)
    print("收尸结果:", [type(r).__name__ for r in results])
    assert all(isinstance(r, asyncio.CancelledError) for r in results), \
        "遗留任务应被取消并等到落实, 而不是放任空跑 5 秒"
    assert all(f.cancelled() for f in stragglers)


if __name__ == "__main__":
    asyncio.run(main())
```

**追问**:1) 任务正在 await 的 IO 能被 cancel 打断吗?——能,CancelledError 会注入到 await 点,socket 操作被中断后由框架收尾。2) 超时后想拿到慢任务的迟来结果呢?——那就别取消,改成收进后台任务注册表,完成后再处理,取舍要显式。3) 「超时只约束迭代不约束任务」的完整语义?——as_completed 的 TimeoutError 终止的是「收取」,任务还在事件循环里跑;收尸责任在调用方:原 Future 列表筛未完成→cancel→gather(return_exceptions=True) 等取消落实——「收取与任务生命周期解耦」是 as_completed 最重要的边界。4) 迟来结果的取舍怎么显式化?——取消(丢弃结果)或收进后台任务注册表(Q1588)等完成再处理——两条路都要显式选,默认「取消」会丢结果,默认「收编」会拖关闭——取舍写进代码注释与配置。5) 生产陷阱?——超时后不收尸(任务泄漏+异常 never retrieved);cancel 后不 gather(取消没落实);慢任务做了不可取消的清理(收尸卡住,Q2402);以为超时=任务终止(只是迭代终止);超时后重试整批(已完成部分重复执行,要幂等键)。

---
