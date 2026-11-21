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
