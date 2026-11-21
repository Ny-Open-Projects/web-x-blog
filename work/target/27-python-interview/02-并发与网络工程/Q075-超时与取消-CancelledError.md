---
title: [Q075] 超时与取消 CancelledError
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q075 · 超时与取消 CancelledError

> 难度:★★★★ | 标签:asyncio, 超时, 取消, CancelledError

**问**:asyncio 如何给操作加超时?取消时 CancelledError 该如何处理?

**答**:用 `asyncio.timeout`(3.11+)或 `wait_for` 限时,超时会向协程注入 CancelledError。处理取消的规则:捕获 CancelledError 后必须重新抛出(或用 shield 保护关键清理),在 finally 里释放资源;`asyncio.shield` 可让"不可中断的收尾操作"不被取消波及。吞掉 CancelledError 是常见反模式,会破坏上层取消传播。注意 `asyncio.timeout` 是 3.11 新增 API,低版本直接 AttributeError,应按版本分流:3.11+ 用 timeout 上下文管理器,老版本用 wait_for 等价演示。

```python
# file: code/02_并发与网络工程/q075_timeout_cancel.py
import asyncio
import sys


async def slow_io() -> str:
    try:
        print("开始慢 IO")
        await asyncio.sleep(10)
        return "完成"
    except asyncio.CancelledError:
        print("收到取消, 做清理")
        await asyncio.shield(asyncio.sleep(0.05))  # 保护关键清理不被再次取消
        print("清理完成")
        raise  # 必须重新抛出


async def demo_wait_for() -> None:
    # wait_for 等价老写法, 3.8+ 全版本可用
    try:
        await asyncio.wait_for(slow_io(), timeout=0.3)
    except asyncio.TimeoutError:
        print("整体超时(wait_for 等价演示)")


async def main() -> None:
    if sys.version_info >= (3, 11):
        try:
            async with asyncio.timeout(0.3):  # 3.11+ 写法
                result = await slow_io()
                print(result)
        except TimeoutError:
            print("整体超时")
    else:
        print(
            f"asyncio.timeout 需要 Python 3.11+, "
            f"当前 {sys.version_info.major}.{sys.version_info.minor}, "
            f"演示跳过, 改用 wait_for 等价演示"
        )
        await demo_wait_for()

    # wait_for 超时语义再单独演示一次
    try:
        await asyncio.wait_for(asyncio.sleep(5), timeout=0.2)
    except asyncio.TimeoutError:
        print("wait_for 超时")


if __name__ == "__main__":
    asyncio.run(main())
```

**追问**:
- Task.cancel 和给 Future set_exception 的区别?——cancel 会向协程在当前 await 点抛 CancelledError,是协作式中断;它返回的 Future 状态变为 cancelled。
- CancelledError 在 3.8 前后有什么变化?——3.8 起改为继承 BaseException,`except Exception` 不再误吞取消,但仍可能被裸 except 吞掉。
- shield 的正确用法?——只保护「必须完成的清理段」,外层仍捕获 CancelledError;整段 shield 等于拒绝取消。
- 超时之后任务还活着吗?——wait_for 超时会 cancel 内部任务;asyncio.timeout 只是注入取消,任务必须 re-raise 才真正终止。
