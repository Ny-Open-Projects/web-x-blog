---
title: [Q2401] 慢回调看门狗:debug 模式的计时点名
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2401 · 慢回调看门狗:debug 模式的计时点名

> 难度:★★★★ | 标签:事件循环, 慢回调, set_debug

**问**:协程卡住整个事件循环,怎么在开发期就发现?

**答**:事件循环是单线程的,一个 200ms 的同步阻塞让所有任务一起停摆,受害者表现为"sleep 0.01 睡出了 0.2 秒"。loop.set_debug(True) 配 slow_callback_duration 给每个回调计时,超标的在日志里点名。

- 实测受害者等待 0.246s,本应 0.01s,日志出现 Executing Handle blocking_callback took 0.2xx seconds;

- slow_callback_duration 阈值默认 100ms,可按业务调严,开发期 50ms 起步;

- 点名只指路不定罪:阻塞调用要丢线程池 run_in_executor,或拆小在中间 await 让出控制权;

- 生产期等价物是自建心跳监控:协程定期打卡,超时告警,因为生产不会开 debug。

```python
# file: code/02_并发与网络工程/q2401_slow_callback_watchdog.py
# -*- coding: utf-8 -*-
"""慢回调看门狗: debug 模式给每个回调计时, 超标就点名。

- 事件循环是单线程的, 一个 200ms 的同步阻塞让所有任务一起卡住;
- loop.set_debug(True) 配 slow_callback_duration, 超时回调在日志里现形;
- 抓到之后对症下药: 阻塞调用丢线程池, 或拆小让出控制权。
"""
import asyncio
import io
import logging
import time


def blocking_callback():
    """罪魁祸首: 在回调里同步睡 200ms, 整个循环陪它停摆。"""
    time.sleep(0.2)


async def victim():
    """受害者视角: 一个 10ms 就能完成的等待被拖长。"""
    t0 = time.monotonic()
    await asyncio.sleep(0.01)
    return time.monotonic() - t0


async def main(capture):
    loop = asyncio.get_running_loop()
    loop.slow_callback_duration = 0.05           # 阈值调低到 50ms 便于演示
    loop.call_soon(blocking_callback)            # 塞一个阻塞回调进队列
    cost = await victim()
    await asyncio.sleep(0.05)
    return cost


def main_entry():
    stream = io.StringIO()
    handler = logging.StreamHandler(stream)
    alog = logging.getLogger("asyncio")
    alog.addHandler(handler)
    alog.setLevel(logging.WARNING)
    cost = asyncio.run(main(stream), debug=True)
    alog.removeHandler(handler)
    text = stream.getvalue()
    flagged = [ln for ln in text.splitlines() if "took" in ln]
    print("受害者等待耗时: %.3fs (本应 0.01s)" % cost)
    for ln in flagged:
        print("看门狗点名:", ln.strip()[:100])
    assert flagged, "debug 模式必须点名慢回调"
    assert cost > 0.1, "阻塞回调期间, 无辜协程的等待被显著拖长"


if __name__ == "__main__":
    main_entry()
```

**追问**:1) await asyncio.sleep 也会被点名吗?——只有单次回调执行超阈值才点名,sleep 本身不占循环,不会误报。2) C 扩展里的阻塞能被抓到吗?——能抓到现象(整个循环停摆)但拿不到栈,原生阻塞要靠心跳与采样工具定位。3) slow_callback_duration 的机制与调参?——debug 模式下每个回调计时,超过阈值(默认 100ms)在日志点名「Executing <callback> took ...」;开发期 50ms 起步调严;只测「单次回调执行」,sleep 不占循环不会误报(见原问)——「点名指路不定罪」,对症下药是丢线程池或拆小让出。4) 生产期的心跳监控怎么搭?——协程定期 beat+看门狗(Q1590);C 扩展阻塞抓不到栈(采样工具 py-spy 或 eBPF);slow_callback_duration 只在 debug 模式生效,生产等价物是心跳——「开发期点名+生产期心跳」双层监控。5) 生产陷阱?——200ms 同步阻塞藏在 C 扩展里(现象有、栈没有);把受害者(sleep 变长)当网络问题排查;debug 模式没在 CI 跑(阻塞回调上线才现形);修了阻塞没回归(下次又出现);心跳打在循环开头(卡在循环体中间发现不了,Q1590 同坑)。

---
