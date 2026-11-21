import asyncio
import logging
import time

logging.basicConfig(level=logging.WARNING, format="%(levelname)s %(message)s")


async def suspicious_task() -> None:
    time.sleep(0.3)  # 错误: async 函数里的阻塞调用


async def fast_task() -> None:
    await asyncio.sleep(0.01)


async def main() -> None:
    loop = asyncio.get_running_loop()
    loop.set_debug(True)                 # 打开 asyncio 调试
    loop.slow_callback_duration = 0.1    # 超过 100ms 的回调告警

    # 未 await 的协程: debug 模式会记录创建点并告警
    asyncio.ensure_future(fast_task())   # 有引用? ensure_future 返回值被丢弃 — 演示告警
    coro = fast_task()                   # 创建但从未 await
    del coro

    await suspicious_task()  # 触发 "Executing <Task ...> took 0.3s" 告警
    await fast_task()

    # 卡顿现场排查: 打印所有任务栈
    for t in asyncio.all_tasks():
        if t is not asyncio.current_task():
            print(f"任务 {t.get_name()} 状态 {t._state}")
    print("调试输出应包含 Executing ... took 与 never awaited 告警")


asyncio.run(main())
