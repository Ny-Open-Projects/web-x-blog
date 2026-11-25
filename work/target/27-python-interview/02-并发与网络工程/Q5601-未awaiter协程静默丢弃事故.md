---
title: [Q5601] 未 await 协程对象静默丢弃事故
date: 2026-11-21
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5601 · 未 await 协程对象静默丢弃事故复盘

> 难度:★★★★☆ | 标签:事故复盘, asyncio, 协程

**问**:代码"调用"了一个 async 函数但业务没执行，也没有报错中断，为什么？

**答**:结论：`async def` 的调用不执行函数体，只构造一个协程对象；不 `await`、不 `create_task`，它就永远不会被调度，函数体一行都不会跑。RuntimeWarning("coroutine ... was never awaited") 只在协程对象被 GC 时打一次警告且默认藏在日志里——而如果对象被立即丢弃（表达式语句、`list.append` 中转后遗漏），警告照样出现但没人看。事故形态还有更隐蔽的一种：协程对象被存进列表但没有事件循环引用它，或是在同步上下文里调用了异步函数。实战三道防线：① 静态检查（ruff 的 `ASYNC`/`RUF006` 规则能抓住未 await 挂起调用）；② 开发期 `PYTHONASYNCIODEBUG=1` 让未完成任务的警告更醒目；③ 评审时把"裸调用 async 函数"当一类 review 标记。

```python
import asyncio, warnings

async def charge(order_id):
    await asyncio.sleep(0)
    return f"charged-{order_id}"

async def main():
    charge("o1")                    # 事故源：只建对象，不执行
    tasks = [charge("o2")]          # 又一种：放进列表但没人 await

    results = []
    results.append(await charge("o3"))          # 正解 1：await
    results.append(asyncio.create_task(charge("o4")))  # 正解 2：登记进 loop
    results.append(await results[-1])

    # 捕获"never awaited"做演示：GC 未消费的协程
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        asyncio.ensure_future(charge("o5"))     # 在 loop 里但未等待
        await asyncio.sleep(0)
    await asyncio.sleep(0)

asyncio.run(main())
print("o1/o2 的函数体从未执行；o3/o4 已真正运行")
```

**追问一层**:`asyncio.ensure_future(coro)` 与 `create_task` 与裸 `await` 三者的差异与丢弃风险？
**追二层**:为什么 RuntimeWarning 只在 GC 时机触发？free-threading / 无 GC 环境下会怎样？

**背诵要点**
- 调用 async 函数=构造协程对象，不 await 不执行。
- never awaited 警告在 GC 时才出现，靠不住，要靠静态检查。
- 正解只有两条路：await 或 create_task 登记进 loop。

**复盘追问**
- 批量任务里混入"忘 await"的项，如何用收尾对账（计数/幂等键）兜住？提示：Q1587 done-callback 纪律。
- 测试如何强制暴露这类 bug？提示：warnings 升级为 error + coverage 断言副作用。
