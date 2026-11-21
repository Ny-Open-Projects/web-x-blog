---
title: [Q533] 富比较与 total_ordering
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q533 · 富比较与 total_ordering

> 难度:★★★☆ | 标签:运算符, 排序

**问**:实现排序支持最少要写几个比较方法?functools.total_ordering 的代价是什么?

**答**:sorted/min/max 只要求 __lt__ 一个方法;== 建议一并实现(否则用身份比较,值相等的两个对象不相等,排序结果看似正常但去重行为诡异)。functools.total_ordering 装饰器从 __eq__ + 一个比较方法推导出其余(__le__/__gt__/__ge__),代价是每次比较经过一层间接调用,且反向运算可能落到 NotImplemented 路径,热点代码手写全部六个更直接。实现时对不支持的类型返回 NotImplemented 让解释器尝试反射运算,而不是抛 TypeError。

```python
# file: code/01_语言核心与底层/q533_total_ordering.py
import functools

@functools.total_ordering
class SemVer:
    def __init__(self, major, minor):
        self.major, self.minor = major, minor

    def __eq__(self, other):
        if not isinstance(other, SemVer):
            return NotImplemented
        return (self.major, self.minor) == (other.major, other.minor)

    def __lt__(self, other):
        if not isinstance(other, SemVer):
            return NotImplemented
        return (self.major, self.minor) < (other.major, other.minor)

    def __repr__(self):
        return f"{self.major}.{self.minor}"

if __name__ == "__main__":
    a, b, c = SemVer(1, 0), SemVer(1, 2), SemVer(2, 0)
    print(a < b, b <= c, c > a, a != b)   # <= 与 > 由 total_ordering 推导
    print(sorted([c, a, b]))
    print(max(a, c))
```

**追问**:1) 为什么 __eq__ 与 __hash__ 必须一起考虑?——定义 __eq__ 后默认 __hash__ 被置 None,对象不可哈希;要保持可哈希必须自定义 __hash__ 且保证「相等对象哈希相等」,否则 dict 行为错乱。2) total_ordering 的成本?——functools.total_ordering 由 __lt__ + __eq__ 派生 le/gt/ge,每次比较多一层 Python 函数调用;热路径手写全部比较或用 dataclass(order=True) 让 C 层生成。3) total_ordering 的底层要求?——至少定义一个比较方法加 __eq__,装饰器为缺失者生成基于 __lt__ 组合的包装;生成的方法语义要与业务排序一致。4) 生产陷阱?——只定义 __lt__ 不定义 __eq__,sorted 能用但相等判定退化为 identity;NaN 参与违反全序假设(heap/sort 行为未定义);比较方法里抛异常而不是返回 NotImplemented。
