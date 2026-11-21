---
title: [Q1286] sys.setprofile:性能探针的原理与开销
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1286 · sys.setprofile:性能探针的原理与开销

> 难度:★★★☆☆ | 标签:sys.setprofile, 性能, 内省

**问**:cProfile 是怎么实现的?为什么 profile 函数只收 call/return 事件而不给每行?自己写探针要注意什么?

**答**:sys.setprofile 注册的探针函数在 C 层事件点被回调,事件只有 call、return、c_call、c_return——没有 line 事件,这是它和 sys.settrace(Q552)的分界:settrace 面向调试器/覆盖率(需要行级),setprofile 面向性能采样(函数粒度足够,省掉每行的巨大开销)。cProfile 就是一个内置的 profile 探针。自己写探针的铁律:必须 try/finally 里 `setprofile(None)` 还原,否则全局所有代码都在回调里跑,程序慢一个数量级;探针内不能做重活(打日志、建大对象),通常只累加计数。注意探针在目标线程有效,多进程/多线程要分别挂;与 Q430 的结论呼应:探针本身会改变时序,热点排序可信,绝对耗时不可信。

```python
# file: code/01_语言核心与底层/q1286_setprofile.py
import sys
from collections import Counter


def inner_a():
    return 1


def inner_b():
    return inner_a() + inner_a()


def outer():
    return inner_b() + inner_a()


if __name__ == "__main__":
    calls = Counter()

    def profiler(frame, event, arg):
        if event == "call":
            calls[frame.f_code.co_name] += 1

    sys.setprofile(profiler)
    try:
        outer()
    finally:
        sys.setprofile(None)               # 探针必须拆除,否则全局减速
    print("call counts:", dict(calls))
    print("c_call 事件同样存在,cProfile 因此能统计内置函数")
```

**追问**:1) 为什么 profile 回调里再抛异常不会中断被测函数?——解释器对探针异常做了静默处理(打印后忽略),这是为了探针自身 bug 不污染业务,但也意味着探针错误容易被忽视。2) setprofile 的事件模型?——'call'/'c_call'/'return'/'c_return' 四类,函数粒度(非行级),开销比 settrace 低但仍数量级;3.12 的 sys.monitoring 是接管方向(Q552)。3) 与 settrace 的分工?——profile 看调用关系与耗时,trace 看行级与局部变量;两者可同时设置但语义独立,调试器有自己的组合方式。4) 生产陷阱?——常开探针把性能拖垮,生产用采样式(py-spy);探针改变时序掩盖竞态问题;探针静默吞错导致「测了个寂寞」。
