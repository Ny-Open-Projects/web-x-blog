---
title: [Q073] async/await 执行模型
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q073 · async/await 执行模型

> 难度:★★★ | 标签:asyncio, async, await

**问**:await 到底做了什么?为什么 async 函数里同步调用阻塞函数会毁掉并发?

**答**:await 把控制权交还事件循环并挂起当前协程,直到等待的对象(另一个协程、Task、Future、IO)完成再从暂停点恢复;恢复时局部变量栈完好,类似生成器的 send。若在协程里直接调用 time.sleep、requests.get 这类同步阻塞函数,整个事件循环线程被占住,所有并发协程全部停摆。

```python
# file: code/02_并发与网络工程/q073_async_model.py
import asyncio
import time


async def blocking_way() -> float:
    start = time.perf_counter()
    for i in range(3):
        time.sleep(0.3)  # 错误: 同步阻塞事件循环
        print(f"阻塞式 第 {i} 次")
    return time.perf_counter() - start


async def async_way() -> float:
    start = time.perf_counter()
    await asyncio.gather(*(asyncio.sleep(0.3, result=i) for i in range(3)))
    print("异步式 三次等待重叠")
    return time.perf_counter() - start


async def main() -> None:
    t1 = await blocking_way()
    t2 = await async_way()
    print(f"阻塞式耗时 {t1:.2f}s, 异步式耗时 {t2:.2f}s")


if __name__ == "__main__":
    asyncio.run(main())
```

**追问**:
- await 一个普通同步函数会怎样?——同步函数不会被挂起,直接在事件循环线程里跑完,这就是「假异步」阻塞的常见来源。
- 协程里的异常去哪了?——沿 await 链向上传播;由 Task 承载时异常保留到被 await/观察时抛出,不观察则 GC 时打印 "Task exception was never retrieved"。
- `await asyncio.sleep(0)` 是干什么的?——主动让出一次控制权,给事件循环处理其他回调的机会,CPU 长段分片的惯用手法。

---
