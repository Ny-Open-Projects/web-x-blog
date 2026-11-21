---
title: [Q2679] 自定义 Task 工厂:set_task_factory 给每个任务挂档案
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2679 · 自定义 Task 工厂:set_task_factory 给每个任务挂档案

> 难度:★★★★ | 标签:task factory, 可观测性, 任务档案

**问**:想对所有 asyncio.Task 的创建做登记,有什么必经之路?

**答**:loop.set_task_factory:工厂在每次 create_task 时被调用,任务创建一个不漏。工厂里登记出生时刻,done_callback 注销死亡,就得到一份实时在途任务清单。实测 0.1 秒时清单里只剩没跑完的 slow 与 mid,收尾后注册表归零。3.9 有个坑:自定义工厂会忽略 create_task 的 name 参数,名字得让协程自己用current_task().set_name 挂。

- 工厂是任务可观测性的入口:看门狗、泄漏检测、慢任务报告都从这里拿数据;

- 登记要用 task 对象做键,别用名字——名字会变,对象身份不会;

- done_callback 里只做注销这类轻活,重活交给队列;

- 工厂必须返回 Task,忘记返回会得到 None 引发连锁错误。

```python
# file: code/02_并发与网络工程/q2679_task_factory.py
# -*- coding: utf-8 -*-
"""自定义 Task 工厂: set_task_factory 给每个任务挂档案。

- 工厂在 create_task 时被调用: 任务创建的必经之路, 一个不漏;
- 按 task 对象登记, done_callback 注销, 得到实时在途清单;
- 3.9 注意: 自定义工厂会忽略 create_task 的 name 参数, 名字让协程自己报。
"""
import asyncio

REGISTRY = {}


def factory(loop, coro):
    task = asyncio.Task(coro, loop=loop)
    REGISTRY[task] = loop.time()             # 出生登记
    task.add_done_callback(REGISTRY.pop)     # 死亡注销, 按对象键删除
    return task


async def worker(name, dur):
    asyncio.current_task().set_name(name)    # 3.9 下名字得自己挂
    await asyncio.sleep(dur)
    return name


async def main():
    loop = asyncio.get_running_loop()
    loop.set_task_factory(factory)

    t1 = asyncio.create_task(worker("fast", 0.05))
    t2 = asyncio.create_task(worker("slow", 0.3))
    t3 = asyncio.create_task(worker("mid", 0.2))

    await asyncio.sleep(0.1)                 # fast 已完成
    live = sorted(t.get_name() for t in REGISTRY if not t.done())
    print("0.1s 时在途任务:", live)
    print("fast 已完成:", t1.done(), "/ slow 仍在途:", not t2.done())

    await asyncio.gather(t2, t3)
    print("收尾后注册表大小:", len(REGISTRY), "(全部被 done_callback 注销)")
    print("要点: 工厂是任务的可观测性入口, 档案挂上后想怎么巡检都行")


if __name__ == "__main__":
    asyncio.run(main())
```

**追问**:1) 工厂能替换 Task 实现吗?——能,可以返回自定义子类,埋点、统计、调试钩子都在构造与回调里加。2) 登记表会不会泄漏?——不会,done_callback 注销是出生登记的对偶,只要任务终态必达,表就必然归零。3) 底层机制:工厂的调用时机与签名?——循环在每次 create_task/ensure_future 时以 (loop, coro) 调用工厂,必须返回 Task 实例;3.9 的自定义工厂忽略 create_task 的 name 参数,3.10+ 才把 name 传入;done_callback 在任务终态后由循环调用,只适合轻量注销。4) 生产陷阱?——工厂忘记 return Task,全部任务变 None 连锁报错;done_callback 里做重活拖慢循环;用任务名当登记键,重名互相覆盖,应以对象身份为键。

---
