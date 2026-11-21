---
title: [Q431] 生成器的 send:双工通信与预激
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q431 · 生成器的 send:双工通信与预激

> 难度:★★★☆ | 标签:生成器, 协程

**问**:生成器除了被 next 驱动,还能 send 值进去,这解决了什么问题?为什么第一次调用必须先 next 或 send(None)?

**答**:`send` 让数据可以双向流动:调用方传入的值成为当前挂起的 `yield` 表达式的求值结果,生成器据此分支,实现「有状态的消费者」。第一次调用时生成器还没执行到任何 yield,不存在「yield 表达式」可以接收值,所以只能 `send(None)`(等价于 next);对未启动的生成器 send 非 None 值会抛 TypeError。这个「先预激再使用」的约束是所有生成器协程库都要处理的问题,常见解法是预激装饰器或在首次 send 时自动判空。

```python
# file: code/01_语言核心与底层/q431_generator_send.py
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average          # send 进来的值成为这个表达式的值
        total += term
        count += 1
        average = total / count

if __name__ == "__main__":
    avg = averager()
    first = next(avg)                 # 预激:推进到第一个 yield,得到 None
    print("first yield:", first)
    print(avg.send(10))               # 10.0
    print(avg.send(20))               # 15.0
    print(avg.send(30))               # 20.0

    fresh = averager()
    try:
        fresh.send(1)                 # 未预激就 send 非空值
    except TypeError as e:
        print("must prime first:", e)
```

**追问**:1) send(None) 与 next 的关系?——完全等价,CPython 在生成器未启动时对非 None 的 send 直接抛 TypeError,因为此刻没有 yield 表达式可以充当接收点。2) 为什么会有「预激」问题,工程上怎么解?——启动前没有 yield 点可接收值,解法是预激装饰器自动 next 一次或封装成类;现代方案直接用 async 协程,await 语义天然规避了这个问题。3) send 在 CPython 里如何把值送进 yield 表达式?——gen_send_ex 恢复挂起帧时把传入值压到栈顶,yield 表达式的求值结果直接取它;只有首次 send(None) 走与 next 相同的启动路径。4) 生产陷阱?——多个消费者共享同一生成器实例,send/next 交错会让内部状态错位;生成器是单消费通道,要么独占要么改用队列。
