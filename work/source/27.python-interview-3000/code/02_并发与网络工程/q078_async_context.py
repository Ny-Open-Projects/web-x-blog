import asyncio
from contextlib import asynccontextmanager


class AsyncConnection:
    async def __aenter__(self) -> "AsyncConnection":
        await asyncio.sleep(0.1)  # 模拟建连
        print("连接建立")
        return self

    async def __aexit__(self, exc_type, exc, tb) -> bool:
        await asyncio.sleep(0.05)  # 模拟关闭
        print("连接关闭, 异常:", exc_type.__name__ if exc_type else None)
        return False  # 不吞异常


@asynccontextmanager
async def timer(label: str):
    start = asyncio.get_running_loop().time()
    try:
        yield
    finally:
        elapsed = asyncio.get_running_loop().time() - start
        print(f"[{label}] 耗时 {elapsed:.2f}s")


async def main() -> None:
    async with AsyncConnection() as conn, timer("业务块"):
        await asyncio.sleep(0.2)
        print("业务执行中")


if __name__ == "__main__":
    asyncio.run(main())
