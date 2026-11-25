---
title: "[Q5704] asyncio.Queue maxsize：背压背后的消费者死亡挂死"
date: 2026-11-24
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5704 · asyncio.Queue maxsize：背压背后的消费者死亡挂死

难度：P6 ｜ 标签：asyncio.Queue、maxsize、背压、QueueFull、put 挂死、超时

**问**：生产者往 `asyncio.Queue(maxsize=100)` 塞数据，消费者协程因异常退出后，整条流水线悄悄停摆但进程还活着，监控看不到任何错误——生产者 `await q.put()` 永远挂在队列满上。`maxsize` 的背压语义到底是什么？`put_nowait`、`put`、`put`+超时三种写入策略分别适合什么场景？怎么检测"消费者已经死了"？

**答**：
结论：`maxsize` 是队列积压上限，队列满时 `await put()` **挂起等待**而不是报错——这就是背压：上游减速由"下游不再消费"自动传导。代价是等待是无限期的，且只等"消费动作"，不验证"消费者健康"：消费者协程崩溃退出后，队列不再有人取，所有 `put` 永久挂起，既不抛异常也不超时。`put_nowait` 队列满时立即抛 `QueueFull`，把"下游不可用"显式化；`await put()` 隐式等待；`asyncio.wait_for(q.put(x), timeout)` 介于两者之间——等一个预算，超了先救援自己。

取舍：a) 数据不许丢（订单/计费）：`await put()` + 监控队列水位 + 消费者任务包 try/except 并上报，死亡要报警而不是静默；b) 可丢弃（行情/日志）：`put_nowait` + 满时丢弃计数，用丢包保护上游；c) 中间态（批量推上游但允许短暂等待）：`wait_for(put, timeout)`，超时后进入丢弃/降级分支；d) 生产者/消费者必须放在同一个 task group 或注册表里统一监管，消费者死了要让生产者也收到信号（取消或关闭哨兵），而不是各自为战；e) `qsize()` 在事件循环内是精确值，用它做水位监控没问题，但监控读取不应阻塞主循环。

实战：事故形态是"数据采集管道 20 个生产者 + 1 个消费者，消费者里数据库重连逻辑抛未捕获异常，生产者全挂死在 put 上，指标采集任务也排在队列里，监控超时才发现停了 40 分钟；修复是把消费者纳入 TaskGroup（消费者死则整组取消并告警），生产者 put 加 5 秒预算，超时丢弃并计数"。下面复现挂死与救援。

```python
import asyncio


async def main():
    q = asyncio.Queue(maxsize=3)
    for i in range(3):
        q.put_nowait(i)                      # 同步填满，暂不消费
    print("[1] 满队列 put_nowait:", end=" ")
    try:
        q.put_nowait("x")
    except asyncio.QueueFull as e:
        print("立即拒绝:", type(e).__name__)

    async def consumer():
        await asyncio.sleep(0)
        raise RuntimeError("consumer crashed")   # 消费者启动即崩

    task = asyncio.create_task(consumer())
    try:
        await task
    except RuntimeError:
        print("[2] 消费者已死亡，队列无人取")

    try:
        await asyncio.wait_for(q.put("x"), timeout=0.3)
        print("[3] put 成功")
    except asyncio.TimeoutError:
        print("[3] 生产者 put 挂死（0.3s wait_for 超时救援）")
    print("[4] 队列水位:", q.qsize(), "/", q.maxsize)


asyncio.run(main())
```

**追问一**：`maxsize=0`（无界）和 `maxsize` 很大（如 100 万）有什么本质区别？—— 没有本质区别，都是"背压只在内存耗尽时触发"。区别只在触发时机：前者靠进程内存上限兜底，后者靠 maxsize 兜底但上限本身是内存预算的换算值（每条消息大小 × maxsize）。真正需要的是按下游消费速率的有界队列 + 满策略三选一（等待/丢弃/拒绝），maxsize 的数值要按"下游最大可接受积压延迟"倒推，而不是拍脑袋。

**追问二**：怎么系统性地防止"消费者死亡导致生产者挂死"？—— 三层防线：第一层结构上，生产者与消费者放同一个 TaskGroup/结构化并发作用域，消费者异常会取消整组，生产者的 put 在取消时抛 CancelledError 而不是永久挂起；第二层运行时，消费者函数体整体 try/except，异常转告警并退避重启，同时给 put 包 wait_for 做最后保险；第三层观测上，队列水位 + put 等待时长作为指标，水位持续顶满 maxsize 就是消费者故障的先兆。只加 wait_for 而不做结构化监管，只是把挂死变成丢数据，问题没根治。

## 背诵要点
- `maxsize` 满时 `await put()` 无限期挂起（背压），不校验消费者是否存活；消费者崩溃 → 生产者集体挂死。
- 三种写策略：`put_nowait` 立即拒绝（可丢数据）、`await put` 不许丢但要监管消费者、`wait_for(put, t)` 留预算降级。
- 根治靠结构化并发：生产者消费者同组，消费者死则整组取消告警；水位顶满 = 消费者故障先兆。

## 复盘追问
- 消费者异常退出后为什么生产者不报错？（put 只等消费动作，不知道消费者存在与否）
- maxsize 从 0 改成 100 万解决了什么、没解决什么？（只是换了内存兜底触发点，没有引入满策略与监管）
