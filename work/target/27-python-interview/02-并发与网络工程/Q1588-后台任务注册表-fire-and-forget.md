---
title: [Q1588] 后台任务注册表:fire-and-forget 的收编
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1588 · 后台任务注册表:fire-and-forget 的收编

> 难度:★★★★ | 标签:asyncio, 后台任务, 优雅关闭

**问**:主流程想丢几个后台任务去跑(fire-and-forget),怎么保证它们不会被 GC 吞掉、异常不丢失、关闭时不被腰斩?

**答**:用一个注册表收编。spawn 把 Task 存进字典——强引用解决 GC 陷阱(Q603:循环不持任务引用,任务随时可能被回收);done callback 在完成时移出注册表并回收结果或异常——异常在这里被领走,不会变成 never retrieved;shutdown 在主流程结束时统一排空,asyncio.wait 等剩余任务收尾,超时的记录告警。三个动作缺一不可:只持引用不管异常,失败无声;只管异常不持引用,任务可能根本跑不完;都不做,关闭时后台任务被腰斩。

```python
# file: code/02_并发与网络工程/q1588_bg_registry.py
"""后台任务注册表: fire-and-forget 的收编。

裸 create_task 不持引用会被 GC 吞掉(Q603 的陷阱); 放进注册表:
- 强引用: 注册表替你持有任务;
- done callback: 完成即移出并回收结果/异常;
- shutdown: 主流程结束时统一排空, 剩下的收编任务一个不漏。
"""
import asyncio


class BackgroundRegistry:
    def __init__(self):
        self.tasks = {}
        self.outcomes = {}

    def spawn(self, name, coro):
        task = asyncio.create_task(coro, name=name)
        self.tasks[name] = task                    # 强引用, 防 GC
        task.add_done_callback(lambda t, n=name: self._collect(n, t))
        return task

    def _collect(self, name, task):
        self.tasks.pop(name, None)
        if task.cancelled():
            self.outcomes[name] = "cancelled"
            return
        try:
            self.outcomes[name] = task.result()
        except Exception as e:
            self.outcomes[name] = e                # 异常在这里回收, 不变孤儿

    async def shutdown(self, timeout=2.0):
        pending = [t for t in list(self.tasks.values()) if not t.done()]
        if not pending:
            return []
        _, still = await asyncio.wait(pending, timeout=timeout)
        return list(still)


async def job(name, delay, fail=False):
    await asyncio.sleep(delay)
    if fail:
        raise ValueError(name + " 失败")
    return name + " 完成"


async def main():
    reg = BackgroundRegistry()
    reg.spawn("flush", job("flush", 0.05))
    reg.spawn("metrics", job("metrics", 0.3))
    reg.spawn("report", job("report", 0.02, fail=True))
    print("主流程干完活, 注册表里还有:", sorted(reg.tasks))

    still = await reg.shutdown(timeout=1.0)
    print("shutdown 后未完成:", [t.get_name() for t in still])
    for name, outcome in sorted(reg.outcomes.items()):
        print("后台 %-8s -> %s" % (name, outcome))

    assert not still, "超时足够时后台应全部收尾"
    assert not reg.tasks, "done callback 应清空注册表"
    assert isinstance(reg.outcomes["report"], ValueError), "失败任务的异常应被回收"
    assert reg.outcomes["flush"] == "flush 完成"
    print("结论: 注册表 = 强引用 + 完成回收 + 关闭排空, 三件套缺一不可")


if __name__ == "__main__":
    asyncio.run(main())
```

**追问**:1) shutdown 超时后剩余任务怎么办?——cancel 后再 gather 一轮给它们收尾机会,仍不退出的记录名字与栈,交给监控。2) shutdown 的排空语义怎么定?——三档:优雅(wait 全部完成)、受限(cancel 超时任务后再 gather 收尾)、强杀(记录后放弃);与线程池 shutdown(Q1305)的三档完全同构——两套并发模型的收尾语义可以互相印证。3) 注册表为什么用强引用而不是弱引用?——弱引用下任务可能被 GC 静默吞掉(任务根本跑不完);强引用保证存活;完成时 done callback 移除,注册表不涨——「创建即收编、完成即销账」。4) 生产陷阱?——shutdown 超时后直接丢任务(没 cancel+再 gather,资源清理悬空);注册表无上限(fire-and-forget 洪水,要限流);异常回收后没告警(任务失败静默);关闭流程与注册表没有联动(server 关闭时后台任务还在跑,写入已关闭的连接)。

---
