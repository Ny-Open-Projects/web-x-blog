---
title: [Q2689] 悬挂协程的检测钩子:任务档案 + cr_frame 尸检
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2689 · 悬挂协程的检测钩子:任务档案 + cr_frame 尸检

> 难度:★★★★ | 标签:协程悬挂, cr_frame, 任务工厂

**问**:一个协程没异常、不完成、占着连接,怎么知道它卡在哪一行?

**答**:两步:任务工厂在创建时登记出生时刻,巡检器扫出年龄超过阈值还没完成的任务;然后剖开它的 cr_frame——协程对象挂起的帧,f_lineno 就是它卡住的那一行。实测嫌疑协程卡 0.6 秒,巡检两次报告"已挂 0.36s/0.51s,卡在 suspect 的 await sleep 行",完成即注销。心跳看门狗知道"卡了",cr_frame 尸检知道"卡在哪"。

- task.get_coro().cr_frame 是协程的现场,只读检查安全;

- 巡检由循环内的独立协程定期跑,报告走日志,处置仍走取消;

- f_lineno 指向当前正挂起的 await 行,栈不深但足够定位;

- 误报控制:阈值要大于正常操作时长,慢任务要能自证心跳。

```python
# file: code/02_并发与网络工程/q2689_hang_detect.py
# -*- coding: utf-8 -*-
"""悬挂协程的检测钩子: 任务档案 + cr_frame 尸检。

- 任务工厂在创建时登记"出生时刻", 完成回调注销, 得到在途清单;
- 巡检器扫出"年龄超过阈值还没完"的任务, 直接剖开 cr_frame;
- cr_frame 的 f_lineno 就是它卡住的那一行, 尸检报告精确到行号。
"""
import asyncio
import os

BORN = {}                                # task -> 出生时刻
STUCK_LIMIT = 0.3


def factory(loop, coro):
    task = asyncio.Task(coro, loop=loop)
    BORN[task] = loop.time()
    task.add_done_callback(BORN.pop)
    return task


def inspect_stuck(now):
    report = []
    for t, born in BORN.items():
        if t.done():
            continue
        age = now - born
        if age <= STUCK_LIMIT:
            continue
        coro = t.get_coro()
        fr = getattr(coro, "cr_frame", None)
        if fr is not None:
            where = "%s:%d" % (os.path.basename(fr.f_code.co_filename),
                               fr.f_lineno)
        else:
            where = "unknown"
        report.append((t.get_name(), age, where))
    return report


async def suspect():
    await asyncio.sleep(0.6)             # 嫌疑犯: 卡在这一行 0.6 秒
    return "done"


async def healthy():
    await asyncio.sleep(0.05)
    return "ok"


async def main():
    loop = asyncio.get_running_loop()
    loop.set_task_factory(factory)

    bad = asyncio.create_task(suspect(), name="suspect")
    good = asyncio.create_task(healthy(), name="healthy")
    await good

    for _ in range(4):                   # 周期巡检
        await asyncio.sleep(0.15)
        for name, age, where in inspect_stuck(loop.time()):
            print("检测到悬挂: %s 已挂 %.2fs, 卡在 %s" % (name, age, where))

    await bad
    print("收尾后登记表大小:", len(BORN), "(完成即注销)")
    print("要点: 心跳看门狗知道'卡了', cr_frame 尸检知道'卡在哪'")


if __name__ == "__main__":
    asyncio.run(main())
```

**追问**:1) 能不能看到协程的完整调用栈?——能,沿 cr_frame.f_back 走是生成器/协程链,但跨 await 的逻辑栈 asyncio 没有完整保留。2) 为什么不能直接杀掉悬挂任务了事?——它可能持有连接与锁,尸检先确认卡点,再决定取消还是转移。3) 底层机制:cr_frame 的 f_lineno 为什么就是卡住的行?——协程在 await 让出时生成器帧冻结在当前字节码偏移,f_lineno 对应该偏移的源码行;巡检只读帧属性不改状态,是安全的尸检;多层嵌套时要沿 cr_await 逐层剖才能到最内层卡点。4) 生产陷阱?——阈值小于正常操作时长,慢任务被误报悬挂(要配合心跳自证);只剖最外层,行号停在 await 中转行,误判卡点;检测后直接 cancel 持锁协程,锁与连接的清理路径被打断。

---
