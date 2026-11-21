---
title: [Q2407] run_in_executor 的进程池分支
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2407 · run_in_executor 的进程池分支

> 难度:★★★ | 标签:run_in_executor, 进程池, pickle

**问**:CPU 密集的协程怎么不卡事件循环?线程池为什么救不了它?

**答**:线程池解决不了 GIL,纯 Python 的 CPU 任务丢线程池照样和循环抢 GIL;要换 ProcessPoolExecutor,让任务在子进程真并行。

- 实测:200 万求和丢进程池,协程拿到结果,事件循环全程不被阻塞;

- 进程池的桥是 pickle:参数与返回值都要能序列化,实测模块级普通函数顺利过桥;

- 实测闭包提交当场失败,提示不可序列化——这是正常异常路径,业务上要预先把闭包改成可传参的模块级函数;

- macOS 默认 spawn 启动子进程,目标函数所在模块会被重新导入,if __name__ == '__main__' 守卫是必需品。

```python
# file: code/02_并发与网络工程/q2407_run_in_executor_pool.py
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
```

**追问**:1) 进程池 worker 数怎么定?——CPU 核数封顶,每核一个,多了只在进程切换上浪费。2) 大结果返回会不会卡?——会,pickle 回传在循环线程反序列化,结果太大时考虑写临时文件传路径。3) pickle 桥的边界清单?——模块级普通函数过桥;闭包/lambda/带连接句柄的对象失败(当场 pickle 失败或 Secondary 异常,Q603 同口径);macOS 默认 spawn:目标函数所在模块重新导入,__main__ 守卫必需——「可序列化+可导入」是进程池任务的两个资格。4) worker 数与大结果的账?——worker=CPU 核数封顶(多了切进程浪费);大结果 pickle 回传在循环线程反序列化(卡循环):写临时文件传路径/分片返回——「返回值大小」是进程池桥接的隐性瓶颈。5) 生产陷阱?——CPU 任务丢线程池(GIL 救不了,见原问);闭包提交(pickle 失败);无 __main__ 守卫(spawn 递归导入);大结果直接回传(循环卡顿);进程池异常路径没处理(Secondary 异常 traceback 丢失);worker 数超核(切换开销)。

---
