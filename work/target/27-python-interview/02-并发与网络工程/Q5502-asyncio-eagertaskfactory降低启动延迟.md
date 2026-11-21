---
title: [Q5502] asyncio.eager_task_factory（3.12）：降低任务启动延迟
date: 2026-11-18
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5502 · asyncio.eager_task_factory（3.12）：降低任务启动延迟

> 难度:★★★ | 标签:asyncio, eager_task_factory, 性能

**问**：默认的 `create_task` 为什么要「先挂起、下个循环迭代才执行」？`asyncio.eager_task_factory` 改变了什么？什么场景收益最大，什么场景反而要小心？和 TaskGroup 混用有什么注意点？

**答**：结论：默认 Task 走 `loop.call_soon` 排队——`create_task(coro)` 返回后协程**不立即执行**，要等当前代码把控制权交回事件循环的下一迭代，这带来两个成本：a) 短任务要付一次完整的「挂起-调度-恢复」往返（微秒级但海量调用下可观测）；b) 语义陷阱——create_task 之后「任务已开始」是错觉，循环体内的同步代码会先跑完。`eager_task_factory`（3.12）让任务**在 create_task 调用栈内同步执行到第一个真正 await 点**：不阻塞就完成的协程（命中缓存、立即返回的future）根本不进调度器，省掉整轮调度；要挂起的才被转成常规 Task 继续。收益场景：请求路径上「fire-and-forget 短任务」「单飞/去重检查后立即返回」这类高 QPS 小协程，社区基准显示消除了大量无谓的 loop 迭代。要小心的场景：a) **重入风险**——eager 执行意味着 create_task 的回调链里同步代码可能先于「caller 后续语句」跑完，依赖「create_task 返回时任务还没跑」的代码会翻车（如先 create 再初始化共享资源的顺序）；b) 异常路径变化：同步段抛的异常仍记入 Task（与默认一致的 done 回调语义），但抛出时机在调用栈内，traceback 更近。实战：`loop.set_task_factory(asyncio.eager_task_factory)` 全局开启，或 `asyncio.eager_task_factory(loop, coro, **kwargs)` 定点用；用 TaskGroup 时注意 eager 子任务若同步完成，组的「收集完成」路径更短，取消语义不变。

```python
# 基线:Python 3.12+。3.11 及以下降级:自建一个「立即 await 一次」包装,
# 或直接 await 协程(不 create_task),效果近似但语义不同。
import asyncio
import time

def order_eager() -> None:
    async def quick() -> str:
        return "done"  # 不含真实挂起,完成于调用栈内

    async def main() -> None:
        loop = asyncio.get_running_loop()
        loop.set_task_factory(asyncio.eager_task_factory)
        t = loop.create_task(quick())
        # eager:quick() 已在 create_task 内同步跑完,状态直接 done
        print("eager 状态:", t.done(), await t)

    asyncio.run(main())

def order_default() -> None:
    async def quick() -> str:
        return "done"

    async def main() -> None:
        loop = asyncio.get_running_loop()
        t = loop.create_task(quick())
        print("default 状态:", t.done())   # False:排队中,尚未执行
        print("default 结果:", await t)

    asyncio.run(main())

start = time.perf_counter()
order_default()
order_eager()
print(f"elapsed={time.perf_counter() - start:.4f}s")
```

**追问**：
1) eager 执行对「取消」有影响吗？——create_task 立即返回后对 task.cancel()：eager 模式下若协程已同步完成，cancel 是 no-op（任务已 done）；默认模式下至少要等到下一迭代才处理取消。判断逻辑「cancel 前任务是否已跑」在两种模式答案不同，混合使用时最容易出 bug。
2) 为什么不直接默认开启？——向后兼容：大量存量代码隐式依赖「create_task 后、await 前」这段窗口里 caller 先执行（如先 create_task 再补全某全局配置）；eager 把执行时机提前，这类顺序依赖会静默改变行为，所以只能 opt-in。
3) 怎么量化收益？——微基准对比 `create_task` + 立即 await 的总耗时（默认 vs eager），或压测服务的 P99：任务是纯计算/缓存命中型收益明显；任务内马上要 await 网络的，eager 只省「挂起到第一个 await」一步，收益趋近于零。
