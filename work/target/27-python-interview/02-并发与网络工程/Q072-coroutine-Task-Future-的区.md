---
title: [Q072] coroutine / Task / Future 的区别
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q072 · coroutine / Task / Future 的区别

> 难度:★★★ | 标签:asyncio, coroutine, Task, Future

**问**:coroutine、Task、Future 三者是什么关系?什么时候需要把协程包成 Task?

**答**:coroutine 是用 async def 定义的、可暂停恢复的函数,自身不执行,调用只产生协程对象;Task 继承自 Future,是把协程"排入事件循环立即执行"的载体,创建即调度;Future 是更底层的"结果占位",一般由库代码完成并 set_result。需要并发运行一个协程时用 `asyncio.create_task`,只 await 它则只是顺序执行。

```python
# file: code/02_并发与网络工程/q072_coro_task_future.py
import asyncio


async def job(name: str) -> str:
    await asyncio.sleep(0.2)
    return f"{name} done"


async def main() -> None:
    coro = job("裸协程")          # 不会执行
    task = asyncio.create_task(job("任务"))  # 创建即调度

    # 裸协程需要 await 才执行: 顺序执行
    print("await 裸协程:", await coro)
    print("await Task:", await task)

    # 更底层的 Future 手动控制完成
    fut: asyncio.Future[str] = asyncio.get_running_loop().create_future()
    fut.set_result("future 完成")
    print("await Future:", await fut)


if __name__ == "__main__":
    asyncio.run(main())
```

**追问**:
- create_task 后不保存引用会怎样?——事件循环只持弱引用,任务可能被 GC 静默回收;官方文档要求保存引用(集合 + done_callback 清理)。
- ensure_future 和 create_task 的区别?——ensure_future 接受任意 awaitable 并包装,历史 API;create_task 只接受协程、语义更明确,新代码用它。
- Task 什么时候真正开始跑?——create_task 只是 call_soon 排入就绪队列,当前协程让出控制权(遇到 await)后才开始执行。

---
