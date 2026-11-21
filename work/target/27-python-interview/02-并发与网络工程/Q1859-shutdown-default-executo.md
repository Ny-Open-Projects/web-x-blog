---
title: [Q1859] shutdown_default_executor 语义:默认执行器线程的收尾责任人
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1859 · shutdown_default_executor 语义:默认执行器线程的收尾责任人

> 难度:★★☆ | 标签:asyncio, 线程池, 优雅关闭

**问**:asyncio.run 跑完进程干干净净,自己 new loop 跑 run_in_executor 线程却还挂着,差别在哪?

**答**:差别是默认执行器的收尾责任:loop.run_in_executor(None, ...) 惰性创建默认执行器线程,任务跑完线程并不消失,必须有人显式 await loop.shutdown_default_executor() 才会收走。

- 手动管理 loop 的场景(run_until_complete 自己写主循环)要自己调 shutdown_default_executor,实测收尾后活跃线程数回到基线;

- asyncio.run 从 Python 3.9 起在退出前自动调用它,这是两种跑法最容易被忽略的差别;

- 线程名以 asyncio_ 开头,可以作为监控里 '默认执行器泄漏' 的识别特征。

自研的执行器(run_in_executor 传自定义 ThreadPoolExecutor)不受此管理,要自己 shutdown(wait=True)。

```python
# file: code/02_并发与网络工程/q1859_shutdown_executor.py
# -*- coding: utf-8 -*-
"""shutdown_default_executor 语义: 默认执行器线程的收尾责任人。

- loop.run_in_executor(None, ...) 惰性创建默认执行器线程, 任务跑完线程还挂着;
- 手动管理 loop 时必须显式 await loop.shutdown_default_executor() 才能收走线程;
- asyncio.run 从 3.9 起在退出前自动调用它, 这是两种跑法的核心差别。
"""
import asyncio
import threading
import time


def blocking_job():
    time.sleep(0.25)
    return threading.current_thread().name      # 默认执行器线程名 asyncio_0


async def use_default_executor():
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, blocking_job)


def main():
    baseline = threading.active_count()

    # 场景一: 手动管理 loop, 必须显式 shutdown
    loop = asyncio.new_event_loop()
    try:
        name = loop.run_until_complete(use_default_executor())
        during = threading.active_count()
        loop.run_until_complete(loop.shutdown_default_executor())
        after = threading.active_count()
    finally:
        loop.close()
    print("手动 loop: 执行线程=%s, 执行后活跃线程=%d, shutdown后=%d"
          % (name, during, after))
    assert name.startswith("asyncio_"), "默认执行器线程名以 asyncio_ 开头"
    assert during == baseline + 1, "执行器线程已创建"
    assert after == baseline, "shutdown_default_executor 负责收走线程"

    # 场景二: asyncio.run 自动收尾, 无需手动调用
    def run_and_count():
        asyncio.run(use_default_executor())
        return threading.active_count()

    after_b = run_and_count()
    print("asyncio.run 之后活跃线程: %d (基线 %d)" % (after_b, baseline))
    assert after_b == baseline, "asyncio.run 退出前自动 shutdown 默认执行器"

    print("结论: 默认执行器不会自己消失, 收尾责任在 loop 的主人")


if __name__ == "__main__":
    main()
```

**追问**:1) 不 shutdown 会怎样?——线程常驻到解释器退出,threading._shutdown 会 join 它们,进程退出可能被卡住;更麻烦的是 executor 里残留未执行的任务,资源(连接、句柄)不释放。2) 默认执行器线程的生命周期为什么容易漏?——run_in_executor(None) 惰性创建,任务完成线程不回收;asyncio.run(3.9+)自动 shutdown_default_executor,自管 loop 不会——「框架替你收尾」的隐性差异,迁移到自管 loop 时最容易漏。3) 自建 ThreadPoolExecutor 的收尾与默认执行器怎么统一?——显式 executor 要 await loop.run_in_executor 后 executor.shutdown(wait=True)(或在 loop 关闭前);默认执行器只认 shutdown_default_executor;两类都要纳入统一的「关闭序列」(Q1588 的后台任务收编)。4) 生产陷阱?——不 shutdown(线程常驻+解释器退出时 threading._shutdown join 卡住,见原问);shutdown 时 executor 里还有未执行任务(丢失,要先排空);线程名观测缺失(泄漏发现不了);shutdown_default_executor 在 loop 已关闭后调用(RuntimeError)。


---
