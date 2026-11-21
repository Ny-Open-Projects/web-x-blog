---
title: [Q2075] 生成器 send 的启动契约与预激模式
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2075 · 生成器 send 的启动契约与预激模式

> 难度:★★★★☆ | 标签:生成器, send, 协议

**问**:刚创建的生成器调用 gen.send(10) 为什么报 TypeError?send 的启动契约是什么?

**答**:send(value) 的语义是「恢复挂起在 yield 处的帧,并把 value 作为该 yield 表达式的值」;刚创建的生成器还停在函数开头,根本没有挂起的 yield 可接收,所以协议规定:启动前 send 非 None 一律 TypeError,只有 send(None) 合法,等价于 next(gen)。完整契约分三步——next 或 send(None) 启动并推进到第一个 yield;此后才能 send 实值双向通信(Q431);close 或耗尽收尾。工程上用预激装饰器封装「先 next 再交给调用方」的仪式,让业务代码拿到的生成器可以直接 send;inspect.getgeneratorstate 能观测 GEN_CREATED、SUSPENDED、CLOSED 的状态机迁移,demo 全程打印。

```python
# file: code/01_语言核心与底层/q2075_send_priming.py
"""生成器 send 的启动契约:先 next 后 send,以及状态机观测。"""
import inspect


def echo():
    total = 0
    while True:
        got = yield total          # 首次推进到 yield 才会停在这里
        total += got


def primed(gen):
    """预激:推进到第一个 yield,调用方即可直接 send。"""
    next(gen)
    return gen


if __name__ == "__main__":
    g = echo()
    print("刚创建:", inspect.getgeneratorstate(g))
    try:
        g.send(10)                 # 未启动就 send 非 None
    except TypeError as e:
        print("启动前 send 报错:", e)

    print("send(None) 等价 next,启动并返回:", g.send(None))
    print("启动后:", inspect.getgeneratorstate(g))
    print("send(10):", g.send(10), "| send(32):", g.send(32))

    h = primed(echo())
    print("预激后直接 send(7):", h.send(7))
    h.close()
    print("close 后:", inspect.getgeneratorstate(h))
```

**追问**:1) 为什么 send(None) 可以启动?——None 表示「无值推进」,是协议规定的合法起点,不会注入任何 yield 表达式的值;预激的现代化身?——yield from 与 async/await 都隐式完成预激,手工预激只服务于裸生成器协议场景。2) 启动契约的完整内容?——未启动生成器只接受 next/send(None),非 None 抛 TypeError(Q431);close/throw 同样要求已启动——「先预激再使用」是一切生成器协议的地基。3) 预激模式的角色演变?——PEP 342 时代预激装饰器是必需品;yield from/await 把预激收进协议;今天只有手写调度器/驱动器才需要。4) 生产陷阱?——忘预激的 TypeError 掩盖真实异常;多个消费者交错 send;把「send 非 None 启动」当成可能行为写条件分支。
