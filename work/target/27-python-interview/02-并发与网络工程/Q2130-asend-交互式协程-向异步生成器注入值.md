---
title: [Q2130] asend 交互式协程:向异步生成器注入值
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2130 · asend 交互式协程:向异步生成器注入值

> 难度:★★★ | 标签:asend, 异步生成器, 会话

**问**:异步生成器只能往外吐数据吗?能不能把调用方的输入"喂"进去参与计算?

**答**:能,asend(v) 把 v 传给当前挂起的 yield 表达式,生成器从单向管道变成双向会话对象。

- 首次必须 asend(None) 启动,非 None 启动抛 TypeError,实测确认;

- 会话里调用方连发三个值,生成器吐出滚动个数与均值;

- 内部 return 以 StopAsyncIteration 呈现,哨兵模式干净收场;

- 结束后再 asend 同样 StopAsyncIteration,会话不可复活。

```python
# file: code/02_并发与网络工程/q2130_asend_interactive.py
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
```

**追问**:1) 这和直接写一个 async 类有什么区别?——asend 把控制流写成了"挂起点",暂停时零开销且天然支持取消传播,适合流式协议的请求应答对。2) asend 与 async for 能混用吗?——能,async for 等价于不断 anext,注入值得用显式 asend,两者别在同一个生成器上混着驱动。3) asend 的「挂起点」语义为什么适合流式协议?——生成器在 yield 处暂停,asend 注入请求→生成器产出响应→再暂停:请求-应答对的全部状态都在生成器帧里,无需类字段;暂停时零开销(不占线程/事件循环)且取消沿 await 传播——双向会话的最小封装。4) asend 与 async for 的混用禁忌?——async for 内部 anext=asend(None),与显式 asend(值) 混着驱动会让「注入值」落在错误的挂起点;同一生成器一种驱动方式;包装层(类)可以统一两种入口。5) 生产陷阱?——首次 asend 非 None(TypeError);StopAsyncIteration 后再 asend(会话不可复活);把生成器跨任务共享(两个驱动者交错 asend,状态错乱);return 值误解(在 StopIteration/StopAsyncIteration 的 value 属性里,不是返回值)。

---
