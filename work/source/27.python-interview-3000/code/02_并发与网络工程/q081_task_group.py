import asyncio
import sys


async def fetch(i: int) -> str:
    await asyncio.sleep(0.2)
    if i == 1:
        raise ValueError(f"任务 {i} 失败")
    return f"result-{i}"


# TaskGroup/except* 是 3.11+ 语法级特性, 放字符串按需编译
TASKGROUP_DEMO = '''
async def main() -> None:
    try:
        async with asyncio.TaskGroup() as tg:
            tasks = [tg.create_task(fetch(i), name=f"fetch-{i}") for i in range(4)]
            # 出 with 时: 要么全部成功, 要么取消全部并抛 ExceptionGroup
        print("全部成功:", [t.result() for t in tasks])
    except* ValueError as eg:
        print("捕获 ExceptionGroup 中的 ValueError:", [str(e) for e in eg.exceptions])
        # 失败时其余任务已被自动取消
    except* RuntimeError as eg:
        print("RuntimeError:", eg.exceptions)
'''


async def main_compat() -> None:
    # 3.11 以下等价演示: gather + return_exceptions 汇总全部异常
    tasks = [asyncio.create_task(fetch(i), name=f"fetch-{i}") for i in range(4)]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    errors = [r for r in results if isinstance(r, Exception)]
    if errors:
        print("等价演示捕获异常:", [str(e) for e in errors], "(TaskGroup 会同时取消其余任务)")
    else:
        print("全部成功:", results)


if __name__ == "__main__":
    if sys.version_info >= (3, 11):
        exec(compile(TASKGROUP_DEMO, "<taskgroup_demo>", "exec"), globals())
        asyncio.run(main())  # noqa: F821  由 TASKGROUP_DEMO 动态定义
    else:
        print(
            f"TaskGroup/except*/ExceptionGroup 需要 Python 3.11+, "
            f"当前 {sys.version_info.major}.{sys.version_info.minor}, "
            f"演示跳过, 改用 gather 等价演示"
        )
        asyncio.run(main_compat())
