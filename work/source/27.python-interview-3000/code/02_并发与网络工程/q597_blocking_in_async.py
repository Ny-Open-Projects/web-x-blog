import asyncio
import threading
import time


class LegacySDK:
    """模拟只提供同步接口的第三方 SDK。"""

    def __init__(self) -> None:
        self._lock = threading.Lock()  # 线程安全性未知时按不安全处理
        self.calls = 0

    def blocking_query(self, key: str) -> str:
        with self._lock:
            time.sleep(0.05)  # 阻塞 50ms
            self.calls += 1
            return f"value-of-{key}"


async def main() -> None:
    sdk = LegacySDK()
    loop = asyncio.get_running_loop()

    # 错误姿势: 直接调用, 冻结事件循环 — 用心跳协程观察
    heartbeat_ticks = [0]

    async def heartbeat() -> None:
        while True:
            heartbeat_ticks[0] += 1
            await asyncio.sleep(0.01)

    hb = asyncio.create_task(heartbeat())
    t0 = time.perf_counter()
    sdk.blocking_query("direct")  # 阻塞 50ms, 心跳完全停止
    direct_dt = time.perf_counter() - t0
    ticks_during_direct = heartbeat_ticks[0]
    print(f"直接调用 {direct_dt * 1000:.0f}ms, 期间心跳仍在: {ticks_during_direct > 0}")

    # 正确姿势: run_in_executor + 显式线程池 (线程安全未知时按串行化处理)
    from concurrent.futures import ThreadPoolExecutor
    executor = ThreadPoolExecutor(max_workers=3, thread_name_prefix="sdk")
    t0 = time.perf_counter()
    results = await asyncio.gather(
        *[loop.run_in_executor(executor, sdk.blocking_query, f"k{i}")
          for i in range(3)]
    )
    par_dt = time.perf_counter() - t0
    hb.cancel()
    print(f"executor 并行 3 次: {par_dt * 1000:.0f}ms (约等于单次耗时)")
    print("结果:", results)
    executor.shutdown()


asyncio.run(main())
