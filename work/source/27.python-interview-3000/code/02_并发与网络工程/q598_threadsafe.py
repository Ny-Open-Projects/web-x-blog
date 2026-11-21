import asyncio
import concurrent.futures
import threading

table: dict = {}


async def update_and_read(key: str) -> int:
    await asyncio.sleep(0.01)  # 模拟异步处理
    table[key] = table.get(key, 0) + 1
    return table[key]


def callback_thread(loop, n: int) -> None:
    """模拟第三方 SDK 的回调线程。"""
    for i in range(n):
        fut = asyncio.run_coroutine_threadsafe(update_and_read(f"k{i % 3}"), loop)
        try:
            value = fut.result(timeout=2)  # concurrent.futures.Future
            print(f"[thread] 回调 {i} 处理完成, 值={value}")
        except concurrent.futures.TimeoutError:
            # 3.9 里它不是内建 TimeoutError, 捕错类型会漏接并炸掉线程
            print("[thread] 投递超时: loop 卡死或未运行")


async def main() -> None:
    loop = asyncio.get_running_loop()
    t = threading.Thread(target=callback_thread, args=(loop, 6))
    t.start()
    # 同时 loop 自己也在跑别的协程, 证明共享同一个循环。
    # 不能直接 t.join(): join 阻塞事件循环线程, 线程侧 fut.result()
    # 就永远等不到派发, 自我死锁到超时; 循环侧必须让出控制权轮询。
    while t.is_alive():
        await asyncio.sleep(0.01)
    t.join()
    print("最终 table:", table)
    assert all(v == 2 for v in table.values()), "每个 key 被处理 2 次"


if __name__ == "__main__":
    asyncio.run(main())
