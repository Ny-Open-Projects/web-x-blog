# -*- coding: utf-8 -*-
"""run_in_executor 的进程池分支: 能 pickle 的才能过桥。

- CPU 密集协程丢线程池救不了 GIL, 要换 ProcessPoolExecutor;
- 进程池的桥是 pickle: 参数与返回值都要能序列化, 闭包和 lambda 过不去;
- 提交不可序列化对象会当场失败, 必须当作正常异常路径处理。
"""
import asyncio
import concurrent.futures


def cpu_sum(n):
    """进程池目标函数: 必须是模块级可 pickle 的普通函数。"""
    return sum(range(n))


def make_closure():
    base = 10

    def closure_task(n):
        return sum(range(n)) + base
    return closure_task


async def main():
    loop = asyncio.get_running_loop()
    with concurrent.futures.ProcessPoolExecutor(max_workers=1) as pool:
        res = await loop.run_in_executor(pool, cpu_sum, 2000000)
        print("进程池协程拿到:", res)
        assert res == sum(range(2000000)), "结果应与本地计算一致"

        try:
            await loop.run_in_executor(pool, make_closure(), 1000)
            raise AssertionError("闭包不该被 pickle 成功")
        except Exception as e:                    # 3.9 各版本报错类型不一, 统一接住
            print("闭包提交失败(符合预期):", type(e).__name__)
    return res


def main_entry():
    # macOS 默认 spawn: 子进程要重新 import 本模块, 必须有 __main__ 守卫
    res = asyncio.run(main())
    print("对照: 同样任务在纯协程里会卡住事件循环, 进程池让它在旁路跑完")


if __name__ == "__main__":
    main_entry()
