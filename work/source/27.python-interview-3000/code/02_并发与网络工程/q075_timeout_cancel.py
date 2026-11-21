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
