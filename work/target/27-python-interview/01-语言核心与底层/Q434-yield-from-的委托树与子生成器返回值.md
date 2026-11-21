---
title: [Q434] yield from 的委托树与子生成器返回值
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q434 · yield from 的委托树与子生成器返回值

> 难度:★★★★ | 标签:生成器, yield from

**问**:多层 yield from 嵌套时,调用方的 send/throw 是如何「穿透」到最内层生成器的?子生成器 return 的值去了哪里?

**答**:yield from 在调用方与子生成器之间建立直通管道:next/send/throw 全部转发给子生成器,中间的委托生成器只是「转发站」,不参与数据的加工。委托链可以任意深,形成一棵树,树的根是驱动者,叶子是真正干活的生成器。子生成器 return 的值随 StopIteration.value 上浮,被 yield from 表达式捕获,成为委托生成器里的局部结果,层层向上直到根。这也是 async/await 的字节码原型:await 本质就是带协议校验的 yield from。

```python
# file: code/01_语言核心与底层/q434_yield_from_tree.py
def leaf(name):
    total = 0
    for _ in range(2):
        got = yield f"{name}-value"
        total += got or 0
    return f"{name} total={total}"        # return 值经 StopIteration.value 上浮

def middle():
    result = yield from leaf("A")         # 委托:转发 next/send/throw
    print("middle got:", result)
    result = yield from leaf("B")
    return result

if __name__ == "__main__":
    g = middle()
    print(next(g))                        # A-value
    print(g.send(1))                      # A-value
    print(g.send(2))                      # A 结束返回,委托切到 B:B-value
    print(g.send(3))                      # B-value
    try:
        g.send(4)
    except StopIteration as stop:
        print("final result:", stop.value)    # B total=7
```

**追问**:1) throw 在委托树上如何传播?——沿着委托链一直扔到当前真正挂起的叶子生成器,叶子捕获则继续,不捕获则异常沿链上抛到调用方。2) yield from 相比手写 for 转发强在哪?——除 next 转发外还双向直通 send/throw、透传子生成器的 StopIteration.value,手写等价物要处理六七个分支,PEP 380 把这些语义收进一条语句。3) await 与 yield from 在字节码层什么关系?——await 编译为 GET_AWAITABLE + SEND 一族指令,语义是「带协议校验的 yield from」:对协程直接驱动,对其他对象先取 __await__。4) 生产陷阱?——委托树中间层生成器没预激就被 send 非 None 值,TypeError 从最深层冒出来难定位;以及委托 list 失去惰性,大流量场景内存翻倍。
