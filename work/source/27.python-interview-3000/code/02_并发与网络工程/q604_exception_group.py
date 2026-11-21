import asyncio
import sys

# ExceptionGroup/except* 是 3.11+ 语法级特性, 放字符串按需编译
DEMO_311 = '''
async def worker(name: str, delay: float, exc: Exception | None) -> str:
    await asyncio.sleep(delay)
    if exc:
        raise exc
    return f"{name}-ok"


async def main() -> None:
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(worker("db", 0.05, ValueError("db 连接失败")))
            tg.create_task(worker("cache", 0.06, TimeoutError("cache 超时")))
            tg.create_task(worker("api", 0.07, ValueError("api 500")))
    except* ValueError as eg:
        print(f"ValueError 子组 ({len(eg.exceptions)} 个):",
              [str(e) for e in eg.exceptions])
    except* TimeoutError as eg:
        print("TimeoutError 子组:", [str(e) for e in eg.exceptions])

    print("三个失败都被独立捕获, 没有信息丢失")
'''


async def main_compat() -> None:
    """3.11 以下等价演示: gather(return_exceptions=True) 收集全部异常。"""
    from typing import Optional

    async def worker(name: str, delay: float, exc: Optional[Exception]) -> str:
        await asyncio.sleep(delay)
        if exc:
            raise exc
        return f"{name}-ok"

    results = await asyncio.gather(
        worker("db", 0.05, ValueError("db 连接失败")),
        worker("cache", 0.06, TimeoutError("cache 超时")),
        worker("api", 0.07, ValueError("api 500")),
        return_exceptions=True,
    )
    errors = [r for r in results if isinstance(r, Exception)]
    print(f"等价演示收集到 {len(errors)} 个异常:", [str(e) for e in errors])
    print("按类型子组拆分捕获要等 3.11+ 的 except*")


if __name__ == "__main__":
    if sys.version_info >= (3, 11):
        exec(compile(DEMO_311, "<exception_group_311>", "exec"), globals())
        asyncio.run(main())  # noqa: F821  由 DEMO_311 动态定义
    else:
        print(
            f"ExceptionGroup/except* 需要 Python 3.11+, "
            f"当前 {sys.version_info.major}.{sys.version_info.minor}, "
            f"演示跳过, 改用 gather(return_exceptions=True) 等价演示"
        )
        asyncio.run(main_compat())
