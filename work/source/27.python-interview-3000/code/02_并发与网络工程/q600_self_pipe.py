import asyncio
import threading
import time

fired_at: list = []


async def main() -> None:
    loop = asyncio.get_running_loop()

    async def idle_waiter() -> None:
        # 循环此刻没有任何 IO, 正阻塞在 select 上
        await asyncio.sleep(1.0)

    t0 = time.perf_counter()

    def fire_from_thread() -> None:
        time.sleep(0.2)  # 确保 loop 已进入空闲 select
        fired_at.append(time.perf_counter() - t0)
        loop.call_soon_threadsafe(
            lambda: fired_at.append(time.perf_counter() - t0)
        )

    threading.Thread(target=fire_from_thread).start()
    await asyncio.sleep(0.5)  # 期间 loop 空闲, 靠 self-pipe 被唤醒处理回调
    print("各时间点:", [f"{t:.2f}s" for t in fired_at])
    print("threadsafe 回调无需 IO 事件即可唤醒循环")


asyncio.run(main())
