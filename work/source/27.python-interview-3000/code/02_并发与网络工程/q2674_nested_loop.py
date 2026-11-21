# -*- coding: utf-8 -*-
"""双循环嵌套的禁止原因: RuntimeError 的现场与三条出路。

- 事件循环不可重入: 运行中的循环里再 run_until_complete / asyncio.run 直接拒绝;
- 硬套的语义也不成立: 外层 await 挂起时, 内层循环根本得不到运行权;
- 出路: 直接 await / 包成 Task / 换线程开独立循环。
"""
import asyncio
import threading


async def inner():
    await asyncio.sleep(0.01)
    return 42


async def show_the_walls():
    loop = asyncio.get_running_loop()
    c1 = inner()                             # 先造出协程对象
    try:
        asyncio.run(c1)                      # 在运行中的循环里再起 run
        print("asyncio.run 竟然成功了")
    except RuntimeError as e:
        print("asyncio.run 嵌套 ->", e)
    finally:
        c1.close()                           # 收掉没跑的协程, 免得刷警告

    c2 = inner()
    try:
        loop.run_until_complete(c2)          # 老式 API 同样拒绝
        print("run_until_complete 竟然成功了")
    except RuntimeError as e:
        print("run_until_complete 嵌套 ->", e)
    finally:
        c2.close()


async def the_three_exits():
    r1 = await inner()                       # 出路一: 直接 await
    print("出路一 直接 await:", r1)

    task = asyncio.get_running_loop().create_task(inner())
    r2 = await task                          # 出路二: 包成 Task 并发跑
    print("出路二 create_task:", r2)

    def fresh_loop_thread():
        return asyncio.run(inner())          # 出路三: 新线程新循环

    fut = asyncio.get_running_loop().run_in_executor(None, fresh_loop_thread)
    r3 = await fut
    print("出路三 独立线程新循环:", r3)


async def main():
    await show_the_walls()
    await the_three_exits()
    print("要点: 嵌套不是语法错误而是结构错误, 循环唯一且不可重入")


if __name__ == "__main__":
    asyncio.run(main())
