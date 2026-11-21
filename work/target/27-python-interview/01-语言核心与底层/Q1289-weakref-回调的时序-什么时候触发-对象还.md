---
title: [Q1289] weakref 回调的时序:什么时候触发、对象还算活着吗
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1289 · weakref 回调的时序:什么时候触发、对象还算活着吗

> 难度:★★★★☆ | 标签:weakref, 终结, 时序

**问**:`weakref.ref(obj, callback)` 的回调什么时候跑?跑的时候 obj 还能访问吗?回调里抛异常会怎样?

**答**:回调在「对象真正死亡」的瞬间同步触发:CPython 引用计数归零时,先执行 `__del__`,再清弱引用并逐个调用回调——所以回调里 `r()` 返回 None,对象已不可访问(与 weakref.finalize 的时机一致,两者都在终结后)。这个时序有两个推论:回调可以安全地做「登记对象已释放」类清理,但绝不能试图访问或复活对象;触发点在任意代码路径中间(比如某个函数刚做完最后一次引用的 del),回调里不要做重活或拿锁,否则随机位置出现执行延迟。回调抛出的异常不会传播——解释器把 traceback 打到 stderr 后继续运行,排查「回调没生效」时先看 stderr。与 finalize 的分工:需要「带参数的清理」用 finalize(避免持有 obj 强引用的闭包),需要「感知死亡」用 ref 回调。

```python
# file: code/01_语言核心与底层/q1289_weakref_callback_timing.py
import gc
import weakref

events = []


class Sensor:
    def __del__(self):
        events.append("del")


if __name__ == "__main__":
    s = Sensor()
    ref = weakref.ref(s, lambda r: events.append(
        "cb, obj %s" % ("dead" if r() is None else "ALIVE")))
    del s
    print("refcount death, synchronous:", events)
    events.clear()

    o = Sensor()
    weakref.ref(o, lambda r: 1 / 0)     # 回调里抛异常
    del o
    print("callback exception swallowed, program continues")
    print("finalize 与 ref 回调时机一致: 都在 __del__ 之后", )
    del events[:]
```

**追问**:1) 为什么回调里 `r()` 一定是 None?——弱引用的清空与回调调用在同一临界步骤里完成,回调被调用即意味着弱引用已失效,不存在「回调里还能摸到对象」的窗口。2) 触发时机?——对象终结(引用归零或 GC 处理)时同步调用回调;回调拿到的只是 ref 本身;若需要数据,用 weakref.finalize 传附加参数(不引用目标)。3) 与 finalize 的选择?——weakref.ref(callback=) 灵活但时序微妙;finalize 保证恰好一次、可 detach、可带参数,资源清理优先 finalize(Q488)。4) 生产陷阱?——回调闭包引用目标对象导致永不回收(头号陷阱);回调抛异常只打印易被忽视;以为「回调未触发=对象还活着」(可能只是 GC 未跑)。
