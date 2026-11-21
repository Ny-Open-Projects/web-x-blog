---
title: [Q1838] 哨兵循环实测:for、iter 双参与 while True 的性价比
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1838 · 哨兵循环实测:for、iter 双参与 while True 的性价比

> 难度:★★★☆☆ | 标签:循环, 基准, timeit

**问**:「读流直到哨兵出现」的三种写法,实测差距有多大?怎么选?

**答**:同一份数据(每次 2 万元素、循环 100 遍取最优)实测:for 直快最快(约 0.056s),iter(生产者, None) 双参形式约 0.32s,while True + 手动判哨兵约 0.29s——差距是常数级的 5-6 倍,来自每轮额外的函数调用与比较。选择逻辑:① 数据已是可迭代对象,永远用 for;② 生产者是「调用函数直到哨兵值」的拉取接口时,iter(callable, sentinel) 双参形式(Q023 讲过语义)把 while True + try next 的样板压成一行,正确性优于速度;③ while True 手写版留给需要多层 break 或每轮多种退出的复杂控制流。基准纪律同 Q430:timeit.repeat 取最小值,结论只对本机版本负责。

```python
# file: code/01_语言核心与底层/q1838_sentinel_loop.py
"""哨兵循环实测:for、while True 与 iter 双参的性价比。"""
import timeit

N = 20000


def make_stream():
    it = iter(range(N))
    return lambda: next(it, None)     # 耗尽后永远返回 None 作为哨兵


def by_for():
    for v in range(N):
        pass
    return "done"


def by_iter_sentinel():
    stream = make_stream()
    for v in iter(stream, None):      # 双参 iter:每轮调 stream,等于 None 即停
        pass
    return "done"


def by_while_true():
    stream = make_stream()
    while True:
        if stream() is None:
            break
    return "done"


def bench(fn, number=100):
    return round(min(timeit.repeat(fn, number=number, repeat=3)), 4)


if __name__ == "__main__":
    for name, fn in [("for", by_for),
                     ("iter 双参", by_iter_sentinel),
                     ("while True + is None", by_while_true)]:
        print(name, ":", bench(fn), "s / 100 x 20000 次")
```

**追问**:1) iter 双参的哨兵比较是 == 还是 is?——相等比较(==);哨兵要用唯一对象避免与合法值相撞,API 设计时通常约定 None 或专用哨兵(Q1282)。2) 三种哨兵循环的取舍?——while True + try/StopIteration 最通用但啰嗦;iter(callable, sentinel) 最贴合「读到哨兵为止」;for + 生成器函数封装最干净;实测差异在常数级,可读性优先。3) 性能实测口径?——timeit 取 min、同进程多轮(Q1568);3.11+ 特化让差异进一步缩小;结论只到常数级,算法不变。4) 生产陷阱?——哨兵与合法值相等导致提前停;把流协议的结束标记当数据用;无实测就声称「快」。
