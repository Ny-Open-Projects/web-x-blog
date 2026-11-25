---
title: [Q5628] 无界 asyncio.Queue 积压的内存容量账
date: 2026-11-21
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5628 · 无界 asyncio.Queue 积压的内存容量账与水位治理

> 难度:★★★★☆ | 标签:容量规划, asyncio, 背压

**问**:"生产者生产快、消费者处理慢"用 `asyncio.Queue()`（默认 maxsize=0 无界）先跑着，这口的账怎么算？积压 100 万条消息占多少内存？为什么不加 maxsize 是定时炸弹？加上之后 put 会怎么表现，怎么设计丢弃与降级策略？

**答**:结论：无界队列的积压上限 = **磁盘外的一切内存**。算账：每条消息不只是一个对象——tuple/dict 载体 + 内嵌 str + Queue 内部 deque 槽位，实测一条 100B 载荷的消息常占 300-800B；100 万条 ≈ 0.3-0.8GB，再叠加上游还在推进，OOM 只是时间问题。危险在于 asyncio 队列**不会自己背压**：`put_nowait` 无界即无条件成功，loop 的其他任务持续被"搬运"占 CPU，看起来服务还活着、内存曲线却单调上涨。正确姿势：a) `maxsize=N` + `await put()`：满时生产者挂起，背压传导到上游（N 取"消费速率×可容忍延迟"）；b) 不允许背压的入口（如网络接收回调）用 `put_nowait` + **水位策略**：软水位打日志/降精度，硬水位丢弃最旧或最新并计数上报；c) 监控 `qsize()` 与"队列驻留时间"（消息入队时间戳），驻留时间才是用户体感。与 Q5506（线程池饱和背压）、Q5573（StreamWriter drain）同属"背压三兄弟"：队列限长、池限流、socket 水位。

```python
import asyncio, sys, tracemalloc

# ---- 1) 积压内存实测：一条消息的真实成本 ----
tracemalloc.start()
q = asyncio.Queue()
for i in range(200_000):
    q.put_nowait({"id": i, "payload": "x" * 100})     # 无界: 无条件成功
cur, peak = tracemalloc.get_traced_memory()
per = cur / 200_000
print(f"20 万条 100B 载荷: 当前 {cur/1e6:.0f} MB, 峰值 {peak/1e6:.0f} MB, "
      f"每条摊 {per:.0f} B（≈载荷的 {per/100:.0f} 倍）")
del q
tracemalloc.stop()

# ---- 2) maxsize + await put：背压传导演示 ----
async def demo_backpressure():
    q = asyncio.Queue(maxsize=10)
    produced, awaited = 0, 0

    async def producer():
        nonlocal produced, awaited
        for i in range(50):
            if q.full():
                awaited += 1                  # 背压触发的等待次数
            await q.put(i)
            produced += 1

    async def consumer():
        while produced < 50 or not q.empty():
            await asyncio.sleep(0.001)
            if not q.empty():
                q.get_nowait()

    await asyncio.gather(producer(), consumer())
    print(f"maxsize=10: 生产 {produced} 条, 满队列等待 {awaited} 次 —— 上游被限速")

asyncio.run(demo_backpressure())

# ---- 3) 水位策略：软/硬水位与丢弃计数 ----
class WatermarkQueue:
    def __init__(self, soft, hard):
        self.q = asyncio.Queue(maxsize=hard)
        self.soft, self.dropped = soft, 0
    def put(self, item):
        if self.q.qsize() >= self.soft:
            if self.q.qsize() >= self.q.maxsize or self.dropped:
                self.dropped += 1
                self.q.get_nowait()           # 硬水位: 丢最旧
                self.q.put_nowait(item)
                if self.dropped % 1000 == 1:
                    print(f"硬水位丢弃累计 {self.dropped} —— 打点上报")
                return
            print(f"软水位 qsize={self.q.qsize()} —— 降精度/告警")
        self.q.put_nowait(item)

wm = WatermarkQueue(soft=5, hard=10)
for i in range(12):
    wm.put(i)
print("最终 qsize:", wm.q.qsize(), "丢弃:", wm.dropped)
```

**追问一层**:为什么 `qsize()` 高但消费慢，CPU 却也不低？（每条消息的搬运（put/get、序列化、对象创建）都在 loop 上；无界队列放大搬运本身——背压不只是内存问题，也是 CPU 问题）。
**追问二层**:丢弃"最旧"还是"最新"怎么决策？（按业务时效性：行情/监控类丢最旧保最新；审计类一条不能丢→不允许丢弃，只能拒收上游或落盘缓冲）。
**追问三层**:多个生产者一个消费者的场景，maxsize 背压为什么可能不公平？（唤醒顺序 FIFO 但各生产者权重相同；需要优先级时改 PriorityQueue 或分队列配额）。

## 背诵要点
- 无界 Queue 积压上界 = 全部内存；每条消息摊销成本常为载荷的 3-8 倍，百万级即数百 MB。
- 治理三件套：maxsize+await put（背压）、put_nowait+水位（软告警/硬丢最旧）、监控 qsize 与驻留时间。
- 背压三兄弟：队列限长、线程池限流（Q5506）、StreamWriter drain（Q5573）。

## 复盘追问
- 服务 RSS 缓慢爬升三天后 OOMKill，代码里有无界队列——如何用 tracemalloc 与 qsize 曲线证明根因并定 maxsize？
- 入口是网络回调不允许 await，如何在不阻塞 loop 的前提下实现背压或降级？
