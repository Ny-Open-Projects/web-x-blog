---
title: [Q433] GeneratorExit 与生成器的清理语义
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q433 · GeneratorExit 与生成器的清理语义

> 难度:★★★☆ | 标签:生成器, 异常, 资源管理

**问**:GeneratorExit 为什么继承 BaseException 而不是 Exception?生成器的清理代码应该怎么写才可靠?

**答**:GeneratorExit 是解释器注入的控制流信号,不是程序错误;继承 BaseException 是为了绕开 `except Exception` 这类兜底捕获,防止业务代码误吞关闭信号。生成器被 close、被 GC 回收、所在 with 块退出时都会触发它。可靠写法是在生成器里用 try/finally(或 try/except GeneratorExit + re-raise)放置清理逻辑,清理完必须让 GeneratorExit 继续传播;捕获后不抛、继续 yield 是协议错误。

```python
# file: code/01_语言核心与底层/q433_generator_exit.py
import gc

def track():
    try:
        yield 1
        yield 2
    except GeneratorExit:
        print("[cleanup] GeneratorExit caught, releasing resource")
        raise                     # 必须重新抛出,让 close 正常收尾

if __name__ == "__main__":
    g = track()
    print(next(g))
    g.close()                     # 显式关闭:清理代码在此执行

    g2 = track()
    print(next(g2))
    del g2                        # CPython 引用归零,立即触发隐式 close
    gc.collect()                  # 其他实现依赖 GC,这里兜底
    print("done")
```

**追问**:1) 为什么 with 块退出也和它有关?——@contextmanager 装饰的生成器上下文管理器在 __exit__ 异常路径上靠 throw 注入异常、正常路径靠 close 触发清理,GeneratorExit 是这套机制的地基。2) 为什么它继承 BaseException 而非 Exception?——它是解释器注入的控制流信号,继承 Exception 会被 `except Exception` 兜底误吞导致 close 失败;CancelledError(3.8+)同理也放在 BaseException 下。3) 隐式 close 在什么时机触发?——生成器对象销毁时 CPython 立即调用 gen_close;有循环引用时推迟到 GC;异步生成器由 loop.shutdown_asyncgens 兜底,这是 asyncio.run 退出时的固定动作。4) 生产陷阱?——在 finally 里做无超时的阻塞清理,close 时整个程序卡死;清理要幂等、短小,长清理交给显式生命周期管理。
