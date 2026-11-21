---
title: [Q2404] shutdown_asyncgens 语义
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2404 · shutdown_asyncgens 语义

> 难度:★★★★ | 标签:异步生成器, 资源清理, 事件循环

**问**:async for 中途 break 之后,异步生成器的 finally 什么时候执行?

**答**:break 后生成器悬在 yield 点,finally 不会立刻执行;它被回收靠两条路:GC 触发钩子,或循环关闭前的 shutdown_asyncgens 大扫除。

- 实测持引用阻止 GC 提前收尸:run 结束时日志只有"资源打开",finally 缺席;

- loop.run_until_complete(loop.shutdown_asyncgens()) 后"资源关闭"出现,恰好一次;

- asyncio.run 的收尾序列自动包含这一步,实测 abandon 的生成器在 run 返回前被送终;

- 手动管理事件循环时要自己补这一课,否则文件句柄、连接这类资源悬到进程退出。

```python
# file: code/02_并发与网络工程/q2404_shutdown_asyncgens.py
# -*- coding: utf-8 -*-
"""shutdown_asyncgens 语义: 悬空的异步生成器, 由循环统一送终。

- break 出 async for 后, 生成器停在 yield 点, finally 不会立刻执行;
- 若还有引用兜着, GC 不来收, 资源就一直悬着, 直到循环关闭前的大扫除;
- asyncio.run 会自动调 shutdown_asyncgens, 手动管理循环时要自己补这一课。
"""
import asyncio

log = []


async def resource_gen():
    try:
        log.append("资源打开")
        yield 1
        yield 2
        yield 3
    finally:
        log.append("资源关闭")


async def use_partially(gen):
    async for x in gen:
        break                       # 只拿一个就走人, 生成器悬在 yield 点


def manual_loop_demo():
    log.clear()
    gen = resource_gen()            # 关键: 持引用, GC 不会提前收尸
    loop = asyncio.new_event_loop()
    try:
        loop.run_until_complete(use_partially(gen))
        before = list(log)
        loop.run_until_complete(loop.shutdown_asyncgens())
        after = list(log)
    finally:
        loop.close()
    print("run 结束时:", before)
    print("shutdown 后:", after)
    assert "资源关闭" not in before, "悬空生成器不会自己收尾"
    assert "资源关闭" in after, "shutdown_asyncgens 必须送终"
    assert after.count("资源关闭") == 1, "收尾恰好一次"


def asyncio_run_demo():
    log.clear()
    holder = {}
    gen = resource_gen()
    holder["g"] = gen               # 持引用防 GC 提前收尸

    async def main():
        async for x in gen:
            break

    asyncio.run(main())
    print("asyncio.run 返回后:", list(log))
    assert "资源关闭" in log, "run 的收尾序列自带 shutdown_asyncgens"


def main_entry():
    manual_loop_demo()
    asyncio_run_demo()


if __name__ == "__main__":
    main_entry()
```

**追问**:1) GC 那条路为什么不可靠?——CPython 引用计数能及时触发,但循环引用要等分代回收,时机不定;持引用时永远不会触发,资源悬死。2) shutdown_asyncgens 会等生成器收尾完成吗?——会,它逐个 await aclose 并收集异常,finally 里的清理真实跑完。3) shutdown_asyncgens 与 GC 两条路的可靠性差异?——GC 路径:引用计数及时触发但循环引用等分代、持引用永不触发——时机不确定;shutdown_asyncgens 逐个 await aclose,finally 真实跑完且时机确定(asyncio.run 自动调,Q2402 收尾序列)——「确定的关闭时机」只有显式调用。4) break 后的资源悬置怎么防?——显式 await agen.aclose()(立即确定,Q1862);或用 contextlib.aclosing 包装(async with 自动 aclose);持引用的场景(调试器/日志)尤其要显式——「aclosing」是异步生成器的 with 等价物。5) 生产陷阱?——break 后不 aclose(文件句柄/连接悬到进程退出);手动管理循环漏 shutdown_asyncgens(Q2404 原问);finally 里做慢 IO(收尾卡死);aclose 后再 asend(不可复活);以为 GC 会兜底(循环引用+持引用都是黑洞)。

---
