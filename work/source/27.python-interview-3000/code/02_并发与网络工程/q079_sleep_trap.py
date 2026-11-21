import asyncio
import time


async def ticker() -> None:
    for i in range(6):
        print(f"tick {i}")
        await asyncio.sleep(0.1)


async def bad_blocker() -> None:
    print("坏例子: time.sleep 0.3s, ticker 应该卡住")
    time.sleep(0.3)


async def good_blocker() -> None:
    print("好例子: run_in_executor, ticker 继续跳")
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, time.sleep, 0.3)


async def main() -> None:
    await asyncio.gather(ticker(), bad_blocker())
    await asyncio.gather(ticker(), good_blocker())


if __name__ == "__main__":
    asyncio.run(main())
