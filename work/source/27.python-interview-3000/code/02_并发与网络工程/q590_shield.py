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
