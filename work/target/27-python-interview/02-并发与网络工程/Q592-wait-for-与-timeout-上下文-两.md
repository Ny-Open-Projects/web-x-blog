---
title: [Q592] wait_for 与 timeout 上下文:两代超时 API
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q592 · wait_for 与 timeout 上下文:两代超时 API

> 难度:★★☆ | 标签:asyncio, timeout, API

**问**:asyncio.wait_for 和 Python 3.11 的 asyncio.timeout 有什么区别?分别适合什么场景?

**答**:wait_for 是函数式:把一个 awaitable 包起来,超时返回时内部任务已被取消,粒度是"这一个调用"。timeout 是作用域式:async with 块内所有 await 共享一个 deadline,超时时块内当前挂起的那一个 await 收到取消,适合"一段逻辑整体限时"以及多步操作共享预算;并且 timeout.expired() 能区分是超时还是外部取消。wait_for 的历史坑:超时时任务被取消但完成时机不确定,旧版本存在"返回结果与 TimeoutError 竞争"的 bug,3.8+ 已修复但语义上 timeout 上下文更清晰。

```python
# file: code/02_并发与网络工程/q592_timeout_api.py
import asyncio
import sys


async def slow(job: str = "job") -> str:
    try:
        await asyncio.sleep(5)
    except asyncio.CancelledError:
        print(f"{job} 收到取消, 清理后退出")
        raise
    return "done"


async def demo_wait_for() -> None:
    try:
        await asyncio.wait_for(slow("wait_for 里的任务"), 0.1)
    except asyncio.TimeoutError:
        print("wait_for: 超时, 内部任务已被取消")


async def demo_timeout_ctx() -> None:
    if sys.version_info < (3, 11):
        print("timeout 需要 3.11+, 跳过")
        return
    try:
        async with asyncio.timeout(0.1):
            await slow("作用域内任务")
            await slow("作用域内第二个任务")  # 多个 await 共享同一个 deadline
    except TimeoutError:
        print("timeout 上下文: 块内整体超时")


async def main() -> None:
    await demo_wait_for()
    await demo_timeout_ctx()


asyncio.run(main())
```

**追问**:1) wait_for 传 None 会怎样?——等价于不设超时,直接 await;所以"可选超时"场景写 wait_for(op, timeout or None) 是安全的,但绝不能传 0(立即取消)。2) 两代 API 的差别?——wait_for 包一层 Task 取消;asyncio.timeout(3.11+)是上下文管理器,块内所有 await 共享预算、超时抛 TimeoutError(内层 Canc 困惑减少)、与 TaskGroup 组合更自然。3) 迁移建议?——新代码用 asyncio.timeout;wait_for 的「取消已发但任务可能完成」竞态(timeout 后 result 仍可能取到)要理解。4) 生产陷阱?——wait_for(op, 0) 立即取消;timeout 块内吞 CancelledError 混淆超时与外部取消(Q589);嵌套 wait_for 预算叠加。

---
