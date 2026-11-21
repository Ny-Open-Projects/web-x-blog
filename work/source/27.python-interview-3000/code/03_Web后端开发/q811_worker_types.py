import asyncio
import threading
import time

def sync_io(total: int, delay: float = 0.01) -> None:
    for _ in range(total):
        time.sleep(delay)          # 阻塞式 IO: 串行等待

async def async_io(total: int, delay: float = 0.01) -> None:
    await asyncio.gather(*(asyncio.sleep(delay) for _ in range(total)))

t0 = time.perf_counter()
sync_io(20)
t1 = time.perf_counter()
asyncio.run(async_io(20))
t2 = time.perf_counter()
print(f"sync 模型耗时 {t1 - t0:.2f}s, 事件循环耗时 {t2 - t1:.2f}s")
print("线程演示:", threading.active_count(), "个活动线程")
