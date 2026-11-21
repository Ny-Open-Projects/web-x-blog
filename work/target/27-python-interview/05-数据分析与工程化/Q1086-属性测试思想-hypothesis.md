---
title: [Q1086] 属性测试思想 hypothesis
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1086 · 属性测试思想 hypothesis

> 难度:★★★★ | 标签:property-based, hypothesis

**问**:example-based 测试永远只是你想到的例子,hypothesis 的属性测试到底换了个什么思路?

**答**:属性测试把"例子 + 期望输出"换成"性质 + 输入生成器":声明输入空间的策略(strategy,如任意整数列表),声明对任意输入都成立的性质(如"reverse 两次等于自身"),框架生成成百上千随机输入验证,一旦失败自动缩小(shrink)出最小反例。价值在于它探索人类想不到的边界:空列表、极值、unicode、NaN。工程采用:核心纯函数、序列化/解析对、金额计算优先用属性测试;集成测试仍以 example-based 为主。

```python
# file: code/05_数据分析与工程化/q1086_hypothesis_idea.py

def reverse_twice(xs):
    return list(reversed(list(reversed(xs))))

try:
    from hypothesis import given, strategies as st
    HAS_HYP = True
except ImportError:
    HAS_HYP = False

if HAS_HYP:
    @given(st.lists(st.integers()))
    def test_reverse_twice(xs):
        assert reverse_twice(xs) == xs

    test_reverse_twice()
    print("hypothesis 随机生成 + 自动缩小,验证通过")
else:
    import random
    random.seed(0)
    for _ in range(300):
        xs = [random.randint(-100, 100) for _ in range(random.randint(0, 20))]
        assert reverse_twice(xs) == xs
    print("未安装 hypothesis,降级为随机 300 组性质验证,思想相同")
```

**追问**:
- 追问 1:shrink 是怎么工作的?—— 从失败输入出发,尝试更简单的变体(去元素、换 0 值),仍失败则继续缩小,直到最小反例。
- 追问 2:hypothesis 怎么保证 bug 不被"随机运气"掩盖?—— 失败案例写入数据库(example database),后续运行优先重放历史反例。
