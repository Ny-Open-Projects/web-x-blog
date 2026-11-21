---
title: [Q1587] Task 收尾纪律:done callback 与异常回收
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1587 · Task 收尾纪律:done callback 与异常回收

> 难度:★★★☆ | 标签:asyncio, Task, 异常

**问**:"Task exception was never retrieved" 这个警告什么时候出现?怎么系统地避免?

**答**:Task 的异常不会自己冒出来:没人调用 result() 或 exception(),任务对象销毁时循环就通过 exception_handler 上报这条警告。系统的收尾纪律三件事:持引用——创建后的 Task 放进集合,防止被 GC 静默吞掉;done callback——add_done_callback 是统一收尾入口,在里面取 result 或 exception,异常在这里被"领走"就不会成为孤儿;exception_handler 兜底——set_exception_handler 抓漏网的孤儿,接日志与告警。反面模式:create_task 后既不存引用也不挂回调,成功时无所谓,失败时异常无声消失,线上表现就是"任务莫名没跑"。

```python
# file: code/02_并发与网络工程/q1587_task_discipline.py
"""Task 收尾纪律: done callback 与异常回收。

Task 的异常不会自己冒出来: 没人 result()/exception(), 循环就通过
exception_handler 报 "Task exception was never retrieved"。
纪律三件事:
- 持引用: 防任务被 GC 静默吞掉;
- done callback: 收尾的统一入口, result() / exception() 都在这里取;
- exception_handler: 兜底哨兵, 专抓漏网的孤儿。
"""
import asyncio
import gc


async def boom():
    raise RuntimeError("后台任务炸了")


async def good():
    await asyncio.sleep(0.02)
    return "result"


async def main():
    loop = asyncio.get_running_loop()
    reported = []
    loop.set_exception_handler(lambda l, ctx: reported.append(ctx))

    # 反面: 创建后不持引用也不取异常 -> 孤儿任务
    # 刻意不绑定返回值: 任务完成后引用归零, __del__ 触发
    # "Task exception was never retrieved" 上报 exception_handler
    asyncio.create_task(boom())

    # 正面: done callback 是收尾统一入口
    captured = []

    def on_done(t):
        if t.cancelled():
            captured.append(("cancelled", None))
            return
        try:
            captured.append(("ok", t.result()))
        except Exception as e:
            captured.append(("error", e))

    t_err = asyncio.create_task(boom())
    t_ok = asyncio.create_task(good())
    t_err.add_done_callback(on_done)
    t_ok.add_done_callback(on_done)

    keepalive = [t_err, t_ok]               # 持引用防 GC
    await asyncio.sleep(0.05)
    gc.collect()                            # 兜底: 确保孤儿任务走到 __del__

    orphans = [ctx["exception"] for ctx in reported if "exception" in ctx]
    print("异常处理器抓到的孤儿:", orphans)
    print("done callback 收尾:", captured)
    assert any(isinstance(e, RuntimeError) for e in orphans), "孤儿异常应上报处理器"
    assert len(captured) == 2, "挂了回调的任务必须各收尾一次"
    assert captured[0][0] == "error" and captured[1][0] == "ok"
    print(keepalive)
    print("结论: done callback 管规范收尾, exception_handler 管兜底哨兵")


if __name__ == "__main__":
    asyncio.run(main())
```

**追问**:1) done callback 里再抛异常会怎样?——callback 的异常同样走 exception_handler 上报,不影响任务本身,但说明收尾逻辑自己有 bug。2) 异常为什么会被「吞」到销毁时才报?——Task 持有异常等调用方来取;无人取时,Task 对象被 GC 的瞬间,事件循环通过 exception_handler 报「never retrieved」——所以警告出现的时机与 GC 时机相关,可能滞后很久,监控要以「创建数 vs 收尾数」差值为准。3) 收尾三件套怎么落地成代码结构?——统一的 spawn 帮助函数(Q1588):创建即持引用+挂 done callback+注册 exception_handler;禁止裸 create_task 进业务代码(lint 规则可查)——把纪律固化在工具函数里比靠自觉靠谱。4) 生产陷阱?——done callback 里做重活阻塞循环;gather(return_exceptions=True) 后不再检查各任务异常(异常被「收集」但没人看);exception_handler 只打日志不告警(孤儿任务持续发生);持引用的集合在任务完成后没移除,内存滞留(Q080 三宗罪)。

---
