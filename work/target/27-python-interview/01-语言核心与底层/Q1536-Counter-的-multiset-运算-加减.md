---
title: [Q1536] Counter 的 multiset 运算:加减交并的语义
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1536 · Counter 的 multiset 运算:加减交并的语义

> 难度:★★★★☆ | 标签:Counter, multiset, collections

**问**:Counter 的 +、-、&、| 各是什么语义?为什么相减后非正计数的条目会消失?什么时候该用 multiset 思维?

**答**:Counter 是多重集合(multiset),运算符围绕「计数」定义:c1 - c2 是差(每元素计数相减,扣成非正的条目直接消失,而不是记 0);+ 取正计数求和,& 取各元素计数最小值(multiset 交集),| 取最大值(multiset 并集),一元 + 与 - 过滤非正计数。丢弃非正项是刻意的 multiset 语义:「不存在」与「0 个」等价,这样 elements()、most_common、迭代都干净。工程场景:库存扣减(下单 stock - order)、订单合并(stock + order)、词袋 diff、权限并集。注意 3.10 起相等比较把缺失视作 0,3.9 仍是严格 dict 相等——版本差异是加分考点;要保留零/负计数就手工循环或 defaultdict(int)。

```python
# file: code/01_语言核心与底层/q1536_counter_multiset.py
from collections import Counter

STOCK = Counter({"apple": 10, "banana": 6, "cherry": 0})
ORDER_A = Counter({"apple": 3, "banana": 1, "durian": 2})
ORDER_B = Counter({"apple": 1, "banana": 4})


def ship(stock, order):
    """扣减库存:multiset 差,扣到非正的品项从结果消失。"""
    return stock - order


if __name__ == "__main__":
    print("stock:", dict(STOCK))
    left = ship(STOCK, ORDER_A)
    print("after order A:", dict(left))         # durian 扣成 -2 直接消失

    print("A & B:", dict(ORDER_A & ORDER_B))    # 各取最小计数
    print("A | B:", dict(ORDER_A | ORDER_B))    # 各取最大计数
    print("+A   :", dict(+ORDER_A), "-A:", dict(-ORDER_A))

    total = ORDER_A + ORDER_B
    print("A + B:", dict(total))                # 汇总订单

    # 相等比较的版本差异:3.10 起缺失视作零,3.9 是严格 dict 相等
    zeroish = Counter({"apple": 0})
    print("zero-count equality:", zeroish == Counter(),
          " 3.10+ 为 True,3.9 为 False")

    # 元素展开:按计数重复
    print("elements:", sorted(total.elements()))
    print("most_common:", ORDER_A.most_common(2))
```

**追问**:1) 为什么 Counter 减法丢掉非正计数而不是记 0?——multiset 语义里「不存在」和「0 个」等价,丢弃让 elements 与相等比较都干净;要保留零值就手工循环。2) multiset 运算的全貌?——+ 与 - 都丢弃非正;& | 取 min/max(非零);elements() 按计数展开;most_common(n) 内部用 heapq.nlargest 高效取 Top-N。3) update 的语义?——计数相加(不是覆盖);要覆盖用直接赋值或先 clear;subtract 是相减且保留非正(与 - 不同)。4) 生产陷阱?——以为 c1 - c2 会保留 0/负值;update 与覆盖语义混淆;most_common 对相同计数依赖插入序,跨进程顺序不稳定(哈希盐)。
