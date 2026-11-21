---
title: [Q543] __contains__ 与 in 的默认成本
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q543 · __contains__ 与 in 的默认成本

> 难度:★★★☆ | 标签:容器, 性能

**问**:`x in obj` 的查找顺序是什么?一个 O(n) 的迭代器容器怎么变成 O(1)?

**答**:in 的分派:优先调用 __contains__;没有则尝试迭代(逐个 == 比较,默认实现 O(n));对旧式序列再回退下标协议。所以「只定义了 __iter__ 的类」成员测试就是全量遍历——慢在语义而不是实现,若容器有结构(区间、有序、哈希),定义 __contains__ 直接利用结构判定,可从 O(n) 降到 O(1)/O(log n)。in 运算符还隐含约定:应返回 bool 且不抛异常(找不到返回 False 而不是报错),自定义实现要遵守。

```python
# file: code/01_语言核心与底层/q543_contains.py
import time

class SlowRange:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return iter(range(self.n))        # 没有 __contains__:in 走全量迭代

class FastRange(SlowRange):
    def __contains__(self, x):
        return 0 <= x < self.n            # 结构化判定:O(1)

if __name__ == "__main__":
    sr, fr = SlowRange(10_000_000), FastRange(10_000_000)

    start = time.perf_counter()
    _ = 9_999_999 in sr
    print("iter-based:", round(time.perf_counter() - start, 4), "s")

    start = time.perf_counter()
    _ = 9_999_999 in fr
    print("structured:", round(time.perf_counter() - start, 6), "s")
```

**追问**:1) dict/set 的 in 和 list 的 in 差在哪?——dict/set 走哈希表 O(1);list 走线性扫描 O(n),高频成员测试应转 set——「list 误当 set 用」是热路径性能的常见病因。2) in 的分派顺序?——优先调 __contains__;没有则回退迭代协议逐元素 ==;自定义 __contains__ 可以定义任意语义(str 的子串判定就是特化实现)。3) 底层路径?——set/dict 的 sq_contains 直连哈希探测;list 的是 PyObject_RichCompare 逐元素比较,元素多时每次 in 都是全扫。4) 生产陷阱?——循环内 `x in big_list` 每次全扫,预先建 set;自定义容器忘 __contains__ 退化成迭代;`in` 用于子串判断的副作用("cat" in "concatenate" 为 True)在标签匹配里出 bug。
