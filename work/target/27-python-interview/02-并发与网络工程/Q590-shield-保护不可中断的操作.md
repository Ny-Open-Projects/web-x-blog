---
title: [Q590] shield:保护不可中断的操作
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q590 · shield:保护不可中断的操作

> 难度:★★★☆ | 标签:shield, 取消, asyncio

**问**:取消风暴里,怎么保证"写审计日志"这类必须完成的操作不被打断?

**答**:`asyncio.shield(inner)` 给内部任务加一层壳:取消打到 shield 所在的外层 await 点,CancelledError 在外层抛出,但 inner 任务继续运行不受影响。要理解两个细节:shield 保护的是 inner 这个 task 对象,如果你 cancel 的是 inner 本身,shield 挡不住;外层被取消后想拿 inner 的结果,要继续 await inner。典型用途:优雅关闭时把"落盘/提交事务"包进 shield,或者反向——超时放弃等待但让任务在后台继续。

```python
# file: code/02_并发与网络工程/q590_shield.py
import asyncio


async def critical_flush() -> str:
    await asyncio.sleep(0.3)  # 模拟不可中断的落盘
    print("critical_flush: 状态已落盘")
    return "saved"


async def main() -> None:
    inner = asyncio.create_task(critical_flush())

    async def outer() -> None:
        # 正确姿势: 在外层 await 点 await shield(...)。
        # 注意 shield 返回的是 Future 不是协程, 不能再丢给 create_task
        # (TypeError: a coroutine was expected); 传 Task 或裸协程都可以。
        return await asyncio.shield(inner)

    outer_task = asyncio.create_task(outer())
    await asyncio.sleep(0.05)
    outer_task.cancel()  # 取消外层
    try:
        await outer_task
    except asyncio.CancelledError:
        print("outer 被取消, 但 inner 仍在跑")

    result = await inner  # 继续等受保护任务
    print("最终结果:", result)

    # 对照: 直接 cancel inner 则 shield 无能为力
    inner2 = asyncio.create_task(critical_flush())

    async def outer2() -> None:
        return await asyncio.shield(inner2)

    shielded = asyncio.create_task(outer2())
    inner2.cancel()
    try:
        await shielded
    except asyncio.CancelledError:
        print("cancel inner: shield 也挡不住 (保护的是外层取消)")


if __name__ == "__main__":
    asyncio.run(main())
```

**追问**:1) uncancel() 是干嘛的?——Python 3.11 给 Task 加了取消计数,在捕获 CancelledError 后做不含 await 的清理时调用 `task.uncancel()` 可避免外层把"本次取消"误记,但要非常谨慎,通常直接 re-raise 才是对的。2) shield 的真实边界?——只保护「这个 await 点」:外层取消仍会在 shield 完成后把外层协程取消;shield 内启动的新任务不在保护范围;清理段要短且幂等(Q589)。3) 与 TaskGroup 的配合?——TaskGroup 取消树下,shield 段内的异常仍会进组;uncancel 用于「接管取消」的高级场景(服务器连接处理);3.11 前 cancelling 计数没有,行为靠协议。4) 生产陷阱?——shield 包整个长任务(等于吞取消);uncancel 后不 re-raise 让取消凭空消失;清理段里再 await 无 shield。

---
