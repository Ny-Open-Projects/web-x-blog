import asyncio
import time


async def workload(n: int) -> int:
    total = 0
    for i in range(n):
        await asyncio.sleep(0)  # 频繁让出, 压测循环调度
        total += i
    return total


async def bench(label: str) -> None:
    start = time.perf_counter()
    await asyncio.gather(*(workload(2000) for _ in range(100)))
    print(f"{label} 耗时 {time.perf_counter() - start:.2f}s")


def run_with_uvloop() -> None:
    try:
        import uvloop  # 第三方库, 未安装则跳过演示
    except ImportError:
        print("uvloop 未安装, 跳过 (pip install uvloop)")
        return
    uvloop.install()
    asyncio.run(bench("uvloop"))


if __name__ == "__main__":
    asyncio.run(bench("默认事件循环"))
    run_with_uvloop()
