# -*- coding: utf-8 -*-
"""asend 交互式协程: 向异步生成器注入值驱动状态机。

- asend(None) 完成首次启动, 之后 asend(v) 把 v 传给 yield 表达式的值;
- 生成器从"只吐数据"变成"边收边算"的会话对象;
- 第一次必须 None, 否则 TypeError; 内部 return 抛 StopAsyncIteration 收场。
"""
import asyncio


async def running_stats():
    """接收数值, 每次吐出当前个数与均值; 收到负数哨兵即结束。"""
    total = 0.0
    n = 0
    while True:
        v = yield {"n": n, "mean": total / n if n else None}
        if v is None or v < 0:
            return                      # 结束: 以 StopAsyncIteration 呈现
        total += v
        n += 1


async def main():
    gen = running_stats()
    first = await gen.asend(None)       # 启动: 必须传 None
    print("启动后首个产出:", first)

    for v in (10, 20, 30):
        out = await gen.asend(v)
        print("asend(%d) -> %s" % (v, out))

    try:
        fresh = running_stats()
        await fresh.asend(5)            # 未启动就注入非 None
        print("意外: 未启动也能非 None 启动")
    except TypeError as e:
        print("未启动非 None 注入被拒:", e)

    try:
        await gen.asend(-1)             # 哨兵: 内部 return
        print("意外: 哨兵没生效")
    except StopAsyncIteration:
        print("asend(-1) 触发内部 return -> StopAsyncIteration, 会话关闭")

    try:
        await gen.asend(99)
        print("意外: 结束后还能继续")
    except StopAsyncIteration:
        print("结束后再 asend 同样 StopAsyncIteration")


if __name__ == "__main__":
    asyncio.run(main())
